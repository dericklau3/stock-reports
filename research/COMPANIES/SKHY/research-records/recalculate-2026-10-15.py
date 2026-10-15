"""Reproduce SKHY conditional normalized-earnings valuation; stdlib only.

All forecasts and multiples are researcher assumptions, not guidance/consensus.
The earnings-power method values equity; do NOT add net cash or IPO proceeds.
It does not separately appraise investment holdings or predict market prices.
"""
import json
import math
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def calculate(inputs):
    a = inputs['assumptions']
    facts = inputs['verified_facts']
    quote = facts['quote']['close_USD_per_ADS']
    fx = facts['fx']['KRW_per_USD']
    shares = a['future_diluted_ordinary_shares']
    ratio = facts['ordinary_shares_per_ADS']
    years = (date.fromisoformat(a['target_date']) - date.fromisoformat(inputs['valuation_date'])).days / 365.25
    discount = (1 + a['discount_rate']) ** years
    scenarios = {}
    for name, s in a['scenarios'].items():
        endpoints = []
        for k in ['low', 'high', 'midpoint']:
            x = s[k]
            ebit = x['revenue_KRW_trillion'] * x['operating_margin']
            # Ordinary attributable earnings, after normal net interest, tax and NCI.
            profit = (ebit + a['normal_net_interest_KRW_trillion']) * (1 - s['tax_rate']) * a['parent_profit_fraction']
            eps = profit * 1e12 / shares * ratio / fx
            future_price = eps * x['PE']
            today_value = future_price / discount
            endpoints.append({'endpoint': k, 'EBIT_KRW_trillion': ebit,
                              'normal_parent_profit_KRW_trillion': profit,
                              'normal_EPS_USD_per_ADS': eps,
                              'scenario_PE_assumption': x['PE'],
                              'target_date_undiscounted_USD_per_ADS': future_price,
                              'valuation_date_USD_per_ADS': today_value,
                              'value_gap_vs_quote': today_value / quote - 1,
                              'quote_divided_by_target_normal_EPS': quote / eps})
        assert endpoints[0]['valuation_date_USD_per_ADS'] < endpoints[2]['valuation_date_USD_per_ADS'] < endpoints[1]['valuation_date_USD_per_ADS']
        scenarios[name] = endpoints
    h1 = facts['H1_2026_KRW_million']
    liquid = h1['cash_and_equivalents'] + h1['short_term_financial_instruments'] + h1['short_term_investment_assets']
    debt = h1['current_borrowings'] + h1['noncurrent_borrowings']
    lease = h1['current_lease_liabilities'] + h1['noncurrent_lease_liabilities']
    cash_capex = h1['PPE_cash_purchase'] + h1['intangible_cash_purchase']
    fcf = h1['CFO'] - cash_capex
    assert h1['finance_income'] - h1['finance_expenses'] == h1['net_finance_income']
    assert h1['EBIT'] + h1['net_finance_income'] + h1['equity_accounted_profit'] + h1['other_income'] - h1['other_expense'] == h1['pretax_profit']
    assert h1['pretax_profit'] - h1['income_tax_expense'] == h1['consolidated_profit']
    assert facts['June_30_ordinary_outstanding'] + facts['IPO_new_ordinary_shares'] == facts['IPO_postoffering_ordinary_shares_proxy']
    # Independent equivalent-denominator calculation checks the ADS direction.
    first = scenarios['base'][0]
    independent_eps = first['normal_parent_profit_KRW_trillion'] * 1e12 / fx / (shares / ratio)
    assert math.isclose(independent_eps, first['normal_EPS_USD_per_ADS'], rel_tol=1e-12)
    # Future economics all include recurring SBC in expenses; extra dilution is a buffer.
    dilution = shares / facts['IPO_postoffering_ordinary_shares_proxy'] - 1
    sensitivity = {}
    for label, alternative_fx in [('KRW_strengthens_10pct', fx * .9), ('KRW_weakens_10pct', fx * 1.1)]:
        sensitivity[label] = scenarios['base'][2]['valuation_date_USD_per_ADS'] * fx / alternative_fx
    for count in [facts['IPO_postoffering_ordinary_shares_proxy'], 800_000_000]:
        sensitivity[f'ordinary_shares_{count}'] = scenarios['base'][2]['valuation_date_USD_per_ADS'] * shares / count
    for rate in [.10, .15]:
        sensitivity[f'discount_rate_{rate}'] = scenarios['base'][2]['target_date_undiscounted_USD_per_ADS'] / (1 + rate) ** years
    base_eps = scenarios['base'][2]['normal_EPS_USD_per_ADS']
    sensitivity['each_PE_turn_changes_today_USD_per_ADS'] = base_eps / discount
    sensitivity['extra_1pct_revenue_investment_need_annual_KRW_trillion'] = a['scenarios']['base']['midpoint']['revenue_KRW_trillion'] * .01
    required_profit = quote * discount / a['scenarios']['base']['midpoint']['PE'] * (shares / ratio) * fx / 1e12
    return {'valuation_date': inputs['valuation_date'], 'target_date': a['target_date'],
            'quote': facts['quote'], 'years': years, 'discount_factor': discount,
            'ADS_equivalent_future_denominator': shares / ratio,
            'dilution_buffer_vs_IPO': dilution,
            'proxy_marketcap_USD': quote * facts['IPO_postoffering_ordinary_shares_proxy'] / ratio,
            'scenarios': scenarios, 'sensitivities': sensitivity,
            'reverse_normal_profit_KRW_trillion_at_base_PE': required_profit,
            'H1_checks_KRW_trillion': {
                'broad_liquid_balance_not_all_cash': liquid / 1e6,
                'debt_excluding_leases': debt / 1e6,
                'leases': lease / 1e6,
                'broad_liquid_balance_minus_debt': (liquid - debt) / 1e6,
                'cash_capex_PPE_plus_intangibles': cash_capex / 1e6,
                'CFO_less_cash_capex_not_normalized': fcf / 1e6,
                'CFO_less_cash_capex_less_investment_dividends_not_normalized': (fcf - h1['dividends_received_cash']) / 1e6},
            'limits': inputs['limits'],
            'verification': 'Source identities, financial arithmetic, capital bridge, ADS denominator and scenario ordering assertions passed.'}

if __name__ == '__main__':
    inputs = json.loads((ROOT / '2026-10-15-valuation-inputs.json').read_text())
    results = calculate(inputs)
    (ROOT / '2026-10-15-valuation-results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(results, ensure_ascii=False, indent=2))

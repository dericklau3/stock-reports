import copy, hashlib, json, pathlib, shutil, subprocess, sys
root=pathlib.Path(__file__).resolve().parent.parent
out=root/'results'
def save(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def fact(value,material,reason):
    return {'value':value,'basis':'analyst','as_of':'2026-10-20','rationale':f'synthetic 材料{material}，虚构题设，仅限本实验；{reason}。详见 results/notes.md。'}
base=json.loads((root/'skill/examples/valuation-p1-v4-input.example.json').read_text())
sotp=base['analyses'][1]
sotp['corporate_cost_pv_m']=fact(40,'B','未分配总部费用现值')
sotp['nonoperating_assets_m']=fact(5,'B','独立非经营资产，不含在分部EV或现金中')
sotp['overlap_reconciliation']='synthetic 材料A/B/C/D：成熟业务与项目独立，持有100%；总部费用仅扣一次；非经营资产和现金分列；融资仅桥接现金及股数；项目期间投入不含于终值或其他分部，失败退出义务只含在失败EV。'
legacy,project=sotp['segments']
legacy['ownership']=fact(1,'B','经济持有比例100%')
legacy['enterprise_value_m']=fact(500,'B','成熟业务当期独立EV，非实证估值')
legacy['boundary_note']='synthetic 材料B：不含总部、项目、现金、债务或独立非经营资产。'
project['ownership']=fact(1,'B/C','题设持有比例100%')
project['boundary_note']='synthetic 材料C/D：新项目独立经营价值，不含成熟业务、总部、非经营资产或资本桥接。'
project['wacc']=fact(.1,'C','题设WACC，不额外重复惩罚成功失败风险')
project['success_probability']=fact(.25,'C','题设条件概率25%，依据仅限本虚构实验，无真实统计或同业参照证据')
project['success_ev_m']=fact(600,'C','目标日成功经营EV，不含此前投入')
project['failure_ev_m']=fact(-50,'C','目标日净经营残值已含退出义务，不含此前投入，保留负值')
project['cost_note']='synthetic 材料C/D：期间投入独立扣除，未在A/B及终值扣除；失败EV已含目标日退出义务，costs不重复扣除。'
project['cost_treatment']='separate'
capital={'bridge_as_of':'2026-10-20','reconciliation_note':'synthetic 材料A：9月末80股、现金20；10月20日收盘前增发20股，每股5，募资100、零费用，无其他变动，故当日100股、现金120；债80及其他索偿10不变。'}
for key,value,reason in [('shares_m',100,'80+20=100百万经济股'),('cash_m',120,'20+20×5=120百万可用现金'),('debt_m',80,'当日有息债务，期间无其他变动'),('other_claims_m',10,'当日其他索偿，期间无其他变动')]:
    capital[key]=fact(value,'A',reason)
    capital[key]['source_url']='https://example.org/DEMO/financing'
for scope in ['partial','counterfactual']:
    for timing in ['normal','delay']:
        a=copy.deepcopy(sotp); a['name']=scope+'_'+timing; a['scenario']='base'
        p=a['segments'][1]; p['target_date']='2028-10-20' if timing=='normal' else '2029-10-20'
        p['costs']=[{'on':'2027-10-20','success_cost_m':fact(80,'C','成功路径当日投入'),'failure_cost_m':fact(40,'C','失败路径当日投入')}]
        if timing=='delay':
            p['costs'].append({'on':'2028-10-20','success_cost_m':fact(60,'D','延期成功路径追加投入'),'failure_cost_m':fact(20,'D','延期失败路径追加投入')})
        a['scope']={'kind':'partial' if scope=='partial' else 'whole','description':('synthetic 材料E：排除未知机器人业务的局部SOTP；不能代表整体或股价下限' if scope=='partial' else 'synthetic 材料E：仅在E不存在且无其他业务遗漏的整体反事实条件版本，不能用于现实整体判断'),'material_omissions':['synthetic 材料E：机器人业务收益和资金消耗均未量化，净价值未知'] if scope=='partial' else []}
        doc={'schema_version':4,'ticker':'DEMO','currency':'USD','valuation_date':'2026-10-20','price':{'value':25,'basis':'market','as_of':'2026-10-19','source_url':'https://example.org/DEMO/quote'},'capital':capital,'analyses':[a]}
        save(out/'inputs'/f'{a["name"]}.json',doc)
for name in ['valuation_engine.py','valuation_p1.py','valuation_p2.py']:
    shutil.copy2(root/'skill'/name,out/'source-code'/name)
save(out/'source-code/sha256.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'source-code').glob('*.py')})
commands=[]
def run(args):
    proc=subprocess.run([sys.executable]+args,cwd=root,text=True,capture_output=True)
    commands.append({'command':[sys.executable]+args,'cwd':str(root),'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
    save(out/'execution-log.json',commands)
    print(args, 'exit_code=',proc.returncode,proc.stderr)
    if proc.returncode: sys.exit(proc.returncode)
for scope in ['partial','counterfactual']:
    for timing in ['normal','delay']:
        name=scope+'_'+timing
        run(['skill/valuation_p1.py',f'results/inputs/{name}.json','--output',f'results/outputs/{name}.json'])
        if scope=='counterfactual':
            run(['skill/valuation_p2.py','freeze',f'results/inputs/{name}.json','--name',name,'--output',f'results/snapshots/{name}.json'])

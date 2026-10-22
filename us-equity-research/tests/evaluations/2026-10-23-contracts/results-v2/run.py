import hashlib,json,pathlib,shutil,subprocess,sys
root=pathlib.Path(__file__).resolve().parent.parent
out=root/'results-v2'
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
missing='synthetic 材料A/D：延期成功路径累计投入140超过当日现金120至少20；资金来源、融资成本与未来股数未界定，不能以成熟业务EV500代替可用现金。'
for name in ['partial_normal','partial_delay','counterfactual_normal','counterfactual_delay']:
 d=json.loads((root/f'results/inputs/{name}.json').read_text()); a=d['analyses'][0]
 def rewrite(x):
  if isinstance(x,dict):return {k:rewrite(v) for k,v in x.items()}
  if isinstance(x,list):return [rewrite(v) for v in x]
  return x.replace('results/notes.md','results-v2/notes.md') if isinstance(x,str) else x
 d=rewrite(d);a=d['analyses'][0]
 if name.endswith('delay'):
  a['scope']['kind']='partial';a['scope']['material_omissions'].append(missing)
  a['scope']['description']+='；融资与每股影响未完成，仍属局部条件计算，不能进行整股比较或冻结。'
 save(out/f'inputs/{name}.json',d)
for name in ['valuation_engine.py','valuation_p1.py','valuation_p2.py']:
 shutil.copy2(root/'skill'/name,out/'source-code'/name)
shutil.copy2(root/'skill/references/valuation-p1.md',out/'source-code/valuation-p1.md')
save(out/'source-code/sha256.json',{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'source-code').iterdir() if p.is_file()})
log=[]
def run(args):
 p=subprocess.run([sys.executable]+args,cwd=root,capture_output=True,text=True)
 log.append({'command':[sys.executable]+args,'cwd':str(root),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr});save(out/'execution-log.json',log)
 print(args,p.returncode,p.stderr)
for name in ['partial_normal','partial_delay','counterfactual_normal','counterfactual_delay']:
 run(['skill/valuation_p1.py',f'results-v2/inputs/{name}.json','--output',f'results-v2/outputs/{name}.json'])
 if name.startswith('counterfactual'):
  run(['skill/valuation_p2.py','freeze',f'results-v2/inputs/{name}.json','--name',name,'--output',f'results-v2/snapshots/{name}.json'])

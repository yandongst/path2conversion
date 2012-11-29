import sys

x_imp={}
x_clk={}
x_ctr1={}
x_vtr={}
x_ctc={}
x_vtc={}
for l in sys.stdin:
  l =l.strip()
  campid,campname,cates,imp,clk,ctr1,vtr,ctc,vtc=l.split('\t')
  key=campid+'---'+cates+'---'+campname
  if key not in x_imp:
    x_imp[key]=0
  if key not in x_clk:
    x_clk[key]=0
  if key not in x_ctr1:
    x_ctr1[key]=0
  if key not in x_vtr:
    x_vtr[key]=0
  if key not in x_ctc:
    x_ctc[key]=0
  if key not in x_vtc:
    x_vtc[key]=0
  x_imp[key]+=float(imp)
  x_clk[key]+=float(clk)
  x_ctr1[key]+=float(ctr1)
  x_vtr[key]+=float(vtr)
  x_ctc[key]+=float(ctc)
  x_vtc[key]+=float(vtc)

for k in x_imp:
  imp=x_imp[k]
  clk=0
  ctr=0.0
  ctr1=0
  vtr=0
  ctc=0
  vtc=0
  if k in x_clk:
    clk=x_clk[k]
  if k in x_ctr1:
    ctr1=x_ctr1[k]
  if k in x_vtr:
    vtr=x_vtr[k]
  if k in x_ctc:
    ctc=x_ctc[k]
  if k in x_vtc:
    vtc=x_vtc[k]
  if imp>0: ctr=clk/imp
  campid,cates,campname=k.split('---')
  
  print '\t'.join([campid,campname,cates,str(imp),str(clk),str(ctr),str(ctr1),str(vtr),str(ctc),str(vtc)])

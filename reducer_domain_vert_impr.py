import sys

x_imp={}
x_clk={}
x_ctr={}
x_vtr={}
x_ctc={}
x_vtc={}

for l in sys.stdin:
  l=l.strip()
  if len(l.split('\t'))!=10:
    print >>sys.stderr,l
    continue
  d,campid,campname,cates,imp,clk,ctr1,vtr1,ctc1,vtc1=l.split('\t')
  key=d+'---'+campid+'---'+campname+'---'+cates
  if key not in x_imp:
    x_imp[key]=0
  if key not in x_clk:
    x_clk[key]=0
  if key not in x_ctr:
    x_ctr[key]=0
  if key not in x_vtr:
    x_vtr[key]=0
  if key not in x_ctc:
    x_ctc[key]=0
  if key not in x_vtc:
    x_vtc[key]=0
  x_imp[key]+=float(imp)
  x_clk[key]+=float(clk)
  x_ctr[key]+=float(ctr1)
  x_vtr[key]+=float(vtr1)
  x_ctc[key]+=float(ctc1)
  x_vtc[key]+=float(vtc1)

for k in x_imp:
  d,campid,campname,cates=k.split('---',3)

  clk=0
  ctr=0.0
  ctr1=0.0
  vtr1=0.0
  ctc1=0.0
  vtc1=0.0
  if k in x_clk:
    clk=x_clk[k]
  if k in x_ctr:
    ctr1=x_ctr[k]
  if k in x_vtr:
    vtr1=x_vtr[k]
  if k in x_ctc:
    ctc1=x_ctc[k]
  if k in x_vtc:
    vtc1=x_vtc[k]
  if x_imp[k]>0.0: ctr=clk/x_imp[k]
  print '\t'.join([campid,campname,d,cates,str(x_imp[k]),str(clk), str(ctr),str(ctr1), str(vtr1), str(ctc1), str(vtc1)])

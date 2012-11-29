
import sys

x={}

for l in sys.stdin:
  l = l.strip()
  fs = l.split('\t')
  key=fs[0]
  event=fs[1]
  cnt=float(fs[2])

  if key not in x:
    x[key]={}

  if event not in x[key]:
    x[key][event]=0

  x[key][event]+=cnt

for k in x:
  impr=0
  click=0
  ctr=0
  vtr=0
  ctc=0
  vtc=0
  if 'impr' in x[k]:impr=x[k]['impr']
  if 'click' in x[k]:click=x[k]['click']
  if 'ctr' in x[k]:ctr=x[k]['ctr']
  if 'vtr' in x[k]:vtr=x[k]['vtr']
  if 'ctc' in x[k]:ctc=x[k]['ctc']
  if 'vtc' in x[k]:vtc=x[k]['vtc']
  ctrrate=0.0
  if impr>0.0: ctrrate=click/impr
  print '\t'.join([k,str(impr),str(click),str(ctrrate), str(ctr),str(vtr),str(ctc),str(vtc)])
  


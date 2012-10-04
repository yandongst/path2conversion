import sys

delimit='-;,'

liftevent='1'

adevent='13'

cnt_beforead=0
cnt_afterad=0

liftevent=sys.argv[1]

for l in sys.stdin:
  l = l .strip()
  c,ds=l.split('\t')
  l_e=[]
  for d in ds.split(delimit):
    ts,e=d.split(',')
    l_e.append(e)
  #print l_e
  if adevent not in l_e: continue
  adexposure=False
  for e in l_e:
    if e ==adevent:
      adexposure=True
    if e==liftevent:
      if adexposure:
        cnt_afterad+=1
      else:
        cnt_beforead+=1


print 'event:'+liftevent, cnt_beforead, cnt_afterad,float(cnt_afterad)/cnt_beforead

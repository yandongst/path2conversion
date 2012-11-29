import sys
x={}
for l in sys.stdin:
  k,v=l.strip().split('\t')
  if k in x:
    x[k]+=float(v)
  else:
    x[k]=float(v)

for k in x:
  print k+'\t'+x[v]
  

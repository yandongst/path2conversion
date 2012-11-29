
import sys

x={}

for l in sys.stdin:
  l = l.strip()
  fs=l.split('\t')
  cate_id=fs[1]
  domain=fs[0]
  impr=fs[2]
  if domain not in x:
    x[domain]=[]
  x[domain].append((cate_id,float(impr)))

for d in x:
  sum=0.0
  for c_i in x[d]:
    cid,imp=c_i
    sum+=imp
  for c_i in x[d]:
    cid,imp=c_i
    print '\t'.join([d,cid,str(imp/sum)])

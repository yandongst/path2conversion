import sys

for l in sys.stdin:
  l = l.strip()
  fs=l.split('\t')
  cate_id=fs[0]
  domain=fs[1]
  impr=fs[2]
  print '\t'.join([domain,cate_id,impr])

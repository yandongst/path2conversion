import sys
from collections import defaultdict

x_camp={}

for l in sys.stdin:
  l = l.strip()
  k,v=l.split('\t')
  #print l
  if k not in x_camp:
    x_camp[k]=defaultdict(int)
  x_camp[k][v]+=1

#print x_camp

for rt in x_camp:
  cnt=x_camp[rt]
  for field in cnt:
    print rt+'\t'+field+'\t'+str(cnt[field])
  

import sys
from collections import defaultdict

x={}

for l in sys.stdin:
  l = l.strip()
  adg,status=l.split('\t')
  if adg not in x:
    x[adg]={}
    x[adg]['click-conversion']=0
    x[adg]['lastmatch']=0
    x[adg]['nonlastmatch']=0
    x[adg]['unmatch']=0
  x[adg][status]+=1

for adg in x:
  print adg+'\t'+str(x[adg]['click-conversion']) +'\t'+str(x[adg]['lastmatch']) +'\t'+str(x[adg]['nonlastmatch'])+'\t'+str(x[adg]['unmatch'])

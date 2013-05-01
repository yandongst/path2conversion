import sys
from collections import defaultdict

x={}

for l in sys.stdin:
  l = l.strip()
  adg,status=l.split('\t')
  if adg not in x:
    x[adg]={}
    x[adg]['match']=0
    x[adg]['unmatch']=0
    x[adg]['lastmatch']=0
  x[adg][status]+=1

for adg in x:
  print adg+'\t'+str(x[adg]['lastmatch']) +'\t'+str(x[adg]['match']) +'\t'+str(x[adg]['unmatch'])

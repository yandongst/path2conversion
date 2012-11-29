import sys

fn='adgroup_id2name.csv'
x={}
with open(fn,'r') as f:
  for l in f:
    k,v=l.strip().split(',',1)
    #print k,v.strip('"')
    x[k]=v.strip('"')

for l in sys.stdin:
  l = l.strip()
  fs=l.split(' ')
  adgname_printed=False
  if fs[-1].startswith('a.'):
    adg_name=fs[-1][2:]
    if adg_name in x:
      print  l.strip()+'_'+x[adg_name]
      adgname_printed=True
    
  if not adgname_printed:
    print l.strip()


import sys
import re
import simplejson as json


x_cate=set([])

def read_cate(fn):
  for l in open(fn,'r'):
    l = l.rstrip()
    if not l.startswith('#'):
      x_cate.add(l)

def in_cate(cates):
  for c in cates.split(','):
    if c in x_cate:
      return True
  return False

#read_cate(fn_cate)

cnt_field=sys.argv[1]

for l in sys.stdin:
  l = l.rstrip()
  cookie, data = l.split('\t')
  try:
    j=json.loads(data)
    if j['ctry']!='United States': continue
    if j['evnttyp'] == 'retarg':
      if cnt_field not in j:
        #sys.stderr.write('field '+ cnt_field+' doesn\'t exist!\n')
        #sys.stderr.write(l+'\n')
        continue
      print j['cmpn'].split(';')[0]+'\t'+j[cnt_field]
  except Exception as inst:
    sys.stderr.write(str(inst)+'\n')

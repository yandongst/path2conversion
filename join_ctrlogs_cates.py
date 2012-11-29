import sys

#fn_ctrlog=sys.argv[1]
fn_domain2cate=sys.argv[1]
fn_camp2name=sys.argv[2]

x_d2c={}
x_camp2name={}

def read_domain2cate(fn):
  #print >>sys.stderr, 'reading '+fn
  with open(fn,'r') as f:
    for l in f:
      l=l.strip()
      d,c = l.split(',',1)
      c=c.strip('"')
      x_d2c[d.lower()]=c
      #print d,c

def read_camp2name(fn):
  with open(fn,'r') as f:
    for l in f:
      l=l.strip()
      d,c = l.split(',',1)
      c=c.strip('"')
      x_camp2name[d.lower()]=c

def read_ctrlog():
  #with open(fn,'r') as f:
  for l in sys.stdin:
    l=l.strip()
    fs = l.split('\t')
    dom=fs[0].lower()
    campid=fs[1]
    impr=fs[2]
    click=fs[3]
    cate='n/a'
    campname='n/a'
    if campid in x_camp2name:
      campname=x_camp2name[campid]
    if dom in x_d2c:
      cate=x_d2c[dom].replace(',','-')
    print dom,campname,impr,click,cate

read_domain2cate(fn_domain2cate)
read_camp2name(fn_camp2name)
#print x_d2c
read_ctrlog()

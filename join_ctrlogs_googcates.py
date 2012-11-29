import sys

#fn_ctrlog=sys.argv[1]
fn_domain2cate=sys.argv[1]
fn_camp2name=sys.argv[2]

x_d2c={}
x_camp2name={}

def read_domain2cate2(fn):
  #print >>sys.stderr, 'reading '+fn
  with open(fn,'r') as f:
    for l in f:
      l=l.strip()
      d,c = l.split(',',1)
      c=c.strip('"')
      x_d2c[d.lower()]=c
      #print d,c

def read_domain2cate(fn):
  #print >>sys.stderr, 'reading '+fn
  with open(fn,'r') as f:
    for l in f:
      l=l.strip()
      d,cs = l.split(':',1)
      x_d2c[d.lower()]=[]
      for id_name_weight in cs.split(';'):
        id,name,w=id_name_weight.split('--')
        x_d2c[d.lower()].append((id,name,w))
        #print id,name,w
      #x_d2c[d.lower()]=c
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
    #print l
    fs = l.split('\t')
    if len(fs) !=8:
      #print l
      print fs
      #return
      sys.exit(1)
      continue
    dom=fs[0].lower()
    campid=fs[1]
    impr=float(fs[2])
    click=float(fs[3])
    cate='n/a'
    campname='n/a'
    if campid in x_camp2name:
      campname=x_camp2name[campid]
    if dom in x_d2c:
      #cate=x_d2c[dom].replace(',','-')
      for data in x_d2c[dom]:
        id,name,w=data
        w=float(w)
        #print id,name,w
        print '\t'.join([dom,campid,campname,id,name,str(impr*w),str(click*w)])
    #else:
      #print >> sys.stderr, '===========:'+dom+': deoesnt exist'

read_domain2cate(fn_domain2cate)
#print x_d2c
read_camp2name(fn_camp2name)
#print x_d2c
read_ctrlog()

import sys

fn_domain2cate=sys.argv[1]
fn_camp2name=sys.argv[2]

x_d2c={}
x_camp2name={}

def read_camp2name(fn):
  with open(fn,'r') as f:
    for l in f:
      l=l.strip()
      d,c = l.split(',',1)
      c=c.strip('"')
      x_camp2name[d.lower()]=c

def read_domain2cate(fn):
  with open(fn,'r') as f:
    for l in f:
      d,c,w=l.strip().split('\t')
      level=len(c.split('/'))-1
      if d not in x_d2c:
        x_d2c[d]=[]
      x_d2c[d].append((c,float(w)))


def read_ctrlog():
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
    if len(fs[0].split('--'))!=2:
      continue
    dom,campid=fs[0].split('--')
    impr=float(fs[1])
    click=float(fs[2])
    ctr1=float(fs[4])
    vtr1=float(fs[5])
    ctc1=float(fs[6])
    vtc1=float(fs[7])
    cate='n/a'
    campname='n/a'
    if campid in x_camp2name:
      campname=x_camp2name[campid]
    if dom in x_d2c:
      #cate=x_d2c[dom].replace(',','-')
      for data in x_d2c[dom]:
        cates,w=data
        w=float(w)
        #print id,name,w
        print '\t'.join([dom,campid,campname,cates,str(impr*w),str(click*w), str(ctr1*w), str(vtr1*w), str(ctc1*w), str(vtc1*w)])
  
read_domain2cate(fn_domain2cate)
read_camp2name(fn_camp2name)
read_ctrlog()

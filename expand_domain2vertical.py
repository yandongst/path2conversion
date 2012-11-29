'''
This file for each domain expands its categories and produces all level domain2cate mappings. e.g.
www.abc.com shopping/clothing-0.2
www.abc.com shopping-0.2
...
'''
import sys
from operator import itemgetter 

fn_goog_cates=sys.argv[1]

x={}
x_id2cate={}

class cid_name(object):
  def __init__(self,cid,name):
    self.cid=cid
    self.name=name
  def __repr__(self):
    return self.cid+'--'+self.name
  def __str__(self):
    return self.__repr__()

class category(object): 
  def __init__(self,cid,name,level,parents):
    self.cid=cid
    self.name=name
    self.level=level
    self.parents=[]
    for p in parents:
      pid,pname=p.split('--')
      #self.parents.append((pid,pname))
      self.parents.append(cid_name(pid,pname))
    self.allnodes=[]
    self.allnodes.extend(self.parents)
    self.allnodes.append(cid_name(cid,name))

def read_goog_cate(fn):
  with open(fn,'r') as f:
    for l in f:
      l= l.strip()
      parts=l.split('/')
      leaf_cid,leaf_cname=parts[-1].split('--')
      level=len(parts) #root level is 0
      c=category(leaf_cid,leaf_cname,level,parts[0:-1])
      x_id2cate[leaf_cid]=c 

def get_cate_level_by_id2(cateid):
  if cateid in x_id2cate:
    return x_id2cate[cateid].level
  return -1

read_goog_cate(fn_goog_cates)

for l in sys.stdin:
  l = l.strip()
  fs=l.split('\t')
  cate_id=fs[1]
  domain=fs[0]
  impr=fs[2]
  #print cate_id,domain,impr
  #print l
  if domain not in x:
    x[domain]=[]
  if cate_id != 'null':
    x[domain].append((cate_id,float(impr)))
    if cate_id in x_id2cate:
      c=x_id2cate[cate_id]
      #print 'this:',c.cid,c.name,impr
      #print 'fullpath:',c.allnodes,impr
      for p in c.allnodes:
        #print 'parent:',p[0],p[1],impr
        print domain+'\t'+'/'.join(str(node) for node in x_id2cate[p.cid].allnodes)+'\t'+impr
      #print


import sys

fn=sys.argv[1]

x_id2name={}
x_id2pid={}

with open(fn,'r') as f:
  for l in f:
    l=l.strip()
    cate,id,pid=l.rsplit(',',2)
    #print cate,id,pid
    x_id2name[id]=cate
    x_id2pid[id]=pid

for id in x_id2name:
  cate=x_id2name[id]
  if id in x_id2pid:
    l_path=[]
    pid=x_id2pid[id]
    while pid !='0':
      l_path.append(pid)
      if pid not in x_id2pid:
        break
      pid=x_id2pid[pid]
    
  l_name=[]
  for id2 in reversed(l_path):
    if id2 not in x_id2pid:continue
    l_name.append(id2+'--'+x_id2name[id2])
  l_name.append(id+'--'+cate)
  print '/'.join(l_name)
    #print l_levels



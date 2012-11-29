import sys

x_impr={}
x_click={}

for l in sys.stdin:
  l = l.strip()
  fs = l.split('\t',6)
  if len(fs)!=7:
    print 'ERROR:',len(fs),fs
  
  dom,campid,campname,cid,cname,impr,click=fs
  #print cate
  #print fs
  key=campid+'-'+campname
  #print 'key:',key
  if key not in x_impr:
    x_impr[key]={}
  if cname not in x_impr[key]:
    x_impr[key][cname]=0
  if key not in x_click:
    x_click[key]={}
  if cname not in x_click[key]:
    x_click[key][cname]=0
  #print x_impr
  x_impr[key][cname]+=float(impr)
  x_click[key][cname]+=float(click)

for camp in x_impr:
  for cate in x_impr[camp]:
    cnt_impr=x_impr[camp][cate]
    cnt_click=0.0
    if cate in x_click[camp]:
      cnt_click=x_click[camp][cate]
    print '\t'.join([camp,cate,str(cnt_impr),str(cnt_click),str(round(cnt_click/cnt_impr*100.0,4))+'%'])

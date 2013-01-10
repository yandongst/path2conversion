import sys
from operator import itemgetter

current_d=''

#set_d=set([])
x={}
ls=[]

def event_camp(a,b):
  try:
    sa = a[1]
    sb = b[1]
    date_delta=int(date_a) - int(date_b)
    #if date_delta==0:
      #return  int(event_a) - int(event_b)
    #else:
      #return int(date_a) - int(date_b)
    return date_delta
  except Exception as exp:
    sys.stderr.write(str(exp)+'\n')
    sys.stderr.write('ERR a:'+ a+'\n')
    sys.stderr.write('ERR b:'+ b+'\n')
  return 0

def proc(l):
  l=sorted(l, key=itemgetter(1), reverse=True)
  for c,w in l[:100]:
    print '\t'.join([current_d,c,str(w)])

for l in sys.stdin: 
  d,c,w=l.strip().split('\t')
  if current_d=='':current_d=d
  elif current_d!=d:
    #if d in set_d:
      #print 'ERROR:'+d
    proc(ls)
    ls=[]
    current_d=d
  else:
    ls.append((c,float(w)))
  #set_d.add(d)

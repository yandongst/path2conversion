import sys
import re

delimit=';'
delimit='-;,'

#sort first by date, then by event
def event_camp(a,b):
  date_delta=0
  try:
    date_a,event_a = a.split(',')[0:2]
    date_b,event_b = b.split(',')[0:2]
    date_delta=int(long(date_a) - long(date_b))
  except Exception as exp:
    sys.stderr.write(str(exp)+'\n')
    sys.stderr.write('ERR a:'+ a+'\n')
    sys.stderr.write('ERR b:'+ b+'\n\n')
  finally:
    return int(date_delta)
  #return int(0)


def filter_events(l):
  l2=[]
  for e in l:
    date_a=e.split(',')[0]
    try:
      if len(date_a)!=10:
        #print 'wrong date:',date_a
        continue
      l2.append(e)
    except Exception as exp:
      #sys.stderr.write('filtered out:'+str(exp)+'\n') 
      pass
  return l2

def sort_events(c,l):
  #print l
  l2=filter_events(l)
  try:
    l2.sort(event_camp)
  except Exception, ex:
    sys.stderr.write( 'to sort:'+str(l2)+'\n')
    sys.stderr.write( 'ex:'+str(ex)+'\n')
    sys.stderr.write( 'raise again\n')
    raise
  print '%s\t%s' %(c,delimit.join(l2))

current_c=''
ls_f=[]
for l in sys.stdin:
  #print l
  l = l.strip()
  c,r = l.split('\t')

  if current_c == '' and c!='':
    current_c = c

  if current_c != c: 
    try:
      sort_events(current_c,ls_f) 
    except Exception, ex:
      sys.stderr.write( '===-----==='.join(ls_f)+'\n')
      sys.stderr.write( str(ex)+'\n')
    current_c = c
    del ls_f[:]

  ls_f.extend(r.split(';'))

sort_events(current_c,ls_f);

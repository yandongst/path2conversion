import sys
import re

delimit=';'
delimit='-;,'

#sort first by date, then by event
def event_camp(a,b):
  try:
    date_a,event_a = a.split(',')[0:2]
    date_b,event_b = b.split(',')[0:2]
    date_delta=long(date_a) - long(date_b)
    #if date_delta==0:
      #return  int(event_a) - int(event_b)
    #else:
      #return int(date_a) - int(date_b)
    return int(date_delta)
  except Exception as exp:
    sys.stderr.write(str(exp)+'\n')
    sys.stderr.write('ERR a:'+ a+'\n')
    sys.stderr.write('ERR b:'+ b+'\n\n')
  return 0


def sort_events(c,l):
  #print l
  l.sort(event_camp)
  print '%s\t%s' %(c,delimit.join(l))

current_c=''
ls_f=[]
for l in sys.stdin:
  #print l
  l = l.strip()
  c,r = l.split('\t')

  if current_c == '' and c!='':
    current_c = c

  if current_c != c: 
    x_f = sort_events(current_c,ls_f) 
    current_c = c
    del ls_f[:]

  ls_f.extend(r.split(';'))

sort_events(current_c,ls_f);

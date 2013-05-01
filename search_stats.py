import sys
import re
import os
from datetime import datetime 
import time 

delimit='-;,'

keywords=set([])
for w in sys.argv[1:]:
  keywords.add(w.lower())
 
#print 'keywords:',keywords

for l in sys.stdin:
  l = l.strip()
  if len(l.split('\t'))!=2:continue
  c,r = l.split('\t')
  for event in r.split(delimit): 
    if len(event.split(',')) < 2:
      continue
      #print 'event:',event
    eventno = event.split(',')[1] 
    if eventno =='4':
      query= event.split(',') [5]
      #print c+'\t'+str(ticks)+','+event+','+channel+','+s_cate+','+kws+','+search_q+','+domain+','+location
      #print 'query:',query
      if set(query.lower().split(' ')) & keywords:
      #for q in query.split():
        #if q in keywords:
        for kws in event.split(',')[4].lower().split('-'):
          for kw in kws.split(' '):
            print kw
      #print query

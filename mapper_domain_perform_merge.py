import sys
import re
import os
from datetime import datetime 
import time 

for l in sys.stdin:
  l = l.strip()
  if len(l.split('\t'))!=2:continue
    #print >>sys.stderr,l
  c,r = l.split('\t')
  
  event = r.split(',')[0] 
  if event == '13' or event == '14':
    event,ticks,camp,campid,adgroupid,domain = r.split(',') 
    print '%s\t%s,%s,%s,%s,%s'%(c,ticks,event,camp,adgroupid,domain)

  elif event == '11' or event =='12':#currently there's no 12. conversion pixel has to be given
    rs =  r.split(',') 
    if len(rs) != 4:
      continue
    event,ts,name,camp = r.split(',') 
    st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    ticks= int(time.mktime(st.timetuple()))
    print '%s\t%d,11,%s'%(c,ticks,camp)
  else: 
    event,ts,data,s_cate,channel= r.split(',',4) 
    st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    ticks= int(time.mktime(st.timetuple()))
    print c+'\t'+str(ticks)+','+event+','+channel+','+s_cate

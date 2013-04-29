import sys
import re
import os
from datetime import datetime 
import time 

for l in sys.stdin:
  l = l.strip()
  if len(l.split('\t'))!=2:continue
  c,r = l.split('\t')
  
  event = r.split(',')[0] 
  if event == '13' or event == '14':
    event,ticks,camp,campid,adgroupid,domain = r.split(',') 
    print '%s\t%s,%s,%s,%s,%s'%(c,ticks,event,camp,adgroupid,domain)

  elif event == '11':
    rs =  r.split(',') 
    if len(rs) != 4:
      continue
    event,ts,name,camp = r.split(',') 
    st=None
    try:
      st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    except Exception,ex:
      continue
    ticks= int(time.mktime(st.timetuple()))
    print '%s\t%d,11,%s'%(c,ticks,camp)
  elif event =='4':
    event,ts,domain,s_cate,channel,kws,search_q,location= r.split(',',7) 
    st=None
    try:
      st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    except Exception,ex:
      continue
    ticks= int(time.mktime(st.timetuple()))
    print c+'\t'+str(ticks)+','+event+','+channel+','+s_cate+','+kws+','+search_q+','+domain+','+location
  else: 
    event,ts,domain,s_cate,channel,kws,search_q,location= r.split(',',7) 
    st=None
    try:
      st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    except Exception,ex:
      continue
    ticks= int(time.mktime(st.timetuple()))
    print c+'\t'+str(ticks)+','+event+','+channel+','+s_cate+','+kws+','+search_q+','+domain+','+location

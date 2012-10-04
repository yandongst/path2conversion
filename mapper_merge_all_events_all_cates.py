import sys
import re
import os
from datetime import datetime 
import time 


#target=set([])
#conv=set([])
#impr_pixel=set([])
#click_pixel=set([])
#cates=set([])

def read_pixels(fn):
  global target
  global conv
  global impr_pixel
  global click_pixel
  global cate
  for l in open(fn,'r'):
    l = l.rstrip()
    if l.startswith('#'):
      continue
    type,pixel = l.split(':')
    if type == 'retarg':
      target.add(pixel)
    elif type == 'conv':
      conv.add(pixel)
    elif type == 'impr':
      impr_pixel.add(pixel)
    elif type == 'click':
      click_pixel.add(pixel)
    elif type == 'cate':
      cates.add(pixel)
    else:
      sys.stderr.write('Error: unrecognized type:'+type)
      sys.exit(1)

#if len(sys.argv)<1:
#  sys.stderr.write('Not enough arguments!\n')
#  sys.exit(1)
#else:
#  read_pixels(sys.argv[1])

#sys.stderr.write(str(target)+'\t'+str(conv)+'\t'+str(impr_pixel)+'\t'+str(click_pixel)+'\t'+str(cates)+'\n')

#A063CA0A7F71E54DC914599802873F3A        20111009 23:06:25,socialoptimizationpixel,rt-yahoo_fantasy_football

for l in sys.stdin:
  l = l.strip()
  c,r = l.split('\t')
  #print len(r.split(','))
  
  event = r.split(',')[0] 
  #print event
  if event == '13' or event == '14':
    #048AA00A022AD24EC53E553302D47BAA        13,1331660652,thedoghousediaries.com
    event,ticks,camp,campid,adgroupid = r.split(',') 
    #if event =='13' and camp in impr_pixel:
    #if event =='13' or event =='14':
    print '%s\t%s,%s,%s,%s'%(c,ticks,event,camp,adgroupid)
    #if event =='14' and camp in click_pixel:

  elif event == '11':
    rs =  r.split(',') 
    if len(rs) != 4:
      continue
    event,ts,name,camp = r.split(',') 
    st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    ticks= int(time.mktime(st.timetuple()))
    #if camp in target:
    print '%s\t%d,11,%s'%(c,ticks,camp)
    #elif camp in conv:
    #print '%s\t%d,12'%(c,ticks)
  elif event =='4':
    event,ts,domain,s_cate,channel= r.split(',',4) 
    st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    ticks= int(time.mktime(st.timetuple()))
    #print c+'\t'+str(ticks)+','+event+','+query
    #if not cates:
    print c+'\t'+str(ticks)+','+event+','+channel+','+s_cate
    #else:
    #  toprint=False
    #  for c1 in s_cate.split('-'):
    #    if c1 in cates: 
          #sys.stderr.write( c)
    #      toprint=True
    #      break
    #  if toprint:
    #    print c+'\t'+str(ticks)+','+event
  else: 
    #if len(r.split(','))!=3:
      #print l
    event,ts,data,s_cate,channel= r.split(',',4) 
    st = datetime.strptime(ts, "%Y%m%d %H:%M:%S")
    ticks= int(time.mktime(st.timetuple()))
    #print c+'\t'+str(ticks)+','+event+','+data
    #if not cates:
    print c+'\t'+str(ticks)+','+event+','+channel+','+s_cate
    #else:
    #  toprint=False
    #  for c1 in s_cate.split('-'):
    #    if c1 in cates: 
          #sys.stderr.write( c)
    #      toprint=True
    #      break
    #  if toprint:
    #    print c+'\t'+str(ticks)+','+event
    #sys.stderr.write('Error:'+l+'\n')
    #sys.exit(1) 

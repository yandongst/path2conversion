import sys

delimit='-;,'

s_retarg=set([])#11
s_conv=set([])#11
s_impr_pixel=set([])#13
s_click_pixel=set([])#14
s_cates=set([])
s_adgroups=set([])
start_date=''
end_date=''
def read_pixels(fn):
  global s_retarg
  global s_conv
  global s_impr_pixel
  global s_click_pixel
  global s_cate
  global s_adgroups
  for l in open(fn,'r'):
    l = l.rstrip()
    if l.startswith('#'):
      continue
    type,pixel = l.split(':')
    if type == 'retarg':
      s_retarg.add(pixel)
    elif type == 'conv':
      s_conv.add(pixel)
    elif type == 'impr':
      s_impr_pixel.add(pixel)
    elif type == 'click':
      s_click_pixel.add(pixel)
    elif type == 'cate':
      s_cates.add(pixel)
    elif type == 'adgroup':
      s_adgroups.add(pixel)
    else:
      sys.stderr.write('Error: unrecognized type:'+type)
      sys.exit(1)
  #sys.stderr.write(str(s_impr_pixel)+'\n')
  #sys.stderr.write(str(s_click_pixel)+'\n')

attrs=[]

read_pixels(sys.argv[1])

def print_events(l_events):
  l=[]
  for event,ts in l_events:
    l.append(ts+','+event)
  sys.stdout.write(delimit.join(l))
  print

def add_event_impr(l_events,l_impr_pixels, start_s, end_s):
  str='__'.join(l_impr_pixels)  
  if start_s != end_s:
    l_events.append(','.join([start_s,'13',str]))
    l_events.append(','.join([end_s,'13',str]))
  else:
    l_events.append(','.join([start_s,'13',str]))

#ts,event,attrs
#13343434343,13,jcp__disney

def add_event(l_events,event1, l_impr_pixels,start_s, end_s):
  if start_s != end_s:
    l_events.append(start_s)
    l_events.append(end_s)
  else:
    l_events.append((event,start_s))

def filter_events(events): 
  l_events=[]
  has_ad=False
  for ev in events:
    fields=ev.split(',')
    if len(fields)<2:continue
    event=fields[1]
    
    if event in ['1','2','3','4']:
      cates = set(fields[3].split('-'))
      #print 'overlap:',cates & s_cates
      if s_cates:
        if cates & s_cates:
          l_events.append(ev);
      else:
        l_events.append(ev);
    elif event=='13':#impr
      if fields[2] in s_impr_pixel:
        has_ad=True
        l_events.append(ev);
    elif event=='14':#click
      if fields[2] in s_click_pixel:
        l_events.append(ev);
    elif event=='11':
      if fields[2] in s_retarg or fields[2] in s_conv:
        l_events.append(ev);
    else:
      print '---whats this---',ev
  if has_ad: return l_events 
  else: return []


def collapse(events):
  #for l in sys.stdin:
    #l = l.strip()
    #c,r = l.split('\t')
    current_event = None
    start_ts = 0
    end_ts = 0
    #if len(r.split(delimit)) == 1:
    if len(events)==1:
      return events
    #print 'org:'+l
    #print
    l_events=[]
    #for rr in r.split(delimit):
    l_impr_pixels=[]
    for rr in events:
      try:
        rrr=rr.split(',')
        date=rrr[0]
        event=rrr[1]
        if current_event == None:
          current_event = event
          start_ts = date
          end_ts = date
          #not_finished=True
        elif event == current_event:#keep updating ending event
          #for impr, combine them with all pixels added as attrs
          if event=='13':
            l_impr_pixels.append(rrr[2])
          end_ts = date
          #not_finished=True
      
        elif event != current_event:
          #print_event(current_event, start_ts,end_ts)
          if event=='13':
            l_impr_pixels=[]

          if current_event=='13':
            add_event_impr(l_events,l_impr_pixels,start_ts,end_ts)
          else:
            add_event(l_events,rr, start_ts,end_ts)
          start_ts = date
          end_ts = date
          current_event = event
          #not_finished=True

      #if not_finished:
      
      except Exception,ex:
        sys.stderr.write(l+'\n'+str(ex)+'\n')
        sys.stderr.write(rr+'\n')
        sys.stderr.write( '---Error:'+rr+'\n') 

    #print_event(current_event, start_ts,end_ts)
    add_event(l_events,current_event, start_ts,end_ts)
    #print_events(l_events)
    return l_events


for l in sys.stdin:
  l = l.strip()
  c,r = l.split('\t')
  has_ad=False
  has_social=False 
  campaigns1=set([])
  adgroups1=set([])
  channels1=set([])
  #multiple adgrousp, campaign. use list here
  events=r.split(delimit)
  f_events=filter_events(events)
  #c_events=collapse(f_events)
 
  for rr in f_events:
    rrr=rr.split(',')
    event=rrr[1]

    cur_channel=''
    str_CAMP='no_CAMP'
    if has_ad:
      str_CAMP='CAMP'
    str_SOCIAL='no_SO'
    if has_social:
      str_SOCIAL='SOCIAL'
    if event=='1' or event=='2':
      cur_channel=rrr[2]

    campaigns=set([])
    campaigns.update(campaigns1)
    campaigns.add(str_CAMP)
    adgroups=set([])
    adgroups.update(adgroups1)
    channels=set([])
    channels.update(channels1)
    channels.add(str_SOCIAL)

    #print campaigns
    #print channels

    event_list=['1','2','3','4','11']
    events_output=[event]
    if event in ['1','2']: 
        events_output.append(event+'-'+cur_channel) 


    if event in event_list:
      pass
      #CAMP/SOCIAL level
      #for channel in channels:
        #print delimit.join([event,str_CAMP,channel])+'\t1'
        #if event in ['1','2']: 
          #print delimit.join([event+'-'+channel,str_CAMP,channel])+'\t1'

      #for camp in campaigns:
        #print delimit.join([event,camp,str_SOCIAL])+'\t1'

      #RTB/channel level
      for camp in campaigns:
        for channel in channels:
          for eo in events_output:
            if eo=='11' and rrr[2] in s_retarg:
              print delimit.join(['11',camp,channel])+'\t1'
            elif eo=='11' and rrr[2] in s_conv:
              print delimit.join(['12',camp,channel])+'\t1' 
            else:
              print delimit.join([eo,camp,channel])+'\t1'
          #if event in ['1','2']: 
            #print delimit.join([event+'-'+channel,str_CAMP,channel])+'\t1'
      #print


      
      #print delimit.join([event,str_ad,str_social])+'\t1'
    #retarging
    elif event=='11' and rrr[2] in s_retarg:
      pass
      #print delimit.join([event,str_ad,str_social])+'\t1'
    elif event=='11' and rrr[2] in s_conv:
      #print delimit.join(['12',str_ad,str_social])+'\t1'
      pass

    #impression
    if event=='13':
      has_ad=True
      campaigns1.add('r.'+rrr[2])
      adgroups1.add('a.'+rrr[3])
    #social
    elif event=='1' or event=='2':
      has_social=True
      channels1.add('c.'+rrr[2]) 

import sys

def filter_events(events): 
  l_events=[]
  has_ad=False
  s_adg=set([])
  for ev in events:
    fields=ev.split(',')
    if len(fields)<2:continue
    event=fields[1]
    
    if event in ['1','2','3','4']:
      try:
        cates = set(fields[3].split('-'))
        if len(s_cates)>0:
          if cates & s_cates:
            l_events.append(ev);
          else:
            pass
            #print len(s_cates)
            #print >>sys.stdout,'>> didnt add because of cate.',ev
        else:
          l_events.append(ev);
      except Exception, ex:
        print >>sys.stderr,'ERROR:',ev
        continue
        #raise
    elif event=='13':#impr
      if fields[2] in s_impr_pixel:
        has_ad=True
        l_events.append(ev);
        s_adg.add(fields[3])
    elif event=='14':#click
      if fields[2] in s_click_pixel:
        l_events.append(ev);
    elif event=='11':
      if fields[2] in s_retarg or fields[2] in s_conv:
        l_events.append(ev);
    else:
      #print '---whats this---',ev
      pass
  if has_ad: return l_events,s_adg 
  else: return [],[]

delimit='-;,'
s_retarg=set([])#11
s_conv=set([])#11
s_impr_pixel=set([])#13
s_click_pixel=set([])#14
s_cates=set([])
s_adgroups=set([])

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

read_pixels(sys.argv[1])

#print s_impr_pixel

for l in sys.stdin:
  l = l.strip()
  c,r = l.split('\t')
  events=r.split(delimit)
  f_events,s_adg=filter_events(events)
  if f_events:
    #print events
    #print f_events
    #print s_adg
    pass

  has_ad=False 
  for rr in f_events:
    if has_ad:
      str_ad='CAMP'
    else:
      str_ad='no_CAMP'
    rrr=rr.split(',')
    event=rrr[1]
    
    #if event != '13' and event != '14':
    events_output=[event]
    events_not_output=set(['13','14'])
    if event in ['1','2']: 
      cur_channel=rrr[2]
      events_output.append(event+'-'+cur_channel) 
    for eo in events_output:
      if eo in events_not_output:continue
      if eo=='11' and rrr[2] in s_retarg:
        print delimit.join(['11',str_ad])+'\t1'
      elif eo=='11' and rrr[2] in s_conv:
        print delimit.join(['12',str_ad])+'\t1' 
      else:
        print delimit.join([eo,str_ad])+'\t1'

    if event=='13':
      has_ad=True 

  #for each adgroup
  # loop thru event
  for adg in s_adg:
    has_adg=False 
    str_adg=''
    cur_channel=''
    for rr in f_events:
      if has_adg:
        str_adg='a.'+adg
      else:
        str_adg='no_a.'+adg
      rrr=rr.split(',')
      event=rrr[1]
      
      events_output=[]
      #if event != '13' and event != '14':
      events_output=[event]
      events_not_output=set(['13','14'])
      if event in ['1','2']: 
        cur_channel=rrr[2]
        events_output.append(event+'-'+cur_channel) 
      for eo in events_output:
        if eo in events_not_output:continue
        if eo=='11' and rrr[2] in s_retarg:
          print delimit.join(['11',str_adg])+'\t1'
        elif eo=='11' and rrr[2] in s_conv:
          print delimit.join(['12',str_adg])+'\t1' 
        else:
          print delimit.join([eo,str_adg])+'\t1'

      if event=='13' and rrr[3]==adg:
        has_adg=True 

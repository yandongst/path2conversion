import sys

x_channel={}
x_adgroup={}
x_adg_ch={}
x_overall={} 
x_label={'1':'Share','2':'Click','3':'PageView','4':'Search','11':'Retargeting'}

for l in sys.stdin:
  l =l.strip()
  #print 'l:',l
  ev,lift,after,before,level=l.split(' ')
  #if float(after)+float(before)<50.0:continue
  #print ev,lift,after,before,level
  #output 3 lines
  #  before
  #  after
  #  lift
  if '-' in ev:
    ev_no,ev_channel=ev.split('-')
    if ev_no not in x_channel:
      x_channel[ev_no]={}
    #x_channel[ev_no][ev_channel]=(before,after,lift)
    x_channel[ev_no][ev_channel]=(before,after,lift)
    # x[adgroup][event_no][channel]
    if level not in x_adg_ch:
      x_adg_ch[level]={}
    if ev_no not in x_adg_ch[level]:
      x_adg_ch[level][ev_no]={}
    x_adg_ch[level][ev_no][ev_channel]=(before,after,lift)
  else:
    x_overall[ev]=(before,after,lift)
    if level not in x_adgroup:
      x_adgroup[level]={}
    x_adgroup[level][ev]=(before,after,lift)

#print x_channel
for ev_no in x_channel:
  print 'Adlift for ',x_label[ev_no]
  channel_list = x_channel[ev_no].keys()
  #c_list=[x_label[x] for x in channel_list]
  #print channel_list
  l_b=[]
  l_a=[]
  l_l=[]
  for ch in channel_list:
    l_b.append(x_channel[ev_no][ch][0])
    l_a.append(x_channel[ev_no][ch][1])
    if x_channel[ev_no][ch][2]=='N/A':
      l_l.append('0.0%')
    else:
      l_l.append(x_channel[ev_no][ch][2])
  print 'Channel,',','.join(channel_list)
  print 'Before,',','.join(l_b)
  print 'After,',','.join(l_a)
  print 'Lift,',','.join(l_l)
  print

print '-'*50

for adg in x_adg_ch:
  for ev_no in x_adg_ch[adg]:
    print 'Adlift for adgroup:',adg,'event:',x_label[ev_no]
    channel_list = x_adg_ch[adg][ev_no].keys()
    #c_list=[x_label[x] for x in channel_list]
    #print channel_list
    l_b=[]
    l_a=[]
    l_l=[]
    for ch in channel_list:
      l_b.append(x_adg_ch[adg][ev_no][ch][0])
      l_a.append(x_adg_ch[adg][ev_no][ch][1])
      if x_adg_ch[adg][ev_no][ch][2]=='N/A':
        l_l.append('0.0%')
      else:
        l_l.append(x_adg_ch[adg][ev_no][ch][2])
    print 'Channel,',','.join(channel_list)
    print 'Before,',','.join(l_b)
    print 'After,',','.join(l_a)
    print 'Lift,',','.join(l_l)
    print

  print
print '-'*50

#print x_adgroup
for adg in x_adgroup:
  print 'Adlift for ',adg
  channel_list = x_adgroup[adg].keys()
  c_list=[x_label[x] for x in channel_list]
  l_b=[]
  l_a=[]
  l_l=[]
  for ch in channel_list:
    l_b.append(x_adgroup[adg][ch][0])
    l_a.append(x_adgroup[adg][ch][1])
    if x_adgroup[adg][ch][2]=='N/A':
      l_l.append('0.0%')
    else:
      l_l.append(x_adgroup[adg][ch][2])
  print 'Channel,',','.join(c_list)
  print 'Before,',','.join(l_b)
  print 'After,',','.join(l_a)
  print 'Lift,',','.join(l_l)
  print

print '-'*50

#print x_overall
#print 'Adlift for all'
#l_b=[]
#l_a=[]
#l_l=[]
#channel_list = x_overall.keys()
#for ev_no in x_overall:
  #l_b.append(x_overall[ev_no][0])
  #l_a.append(x_overall[ev_no][1])
  #if x_overall[ev_no][2]=='N/A':
    #l_l.append('0.0%')
  #else:
    #l_l.append(x_overall[ev_no][2])
#print 'Channel,',','.join(channel_list)
#print 'Before,',','.join(l_b)
#print 'After,',','.join(l_a)
#print 'Lift,',','.join(l_l)
    

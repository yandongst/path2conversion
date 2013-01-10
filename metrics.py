#this is an old version. this computes social lift which makes things nasty
#user metrics2.py

import sys

delimit='-;,'
#key_list=['ad','no_ad','so','no_so']
l_event=set()
l_channels=set([])
l_campaigns=set([])
l_adgroups=set([])
cnt={}

# product of
# (no_)CAMP,RTB(s), ADGROUP(s)
#   and 
# (no_)SOCIAL, channel(s)
#


for l in sys.stdin: 
  l = l.strip()
  k,v=l.split('\t')
  #adlift-3 = ((#3-ad) - (#3-no_ad))/(#2-no_ad)
  kk=k.split(delimit)
  l_event.add(kk[0])
  for vv in kk:
    if vv.startswith('r.'):
      l_campaigns.add(vv)
    elif vv.startswith('c.'):
      l_channels.add(vv)
    elif vv.startswith('a.'):
      l_adgroups.add(vv)
  cnt[k]=float(v)

#print l_event
#print l_campaigns
#print l_adgroups
#print l_channels

#for k in cnt:
  #print k,cnt[k]

ll_camp=[]
ll_camp.append('CAMP')
ll_camp.extend(l_campaigns)
ll_camp.extend(l_adgroups)
ll_social=[]
ll_social.append('SOCIAL')
ll_social.extend(l_channels)

for e in l_event:
  k_ad_so=delimit.join([e,'CAMP','SOCIAL'])
  k_ad_noso=delimit.join([e,'CAMP','no_SO'])
  k_noad_so=delimit.join([e,'no_CAMP','SOCIAL'])
  k_noad_noso=delimit.join([e,'no_CAMP','no_SO'])
  c_ad_so=0
  c_ad_noso=0
  c_noad_so=0
  c_noad_noso=0
  if k_ad_so in cnt:
    c_ad_so=cnt[k_ad_so]
    #print c_ad_so
  if k_ad_noso in cnt:
    c_ad_noso=cnt[k_ad_noso]
    #print c_ad_noso
  if k_noad_so in cnt:
    c_noad_so=cnt[k_noad_so]
    #print c_noad_so
  if k_noad_noso in cnt:
    c_noad_noso=cnt[k_noad_noso]
    #print c_noad_noso
  cnt_ad=float(c_ad_so+c_ad_noso)
  cnt_noad=float(c_noad_so+c_noad_noso)
  if cnt_noad==0:
    print e,'N/A',cnt_ad,cnt_noad,'Adlift'
  else:
    adlift=(cnt_ad-cnt_noad)/cnt_noad
    print e,str(round(adlift,2)*100.0)+'%',cnt_ad,cnt_noad,'Adlift'


for e in l_event:
  k_ad_so=delimit.join([e,'CAMP','SOCIAL'])
  k_ad_noso=delimit.join([e,'CAMP','no_SO'])
  k_noad_so=delimit.join([e,'no_CAMP','SOCIAL'])
  k_noad_noso=delimit.join([e,'no_CAMP','no_SO'])
  c_ad_so=0
  c_ad_noso=0
  c_noad_so=0
  c_noad_noso=0
  if k_ad_so in cnt:
    c_ad_so=cnt[k_ad_so]
    #print c_ad_so
  if k_ad_noso in cnt:
    c_ad_noso=cnt[k_ad_noso]
    #print c_ad_noso
  if k_noad_so in cnt:
    c_noad_so=cnt[k_noad_so]
    #print c_noad_so
  if k_noad_noso in cnt:
    c_noad_noso=cnt[k_noad_noso]
    #print c_noad_noso
  cnt_so=float(c_ad_so+c_noad_so)
  cnt_noso=float(c_ad_noso+c_noad_noso)
  if cnt_noso==0:
    print e,'N/A',cnt_so,cnt_noso,'Solift'
  else:
    adlift=(cnt_so-cnt_noso)/cnt_noso
    print e,str(round(adlift,2)*100.0)+'%',cnt_so,cnt_noso,'Solift'


for e in l_event:
  for adg in l_adgroups:
    k_ad_so=delimit.join([e,adg,'SOCIAL'])
    k_ad_noso=delimit.join([e,adg,'no_SO'])
    k_noad_so=delimit.join([e,'no_CAMP','SOCIAL'])
    k_noad_noso=delimit.join([e,'no_CAMP','no_SO'])
    c_ad_so=0
    c_ad_noso=0
    c_noad_so=0
    c_noad_noso=0
    if k_ad_so in cnt: c_ad_so=cnt[k_ad_so]
    if k_ad_noso in cnt: c_ad_noso=cnt[k_ad_noso]
    if k_noad_so in cnt: c_noad_so=cnt[k_noad_so]
    if k_noad_noso in cnt: c_noad_noso=cnt[k_noad_noso]
    cnt_ad=float(c_ad_so+c_ad_noso)
    cnt_noad=float(c_noad_so+c_noad_noso)
    if cnt_noad==0:
      print e,'N/A',cnt_ad,cnt_noad,'Adlift-adgroup',adg
    else:
      adlift=(cnt_ad-cnt_noad)/cnt_noad
      print e,str(round(adlift,2)*100.0)+'%',cnt_ad,cnt_noad,'Adlift-adgroup',adg

for e in l_event:
  for camp in ll_camp:
    for soci in ll_social:
      k_ad_so=delimit.join([e,camp,soci])
      k_ad_noso=delimit.join([e,camp,'no_SO'])
      k_noad_so=delimit.join([e,'no_CAMP',soci])
      k_noad_noso=delimit.join([e,'no_CAMP','no_SO'])
      c_ad_so=0
      c_ad_noso=0
      c_noad_so=0
      c_noad_noso=0
      if k_ad_so in cnt: c_ad_so=cnt[k_ad_so]
      if k_ad_noso in cnt: c_ad_noso=cnt[k_ad_noso]
      if k_noad_so in cnt: c_noad_so=cnt[k_noad_so]
      if k_noad_noso in cnt: c_noad_noso=cnt[k_noad_noso]
      cnt_ad=float(c_ad_so+c_ad_noso)
      cnt_noad=float(c_noad_so+c_noad_noso)
      if cnt_noad==0:
        print e,'N/A',cnt_ad,cnt_noad,'Adlift',camp,soci
      else:
        adlift=(cnt_ad-cnt_noad)/cnt_noad
        print e,str(round(adlift,2)*100.0)+'%',cnt_ad,cnt_noad,'Adlift',camp,soci

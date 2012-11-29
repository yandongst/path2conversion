import sys 

for l in sys.stdin:
  l = l.strip()
  fs = l.split('\t')
  if len(fs)==8:#delivery
    dom=fs[0].lower()
    campid=fs[1]
    impr=fs[2]
    click=fs[3]
    key=dom+'--'+campid
    print '\t'.join([key,'impr',impr])
    print '\t'.join([key,'click',click])
  if len(fs)==2:#perform
    campid,dom,typ=fs[0].split('--')
    cnt=fs[1]
    dom=dom.lower()
    key=dom+'--'+campid
    print '\t'.join([key,typ,cnt]) 
  else:
    pass
    #print 'ERROR:',l

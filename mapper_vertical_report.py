import sys

for l in sys.stdin:
  l =l.strip()
  campid,campname,domain, cates,imp,clk,ctr,ctr1,vtr,ctc,vtc=l.split('\t')
  print '\t'.join([campid,campname,cates,imp,clk,ctr1,vtr,ctc,vtc])

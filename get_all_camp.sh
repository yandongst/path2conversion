hadoop fs -text /projects/input/adlogs/normalized_rtb_adlog/impr/201212*/valid*/p*|cut -f1|sort -T tmp|uniq -c > 201212_camp.txt
#htext /projects/input/adlogs/normalized_rtb_adlog/click/2012090?/valid*/p*|cut -f1|sort|uniq -c > 0901_0909_click.txt

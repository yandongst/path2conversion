logtype=normalized_rtb_adlog

destdir=/projects/input/adlogs/normalized_rtb_adlog
for event in impr click
do
for (( d=1; d <= 31; d++ ))
do
  printf -v date "201209%02i" $d
  echo hadoop distcp 184.73.100.20/user/root/adlog_analytics/$logtype/$event/$date $destdir/$event/$date
  #hadoop distcp -conf /root/account/insight-site.xml hdfs://184.73.100.20:8020/user/root/adlog_analytics/$logtype/$event/$date /tmp
  hadoop distcp hftp://184.73.100.20:50070/user/root/adlog_analytics/$logtype/$event/$date $destdir/$event/$date
done
done

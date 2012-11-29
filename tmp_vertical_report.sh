for (( d=1; d <= 14; d++ ))
do
  printf -v date "201210%02i" $d
  #hadoop fs -text /projects/input/ctrlogs/net_camp_daily/${date}/part-*|python join_ctrlogs_googcates.py 1022_domain2cate_all.csv camp2name.csv |python mapper_domainctr.py > vertical_report_${date}.txt
  hadoop fs -text /projects/input/ctrlogs/net_camp_daily/${date}/part-*|python join_ctrlogs_googcates.py 1022_domain2cate_topcate.csv camp2name.csv |python mapper_domainctr.py > vertical_report_${date}_top.txt
done

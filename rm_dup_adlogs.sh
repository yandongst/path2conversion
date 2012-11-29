dir=/projects/input/adlogs/normalized_rtb_adlog/impr

for (( d=1; d <= 31; d++ ))
do
  printf -v date "201209%02i" $d
  echo hadoop fs -rmr $dir/$date/$date
  hadoop fs -rmr $dir/$date/$date
done

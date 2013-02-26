year=2012
m1=12
d1=4
m2=12
d2=16


set mapred.job.queue.name=p1;

dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo ${dates}

fn=clorox_pixels.txt
./mapred_adlift_combination_count.sh /projects/output/merged/userevents_adlogs_retarg/${timeperiod} /projects/output/merged/userevents_adlogs_retarg_cnt/${timeperiod}/ $fn
hadoop fs -text /projects/output/merged/userevents_adlogs_retarg_cnt/${timeperiod}/$fn/part-0000*.snappy|python metrics_adlift.py > tmp.txt
echo output to tmp.txt


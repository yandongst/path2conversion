year=2012
m1=12
d1=17
m2=12
d2=17

dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo ${dates}
#./event_end_A.sh ${dates}
#./mapred_classify_to_events.sh /projects/output/merged/merged_logs/sampleA-${timeperiod} /projects/output/merged/merged_logs_classified/sampleA-${timeperiod}

#below is a nonsampling version
echo ./mapred_classify_to_events_nosample.sh ${dates}  /projects/output/merged/merged_logs_classified/${timeperiod}
./mapred_classify_to_events_nosample.sh ${dates}  /projects/output/merged/merged_logs_classified/${timeperiod}

./cp_adlogs.sh ${dates}
./cp_retarg.sh ${dates}
./mapred_format_adlogs_nosample.sh ${dates}
./mapred_retarg_nosample.sh ${dates}
./mapred_merge_all_events_w_cates_nosample.sh ${dates}
fn=toyota_conv_pixels.txt
fn=honda_winter_pixels.txt
fn=bestbuy_pixels.txt
fn=msft_pixels.txt
fn=merrill_pixels.txt
./mapred_adlift_combination_count.sh /projects/output/merged/userevents_adlogs_retarg/${timeperiod}_endA /projects/output/merged/userevents_adlogs_retarg_cnt/${timeperiod}_endA/ $fn
hadoop fs -text /projects/output/merged/userevents_adlogs_retarg_cnt/${timeperiod}_endA/$fn/part-0000*.gz|python metrics_adlift.py > tmp.txt
echo output to tmp.txt


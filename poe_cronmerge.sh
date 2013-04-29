year=`date --date='-7 day'  +%Y|sed 's/^0*//'`
m1=`date  --date='-7 day' +%m|sed 's/^0*//'`
d1=`date  --date='-7 day' +%d|sed 's/^0*//'`
m2=`date  --date='-1 day' +%m|sed 's/^0*//'`
d2=`date  --date='-1 day' +%d|sed 's/^0*//'`

dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo $dates
echo $timeperiod
dir="/home/yandong/workspace/path"
diruct="/home/yandong/workspace/uct"

echo =====================================
echo mapred_classify_to_events_nosample
echo ===================================== 
$dir/./mapred_classify_to_events_nosample.sh ${dates}  /projects/science/output/merged/merged_logs_classified/${timeperiod} 
echo =====================================
echo uct merge
echo ===================================== 
$diruct/mapred_camp_stats.sh ${dates}  
echo =====================================
echo cp_adlogs
echo ===================================== 
$dir/./cp_adlogs.sh ${dates}
$dir/./cp_retarg.sh ${dates}
$dir/./mapred_format_adlogs_nosample.sh ${dates}
$dir/./mapred_retarg_nosample.sh ${dates}
$dir/./mapred_merge_all_events_w_cates_nosample.sh ${dates}

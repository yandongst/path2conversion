year=$1
m1=$2
d1=$3
m2=$4
d2=$5

dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo ${dates}
./mapred_classify_to_events_nosample.sh ${dates}  /projects/science/output/merged/merged_logs_classified/${timeperiod} 
./cp_adlogs.sh ${dates}
./cp_retarg.sh ${dates}
./mapred_format_adlogs_nosample.sh ${dates}
./mapred_retarg_nosample.sh ${dates}
./mapred_merge_all_events_w_cates_nosample.sh ${dates}


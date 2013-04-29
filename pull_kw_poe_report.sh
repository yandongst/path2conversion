year=$1
m1=$2
d1=$3
m2=$4
d2=$5 


dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo ${dates}

fn=$6
fn_output=$7
./mapred_adlift_combination_kw_count.sh /projects/science/output/merged/userevents_adlogs_retarg/${timeperiod} /projects/science/output/merged/userevents_adlogs_retarg_cnt/keyword/${timeperiod}/ $fn
echo hadoop fs -text /projects/science/output/merged/userevents_adlogs_retarg_cnt/keyword/${timeperiod}/${fn}/part-0000*.gz\|python metrics_adlift.py \> ${fn_output}
hadoop fs -text /projects/science/output/merged/userevents_adlogs_retarg_cnt/keyword/${timeperiod}/${fn}/part-0000*.gz|python metrics_adlift.py > ${fn_output}
echo output to $fn_output


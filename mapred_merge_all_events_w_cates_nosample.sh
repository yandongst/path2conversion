
hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
input_op=''

if [ $# -ne 5 ]
then
  echo 'not enough parameters'
  exit 1
fi

year=$1
m1=$2
d1=$3
m2=$4
d2=$5
dir="/home/yandong/workspace/path"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

input_op+="-input /projects/science/output/merged/merged_logs_classified/${timeperiod} "
input_op+="-input /projects/science/output/merged/adlogs/${timeperiod} "
input_op+="-input /projects/science/output/merged/retarg/${timeperiod} "


OUTDIR=/projects/science/output/merged/userevents_adlogs_retarg/${timeperiod}

mapper_opt="python mapper_merge_all_events_all_cates.py"

echo mapper_opt: $mapper_opt


echo $hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file mapper_merge_all_events_all_cates.py -reducer "python reducer.py"  -file /data/4/yandong/reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.job.name='poe_merge'
$hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $dir/mapper_merge_all_events_all_cates.py -reducer "python reducer.py"  -file $dir/reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='poe_merge' -jobconf mapred.job.queue.name=science

hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'

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

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

#input_op+="-input /projects/output/merged/merged_logs_classified/sampleA-${timeperiod}-w-kws "
input_op+="-input /projects/output/merged/merged_logs_classified/sampleA-${timeperiod} "
input_op+="-input /projects/output/merged/adlogs/${timeperiod}-endingA "
input_op+="-input /projects/output/merged/retarg/${timeperiod}-endA "

#echo $input_op

#target=rt-disney
#conv=rt-disney_conversion
#cate=travel_automotive_business_employment.txt
#cate=hertz_all_cates.txt

#target=rt-victorias_secret
#conv=rt-victorias_secret_confirmation
#cate=shopping_clothing



OUTDIR=/projects/output/merged/userevents_adlogs_retarg/${timeperiod}_endA
#OUTDIR=/projects/output/merged/userevents_adlogs_retarg/${timeperiod}_endA-w-kws

mapper_opt="python mapper_merge_all_events_all_cates.py"

echo mapper_opt: $mapper_opt


echo $hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file mapper_merge_all_events_all_cates.py -reducer "python reducer.py"  -file /data/4/yandong/reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.job.name='conv_path'
#$hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file mapper_merge_all_events_all_cates.py -reducer "python reducer.py"  -file /data/4/yandong/reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='conv_path'
$hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file mapper_merge_all_events_all_cates.py -reducer "python reducer.py"  -file reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='conv_path'

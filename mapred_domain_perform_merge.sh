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

input_op+="-input /projects/output/merged/adlogs/${timeperiod} "
input_op+="-input /projects/output/merged/retarg/${timeperiod}" 

OUTDIR=/projects/output/merged/adlogs_retarg/${timeperiod}

mapper_fn="mapper_domain_perform_merge.py" 
mapper_opt="python $mapper_fn"


echo $hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $mapper_fn -reducer "python reducer.py"  -file /data/4/yandong/reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.job.name='adlogs_retarg_merge'
$hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $mapper_fn -reducer "python reducer.py"  -file reducer.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='adlogs_retarg_merge'

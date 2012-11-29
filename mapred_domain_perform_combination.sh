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

input_op+="-input /projects/output/merged/adlogs_retarg/${timeperiod}"

OUTDIR=/projects/output/merged/adlogs_retarg_combination/${timeperiod}

fn_pixel=pixel_test.txt
mapper_fn="mapper_domain_perform_combination.py" 
mapper_opt="python $mapper_fn $fn_pixel"



echo $hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $mapper_fn -file $fn_pixel -reducer "python reducer_count.py"  -file /data/4/yandong/reducer_count.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.job.name='domain_perform_combination'
$hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $mapper_fn -file $fn_pixel -reducer "python reducer_count.py"  -file /data/4/yandong/reducer_count.py -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='domain_perform_combination'

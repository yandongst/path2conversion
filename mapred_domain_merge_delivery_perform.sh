hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'

input_op=''

#if [ $# -ne 5 ]
#then
  #echo 'not enough parameters'
  #exit 1
#fi

#year=$1
#m1=$2
#d1=$3
#m2=$4
#d2=$5

#printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

##TEST ONLY. TIME PERIODS ARE NOT THE SAME##

input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121001/ "
input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121002/ "
input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121003/ "
input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121004/ "
input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121005/ "
input_op+="-input /projects/output/merged/adlogs_retarg_combination/20121101-20121110/ "

OUTDIR="/projects/output/merged/domain_delivery_perform/20111001-20111005"

fn_pixel=pixel_test.txt
mapper_fn="mapper_domain_merge_delivery_perform.py" 
mapper_opt="python $mapper_fn"
reducer_fn="reducer_domain_merge_delivery_perform.py" 
reducer_opt="python $reducer_fn"



echo $hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $mapper_fn -reducer "$reducer_opt"  -file $reducer_fn -jobconf mapred.reduce.tasks=500 -jobconf mapred.job.name='domain_deivery_perform_merge'
$hstream  $input_op -output ${OUTDIR} -mapper "$mapper_opt" -file $mapper_fn -reducer "$reducer_opt"  -file $reducer_fn -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='domain_deivery_perform_merge'

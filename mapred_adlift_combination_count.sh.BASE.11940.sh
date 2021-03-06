## product count of event-camp or event-social for lift calculation 
##
##
##

hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

#fn=volvo_pixels.txt
fn=$3

#OUTDIR=/projects/output/merged/userevents_adlogs_retarg_cnt/20120923-20121006_endA/$fn
OUTDIR=$2/$fn

#input_op=/user/root/yandong/01_05_01_10_preprocess_logs_end_A/
input_op=/projects/output/merged/userevents_adlogs_retarg/20120923-20121006_endA
input_op_pre=''
input_op_post=''

input_op="-input ${input_op} "
input_op="-input $1 "


 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count.py $fn" -file mapper_count.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count2.py $fn" -file mapper_count2.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2

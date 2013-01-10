hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

OUTDIR=$2

input_op=$1

#OUTDIR=/projects/output/merged/merged_logs_classified/sampleA-20121111-20121112

#input_op=/user/root/yandong/01_05_01_10_preprocess_logs_end_A/
#input_op=/projects/output/merged/merged_logs/sampleA-20121111-20121112
#input_op_pre=''
#input_op_post=''

input_op="-input ${input_op} "

#one week only

echo $input_op
 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_classify_events.py" -file mapper_classify_events.py -reducer 'cat'  -jobconf mapred.job.name=yandong_classify -jobconf mapred.reduce.tasks=500
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_classify_events.py" -file mapper_classify_events.py -reducer 'cat'  -jobconf mapred.job.name=yandong_classify -jobconf mapred.reduce.tasks=500

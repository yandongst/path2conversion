## product count of event-camp or event-social for lift calculation 
##
##
##

hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

fn=$3 
OUTDIR=$2/$fn 
input_op="-input $1 " 
 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count_kw.py $fn" -file mapper_count_kw.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count_kw.py $fn" -file mapper_count_kw.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2 -jobconf mapred.job.queue.name=p1

hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
## product count of event-camp or event-social for lift calculation 
##
##
##

pythonbin=/usr/bin/python2.7

fn=$3 
OUTDIR=$2/$fn 
input_op="-input $1 " 
 
<<<<<<< HEAD
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count.py $fn" -file mapper_count.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count2.py $fn" -file mapper_count2.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2 -jobconf mapred.job.queue.name=p1
=======
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count.py $fn" -file mapper_count.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_count2.py $fn" -file mapper_count2.py -file $fn -reducer "$pythonbin reducer_count.py" -file ../../reducer_count.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=2 -jobconf mapred.job.queue.name=p1
>>>>>>> 5672ebcfb487d5abc5374b281851c191ce3dd4bd

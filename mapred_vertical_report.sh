hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

OUTDIR=/projects/output/merged/vertical_report/20111001-20111005

input_op=/projects/output/merged/domain_report_w_verticals/20111001-20111005
input_op_pre=''
input_op_post=''

input_op="-input ${input_op} "

echo $input_op
 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_vertical_report.py" -file mapper_vertical_report.py -reducer "$pythonbin reducer_vertical_report.py" -file reducer_vertical_report.py  -jobconf mapred.job.name=vertical_repotr -jobconf mapred.reduce.tasks=200
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_vertical_report.py" -file mapper_vertical_report.py -reducer "$pythonbin reducer_vertical_report.py" -file reducer_vertical_report.py  -jobconf mapred.job.name=vertical_repotr -jobconf mapred.reduce.tasks=200

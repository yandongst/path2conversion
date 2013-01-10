hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

OUTDIR=/projects/output/merged/domain_report_w_verticals/20111001-20111005

input_op=/projects/output/merged/domain_delivery_perform/20111001-20111005
input_op_pre=''
input_op_post=''

input_op="-input ${input_op} "

fn_d2v=$1
fn_camp2name="camp2name.csv"


echo $input_op
 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_domain_vert_impr.py $fn_d2v $fn_camp2name" -file mapper_domain_vert_impr.py -file $fn_d2v -file $fn_camp2name -reducer "$pythonbin reducer_domain_vert_impr.py" -file reducer_domain_vert_impr.py  -jobconf mapred.job.name=add_vertical -jobconf mapred.reduce.tasks=200
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_domain_vert_impr.py $fn_d2v $fn_camp2name" -file mapper_domain_vert_impr.py -file $fn_d2v -file $fn_camp2name -reducer "$pythonbin reducer_domain_vert_impr.py" -file reducer_domain_vert_impr.py  -jobconf mapred.job.name=add_vertical -jobconf mapred.reduce.tasks=200

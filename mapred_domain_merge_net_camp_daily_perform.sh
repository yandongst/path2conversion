hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

OUTDIR=/projects/output/merged/net_camp_daily_perform/20121022

#input_op=/user/root/yandong/01_05_01_10_preprocess_logs_end_A/
input_op="/projects/input/ctrlogs/net_camp_daily/20121022"
input_op+=",/projects/input/ctrlogs/net_camp_daily/20121022"
input_op_pre=''
input_op_post=''

input_op="-input ${input_op} "

fn_d2v="d2v_impr_1022.txt"
fn_camp2name="camp2name.csv"


echo $input_op
 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_domain_vert_impr.py $fn_d2v $fn_camp2name" -file mapper_domain_vert_impr.py -file $fn_d2v -file $fn_camp2name -reducer "$pythonbin reducer_domain_vert_impr.py" -file reducer_domain_vert_impr.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=200
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin mapper_domain_vert_impr.py $fn_d2v $fn_camp2name" -file mapper_domain_vert_impr.py -file $fn_d2v -file $fn_camp2name -reducer "$pythonbin reducer_domain_vert_impr.py" -file reducer_domain_vert_impr.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=200

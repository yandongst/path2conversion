hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

#input_path="/projects/output/merged/domain_delivery/20121001-20121003"
input_path=$1
#OUTDIR_HOME="/projects/output/merged/domain_delivery_with_verticals/20121001-20121003"
OUTDIR_HOME=$2

google_cate_fn="google_cates.csv"
mapper_fn="expand_domain2vertical.py"
mapper_opt="$pythonbin $mapper_fn $google_cate_fn"
reducer_opt="cat" 

 
echo $hstream -input "$input_path" -output ${OUTDIR_HOME} -mapper "$mapper_opt" -file $mapper_fn -file $google_cate_fn -reducer "$reducer_opt" -jobconf mapred.job.name=add_vertical -jobconf mapred.reduce.tasks=200
$hstream -input $input_path -output ${OUTDIR_HOME} -mapper "$mapper_opt" -file $mapper_fn -file $google_cate_fn -reducer "$reducer_opt" -jobconf mapred.job.name=add_vertical -jobconf mapred.reduce.tasks=200

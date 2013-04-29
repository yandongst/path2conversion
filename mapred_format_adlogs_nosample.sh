hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
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

dir="/home/yandong/workspace/path"

#/projects/science/input/adlogs_new/20130301/2013030100/all_data_hourly/part-00000.gz
input_op_pre=/projects/science/input/adlogs_new
printf -v OUTDIR "/projects/science/output/merged/adlogs/%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year ${m2#0} $d2
echo $OUTDIR

input_path="" 


input_op_post="all_data_hourly"

function check_and_cp() {
  echo check_and_cp $1 #$2
  date=$1
  path="${input_op_pre}/${date}/*/${input_op_post}"
  hadoop fs -test -z $path 2> /dev/null
  if [ $? -eq 0 ]
  then
    echo input_path+=$path,
    input_path+=$path/part*,
  else
    echo $path doesnt exist!
  fi
}

#####same month
if [ $m1 -eq $m2 ]
then
    for (( d=$d1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02i" $year $m1 $d 
      check_and_cp $date

    done

else
#####diff months 
  #######first month
    for (( d=$d1; d <= 31; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m1 $d
      check_and_cp $date
    done

  let m_start=$m1+1
  let m_end=$m2-1

  #######mid months 
  for (( m=$m_start; m <=$m_end; m++ ))
  do 
      for (( d=1; d <= 31; d++ ))
      do
        printf -v date "%04d%02d%02d" $year $m $d
      check_and_cp $date
  done
  done

  #######last month
    for (( d=1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m2 $d
      check_and_cp $date
    done

fi

echo ${input_path}


l=`expr length $input_path`
input_path2=${input_path:0:$l-1}



echo $hstream -input "$input_path2" -output ${OUTDIR} -mapper 'python mapper_format_adlogs.py nosample' -file $dir/mapper_format_adlogs.py -reducer 'cat'  -jobconf mapred.job.name=yandong_event_w_timestamp -jobconf mapred.reduce.tasks=50
$hstream -input "$input_path2" -output ${OUTDIR} -mapper 'python mapper_format_adlogs.py nosample' -file $dir/mapper_format_adlogs.py -reducer 'cat'  -jobconf mapred.job.name=yandong_event_w_timestamp -jobconf mapred.reduce.tasks=50 -jobconf mapred.job.queue.name=science

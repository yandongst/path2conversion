#hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
pythonbin=/usr/bin/python2.7

year=$1
m1=$2
d1=$3
m2=$4
d2=$5

INPUT_HOME=/projects/input/merged_logs/
#printf -v OUTDIR_HOME "/projects/output/merged/merged_logs/sampleA-%04d%02d%02d-%04d%02d%02d" $year ${m1#0} $d1 $year ${m2#0} $d2

#echo $OUTDIR_HOME

input_path="" 

#####same month
if [ $m1 -eq $m2 ]
then
    for (( d=$d1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02i" $year ${m1#0} $d
      hadoop fs -test -z ${INPUT_HOME}${date} 2> /dev/null
      if [ $? -eq 0 ]
      then
        input_path+=${INPUT_HOME}${date},
      else
        echo ${INPUT_HOME}${date}, doesnt exist!
      fi
    done

else
#####diff months 
  #######first month
    for (( d=$d1; d <= 31; d++ ))
    do
      printf -v date "%04d%02d%02d" $year ${m1#0} $d
      hadoop fs -test -z ${INPUT_HOME}${date} 2> /dev/null
      if [ $? -eq 0 ]
      then
        input_path+=${INPUT_HOME}${date},
      else
        echo ${INPUT_HOME}${date}, doesnt exist!
      fi
    done

  let m_start=$m1+1
  let m_end=$m2-1

  #######mid months 
  for (( m=$m_start; m <=$m_end; m++ ))
  do 
      for (( d=1; d <= 31; d++ ))
      do
        printf -v date "%04d%02d%02d" $year ${m#0} $d
        hadoop fs -test -z ${INPUT_HOME}${date} 2> /dev/null
        if [ $? -eq 0 ]
        then
          input_path+=${INPUT_HOME}${date},
        else
          echo ${INPUT_HOME}${date}, doesnt exist!
        fi
      done
  done

  #######last month
  for (( d=1; d <= $d2; d++ ))
  do
    printf -v date "%04d%02d%02d" $year ${m2#0} $d
    hadoop fs -test -z ${INPUT_HOME}${date} 2> /dev/null
    if [ $? -eq 0 ]
    then
      input_path+=${INPUT_HOME}${date},
    else
      echo ${INPUT_HOME}${date}, doesnt exist!
    fi
  done

fi



l=`expr length $input_path`
input_path2=${input_path:0:$l-1}


OUTDIR=$6

#no sample
#change mapper_classify_events.py back if you want sampling
echo $hstream -input $input_path2 -output ${OUTDIR} -mapper "$pythonbin mapper_classify_events.py" -file mapper_classify_events.py -reducer 'cat'  -jobconf mapred.job.name=yandong_classify -jobconf mapred.reduce.tasks=500
$hstream -input $input_path2 -output ${OUTDIR} -mapper "$pythonbin mapper_classify_events.py" -file mapper_classify_events.py -reducer 'cat'  -jobconf mapred.job.name=yandong_classify -jobconf mapred.reduce.tasks=500

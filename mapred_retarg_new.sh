
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

#htext /projects/science/input/retarg_new/2013040100/data/data-m-0*.gz|python mapper_retarg_new.py st|python reducer_retarg_new.py |less

INPUT_HOME=/projects/science/input/retarg_new/
printf -v OUTDIR_HOME "/projects/science/output/merged/retarg_new_stats/%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2
post=data

input_path="" 

#####same month
if [ $m1 -eq $m2 ]
then
    for (( d=$d1; d <= $d2; d++ ))
    do
      for (( dd=0; dd <= 23; dd++ ))
      do
      printf -v date "%04d%02d%02i%02i" $year $m1 $d $dd
      echo $date
      hadoop fs -test -z ${INPUT_HOME}${date}/${post} 2> /dev/null
      if [ $? -eq 0 ]
      then
        input_path+=${INPUT_HOME}${date}/${post},
      else
        echo ${INPUT_HOME}${date}/${post}, doesnt exist!
      fi
      done
    done

else
#####diff months 
  #######first month
    for (( d=$d1; d <= 31; d++ ))
    do
      for (( dd=0; dd <= 23; dd++ ))
      do
      printf -v date "%04d%02d%02i%02i" $year $m1 $d $dd
      echo $date
      hadoop fs -test -z ${INPUT_HOME}${date}/${post} 2> /dev/null
      if [ $? -eq 0 ]
      then
        input_path+=${INPUT_HOME}${date}/${post},
      else
        echo ${INPUT_HOME}${date}/${post}, doesnt exist!
      fi
      done
    done

  let m_start=$m1+1
  let m_end=$m2-1

  #######mid months 
  for (( m=$m_start; m <=$m_end; m++ ))
  do 
      for (( d=1; d <= 31; d++ ))
      do
      for (( dd=0; dd <= 23; dd++ ))
      do
      printf -v date "%04d%02d%02i%02i" $year $m1 $d $dd
      echo $date
        hadoop fs -test -z ${INPUT_HOME}${date}/${post} 2> /dev/null
        if [ $? -eq 0 ]
        then
          input_path+=${INPUT_HOME}${date}/${post},
        else
          echo ${INPUT_HOME}${date}/${post}, doesnt exist!
        fi
      done
      done
  done

  #######last month
  for (( d=1; d <= $d2; d++ ))
  do
      for (( dd=0; dd <= 23; dd++ ))
      do
      printf -v date "%04d%02d%02i%02i" $year $m1 $d $dd
      echo $date
    hadoop fs -test -z ${INPUT_HOME}${date}/${post} 2> /dev/null
    if [ $? -eq 0 ]
    then
      input_path+=${INPUT_HOME}${date}/${post},
    else
      echo ${INPUT_HOME}${date}/${post}, doesnt exist!
    fi
      done
  done

fi



l=`expr length $input_path`
input_path2=${input_path:0:$l-1}

field=st

echo $hstream -input $input_path2 -output ${OUTDIR_HOME} -mapper "python mapper_retarg_new.py $field" -file $dir/mapper_retarg_new.py -reducer 'python reducer_retarg_new.py'  -file $dir/reducer_retarg_new.py -jobconf mapred.job.name=retarg -jobconf mapred.reduce.tasks=1
$hstream -input $input_path2 -output ${OUTDIR_HOME} -mapper "python mapper_retarg_new.py $field" -file $dir/mapper_retarg_new.py -reducer 'python reducer_retarg_new.py'  -file $dir/reducer_retarg_new.py -jobconf mapred.job.name=retarg -jobconf mapred.reduce.tasks=1 -jobconf mapred.job.queue.name=science

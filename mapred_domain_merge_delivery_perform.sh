hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-0.23.1-mr1-cdh4.0.0b2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'

##TEST ONLY. TIME PERIODS ARE NOT THE SAME##
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

INPUT_HOME=/projects/input/ctrlogs/net_camp_daily/
printf -v input_combination "/projects/output/merged/adlogs_retarg_combination/%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2
printf -v OUTDIR_HOME "/projects/output/merged/domain_delivery_perform_merged/%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

#input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121001/ "
#input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121002/ "
#input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121003/ "
#input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121004/ "
#input_op+="-input /projects/input/ctrlogs/net_camp_daily/20121005/ "
#input_op+="-input /projects/output/merged/adlogs_retarg_combination/20121101-20121110/ "


input_path="" 

#####same month
if [ $m1 -eq $m2 ]
then
    for (( d=$d1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02i" $year $m1 $d
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
      printf -v date "%04d%02d%02d" $year $m1 $d
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
        printf -v date "%04d%02d%02d" $year $m $d
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
    printf -v date "%04d%02d%02d" $year $m2 $d
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
input_path+=${input_combination}
#input_path2=${input_path:0:$l-1}


fn_pixel=pixel_test.txt
mapper_fn="mapper_domain_merge_delivery_perform.py" 
mapper_opt="python $mapper_fn"
reducer_fn="reducer_domain_merge_delivery_perform.py" 
reducer_opt="python $reducer_fn"



echo $hstream  -input ${input_path} -output ${OUTDIR_HOME} -mapper "$mapper_opt" -file $mapper_fn -reducer "$reducer_opt"  -file $reducer_fn -jobconf mapred.reduce.tasks=500 -jobconf mapred.job.name='domain_deivery_perform_merge'
$hstream  -input ${input_path} -output ${OUTDIR_HOME} -mapper "$mapper_opt" -file $mapper_fn -reducer "$reducer_opt"  -file $reducer_fn -jobconf mapred.reduce.tasks=500 -jobconf mapred.task.timeout=3600000 -jobconf mapred.job.name='domain_deivery_perform_merge'

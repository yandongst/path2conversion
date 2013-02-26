#htext /projects/input/adlogs/normalized_rtb_adlog/click/2012090?/valid*/p*|cut -f1|sort|uniq -c > 0901_0909_click.txt

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

input_op_pre=/projects/science/input/adlogs/normalized_rtb_adlog

input_path="" 

events='impr'


input_op_post=validdata_*

function check_and_cp() {
  #echo check_and_cp $1 #$2
  path=$1
  #input_path=$2
  hadoop fs -test -z $path 2> /dev/null
  if [ $? -eq 0 ]
  then
    input_path+="$path/part* "
  else
    echo $path doesnt exist!
  fi
}

#####same month
if [ $m1 -eq $m2 ]
then
  for event in $events
  do
    for (( d=$d1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02i" $year $m1 $d

      input_this="${input_op_pre}/${event}/${date}/${input_op_post} "
      check_and_cp $input_this

    done
  done

else
#####diff months 
  #######first month
  for event in $events
  do
    for (( d=$d1; d <= 31; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m1 $d
      input_this="${input_op_pre}/${event}/${date}/${input_op_post} "
      check_and_cp $input_this
    done
  done

  let m_start=$m1+1
  let m_end=$m2-1

  #######mid months 
  for event in $events
  do
  for (( m=$m_start; m <=$m_end; m++ ))
  do 
      for (( d=1; d <= 31; d++ ))
      do
        printf -v date "%04d%02d%02d" $year $m $d
      input_this="${input_op_pre}/${event}/${date}/${input_op_post} "
        check_and_cp $input_this
  done
  done
  done

  #######last month
  for event in $events
  do
    for (( d=1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m2 $d
      input_this="${input_op_pre}/${event}/${date}/${input_op_post} "
      check_and_cp $input_this
    done
  done

fi



l=`expr length "$input_path"`
input_path2=${input_path:0:$l-1}

#hadoop fs -text /projects/input/adlogs/normalized_rtb_adlog/impr/201212*/valid*/p*|cut -f1|sort -T tmp|uniq -c > 201212_camp.txt
echo hadoop fs -text $input_path2\|cut -f1\|sort -T tmp\|uniq -c 
hadoop fs -text $input_path2|cut -f1|sort -T tmp|uniq -c 

ACCDIR=/home/yandong
dest=/projects/science/input/retarg_poe

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


function cp_data() {
  date=$1
  hadoop fs -test -d $dest/${date} 2> /dev/null
  if [ $? -ne 0 ]
  then
    echo COPYING: hadoop distcp -conf ${ACCDIR}/account/insight-site.xml s3n://campaign-analytics/parsed_adlogs/extract_retarg_log/dt=${date}/ $dest/${date}
    #hadoop fs -conf /root/insight-account/core-site.xml -get s3n://campaign-analytics/parsed_adlogs/extract_retarg_log/dt=${date}/ .
    hadoop distcp -conf ${ACCDIR}/account/insight-site.xml s3n://campaign-analytics/parsed_adlogs/extract_retarg_log/dt=${date}/ $dest/${date}
  else
    echo WARNING: path already exists! $dest/${date}. skip copying...
    fi
}

#####same month
if [ $m1 -eq $m2 ]
then 
    for (( d=$d1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m1 $d
      cp_data $date
    done

else
#####diff months

  #######first month
    for (( d=$d1; d <= 31; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m1 $d
      cp_data $date
    done

  let m_start=$m1+1
  let m_end=$m2-1

  #######mid months 
  for (( m=$m_start; m <=$m_end; m++ ))
  do 
      for (( d=1; d <= 31; d++ ))
      do
        printf -v date "%04d%02d%02d" $year $m $d
        cp_data $date
      done
  done

  #######last month
    for (( d=1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m2 $d
      cp_data $date 
  done

fi


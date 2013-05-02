ACCDIR=/home/yandong
dest=/projects/science/input/retarg_new

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
    #hadoop fs -conf /root/insight-account/core-site.xml -get s3n://campaign-analytics/parsed_adlogs/extract_retarg_log/dt=${date}/ .
    for (( d1=0; d1 <= 23; d1++ ))
    do
      printf -v dd "%02d" $d1 
      echo ${date}${dd}
      hadoop fs -test -d $dest/${date}{$dd} 2> /dev/null
      if [ $? -ne 0 ]
      then
        echo hadoop distcp -conf ${ACCDIR}/account/prod-site.xml s3n://sharethis-campaign-analytics/retarg/${date}${dd} $dest/${date}${dd}/
        hadoop distcp -conf ${ACCDIR}/account/prod-site.xml s3n://sharethis-campaign-analytics/retarg/${date}${dd} $dest/${date}${dd}/
      else
        echo WARNING: path already exists! $dest/${date}${dd}. skip copying...
        fi
    done
}

#####same month
if [ $m1 -eq $m2 ]
then 
    for (( d=$d1; d <= $d2; d++ ))
    do
      printf -v date "%04d%02d%02d" $year $m1 $d
      echo cp_data $date
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


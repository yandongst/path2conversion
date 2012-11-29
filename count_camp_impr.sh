while read line
do
echo -n $line " "
topsum=`grep -i $line 1022_camp_vert_dist_topcate.txt |cut -f3|awk '{c+=$1}END{print c}'`
allsum=`grep -i $line 1022_camp_vert_dist.txt |cut -f3|awk '{c+=$1}END{print c}'`
echo -n $topsum", "
echo  $allsum
done < all_camp.txt

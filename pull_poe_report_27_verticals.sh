year=$1
m1=$2
d1=$3
m2=$4
d2=$5


set mapred.job.queue.name=p1;

dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo ${dates}

retarg=dummy 

camp=%ANY%


for vert in arts_and_entertainment game_video_game government social_cultural_religion technology health arts_and_entertainment_music sports shopping_consumer_electronics business social_cultural_family_parenting health_fitness shopping_food_and_drink government_law_legal adult travel science education shopping_tobacco business_investment automotive business_employment business_mortgage_real_estate business_finance_service shopping_home_garden shopping_pets shopping_beauty shopping_clothing shopping_jewelry 
do

fn=${camp}_${vert}
echo impr:$camp >$fn
echo click:$camp >>$fn
echo retarg:$retarg >>$fn
echo cate:$vert >>$fn
cat $fn
./mapred_adlift_combination_count.sh /projects/science/output/merged/userevents_adlogs_retarg/${timeperiod} /projects/science/output/merged/userevents_adlogs_retarg_cnt/vertical/${timeperiod}/ $fn
hadoop fs -text /projects/science/output/merged/userevents_adlogs_retarg_cnt/vertical/${timeperiod}/${fn}/part-0000*.gz|python metrics_adlift.py|python add_adgroup_name.py > lift_${fn}_adg.txt
cat lift_${fn}_adg.txt|python convert2highchart.py >  lift_${fn}.txt
rm $fn

done


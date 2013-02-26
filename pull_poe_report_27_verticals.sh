year=2012
m1=12
d1=4
m2=12
d2=16


set mapred.job.queue.name=p1;

dates="$year $m1 $d1 $m2 $d2"

printf -v timeperiod "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

echo ${dates}

retarg=dummy 


for vert in arts_and_entertainment game_video_game government social_cultural_religion technology health arts_and_entertainment_music sports shopping_consumer_electronics business social_cultural_family_parenting health_fitness shopping_food_and_drink government_law_legal adult travel science education shopping_tobacco business_investment automotive business_employment business_mortgage_real_estate business_finance_service shopping_home_garden shopping_pets shopping_beauty shopping_clothing shopping_jewelry 
do

fn=${camp}_${vert}
echo impr:$camp >$fn
echo click:$camp >>$fn
echo retarg:$retarg >>$fn
echo cate:$vert >>$fn
cat $fn
./mapred_adlift_combination_count.sh /projects/output/merged/userevents_adlogs_retarg/${timeperiod} /projects/output/merged/userevents_adlogs_retarg_cnt/${timeperiod}/ ${camp}_${vert}
hadoop fs -text /projects/output/merged/userevents_adlogs_retarg_cnt/${timeperiod}/${camp}_${vert}/part-0000*.snappy|python metrics_adlift.py > lift_${camp}_${vert}.txt

done


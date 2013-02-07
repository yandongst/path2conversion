dirlift=lift_20121204_20121216_nosample/
camp=RTB-Clorox_PABF-RT 

for vert in arts_and_entertainment game_video_game government social_cultural_religion technology health arts_and_entertainment_music sports shopping_consumer_electronics business social_cultural_family_parenting health_fitness shopping_food_and_drink government_law_legal adult travel science education shopping_tobacco business_investment automotive business_employment business_mortgage_real_estate business_finance_service shopping_home_garden shopping_pets shopping_beauty shopping_clothing shopping_jewelry 
do

pwd

fn=lift_${camp}_${vert}.txt
cat $fn|python add_adgroup_name.py > ${fn}_adgname.txt
mv ${fn}_adgname.txt $dirlift
cd $dirlift
cat ${fn}_adgname.txt|python ../convert2highchart.py > ${fn}_channels.txt

cd ..

done


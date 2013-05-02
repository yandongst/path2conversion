### for finance vertical ###

y=$1
m1=$2
d1=$3
m2=$4
d2=$5

label=$6

rm liftsummary_${label}_${y}${m1}${d1}_${m2}${d2}.txt

#for f in merrilledge hrblock equifax hiscox amex_serve vertical_finance -- finance vertical
#for f in att_wired att_consumer dish samsung radioshack vertical_tech_electronics # tech/electronics vertical
for f in msft_surface #att_wired att_consumer dish samsung radioshack # tech/electronics vertical
#for f in petco aspca vertical_pets # pets
#for f in toyota hyundai vertical_automotive #automotive
#for f in disney greyhound vertical_travel #travel
do
    sh -x pull_vertical_poe_report.sh ${y} ${m1} ${d1} ${m2} ${d2} pixel_${f}.txt POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}.txt
    #sh -x pull_kw_poe_report.sh ${y} ${m1} ${d1} ${m2} ${d2} pixel_${f}.txt POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}.txt
    cat POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}.txt | python add_adgroup_name.py > POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}_adg.txt
    cat POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}_adg.txt |python convert2highchart.py > POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}_final_vertical.txt
    perl ~yqu/workspace/scripts/getLiftSummary.pl POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}_final_vertical.txt  >> liftsummary_${label}_${y}${m1}${d1}_${m2}${d2}.txt
    rm POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}_adg.txt
    rm POE_pixel_${f}_${y}${m1}${d1}_${m2}${d2}_final.txt
done

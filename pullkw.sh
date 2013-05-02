rtb=MGM_Monte_Carlo-RT
rtb=MGM_O-RT
rtb=NYNY-RT
rtb=msft_surface_grp3

bin=./pull_kw_poe_report.sh

$bin 2013 1 27  2 2 pixel_${rtb}.txt  tttt.txt
cat tttt.txt|python convert2highchart.py > ${rtb}_kw_1_27_2_2_final.txt
$bin 2013 2 3  2 9 pixel_${rtb}.txt  tttt.txt
cat tttt.txt|python convert2highchart.py > ${rtb}_kw_2_3_2_9_final.txt
$bin 2013 2 10 2 16 pixel_${rtb}.txt  tttt.txt
cat tttt.txt|python convert2highchart.py > ${rtb}_kw_2_10_2_16_final.txt
$bin 2013 2 17 2 23 pixel_${rtb}.txt  tttt.txt
cat tttt.txt|python convert2highchart.py > ${rtb}_kw_2_17_2_23_final.txt

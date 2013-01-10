
### 3# means tested

bin=/data/4/yandong/projects/path

year=2012
m1=12
d1=4
m2=12
d2=16
printf -v timewindow "%04d%02d%02d-%04d%02d%02d" $year $m1 $d1 $year $m2 $d2

cd $bin

# get data

echo =============================================
echo ===== COPYING ADLOGS DATA =====
echo =============================================

./cp_adlogs.sh $year $m1 $d1 $m2 $d2

echo =============================================
echo ===== COPYING RETARGETING DATA =====
echo =============================================
./cp_retarg.sh $year $m1 $d1 $m2 $d2

# merge
# output dir: /projects/output/merged/adlogs_retarg/20121101-20121111

echo =============================================
echo ===== MERGING ADLOGS DATA =====
echo =============================================
./mapred_format_adlogs_nosample.sh $year $m1 $d1 $m2 $d2
echo =============================================
echo ===== MERGING RETARGETING DATA =====
echo =============================================
./mapred_retarg_nosample.sh $year $m1 $d1 $m2 $d2
echo =============================================
echo ===== MERGING ADLOGS/RETARG DATA =====
echo =============================================
./mapred_domain_perform_merge.sh $year $m1 $d1 $m2 $d2

# compute conversion
# format: [campaignid--domain--ctr|vtr|ctc|vtc] [count]
# output: /projects/output/merged/adlogs_retarg_combination/

echo =============================================
echo ===== GENERATE PERFORMANCE COMBINATIONS ===== 
echo =============================================
 ./mapred_domain_perform_combination.sh $year $m1 $d1 $m2 $d2 #(!!! NEED to do compaign info) / skip this for now

###########################

# copy ctr data

echo =============================================
echo ===== COPYING NET_CAMP DATA ===== 
echo =============================================
./cp_ctrlogs_camp.sh $year $m1 $d1 $m2 $d2
echo =============================================
echo ===== COPYING VERT_CAMP DATA
echo =============================================
./cp_ctrlogs_vert.sh $year $m1 $d1 $m2 $d2

# merge delivery with performance data
#input: /projects/input/ctrlogs/net_camp_daily/2, /projects/output/merged/adlogs_retarg_combination/ (this is output of part 2)
#output: /projects/output/merged/domain_delivery_perform_merged/
#format: domain--campid impr click ctr ctr vtr ctc vtc

echo =============================================
echo ===== MERGING DELIVERY WITH PERFORMANCE DATA
echo =============================================
./mapred_domain_merge_delivery_perform.sh $year $m1 $d1 $m2 $d2

# produce normalized domain2vertical data
# input: /projects/input/ctrlogs/vert_net_daily/
# output: /projects/output/merged/domain_delivery/20121001-20121003
# format: [domain] [cate] [weight]


echo =============================================
echo ===== NORMALIZING DOMAIN-CATE WEIGHTING =====
echo =============================================
./mapred_domain_delivery_normalize.sh  $year $m1 $d1 $m2 $d2

# produce expanded domain2vertical based on output above (add names)
# input: /projects/output/merged/domain_delivery/20121001-20121003
# output: /projects/output/merged/domain_delivery_with_verticals/20121001-20121003/
# output: [domain] [cate-name] weight
domain_vert_file="d2v_impr_1127.txt"

echo =====================================================
echo ===== EXPAND VERTICALS TO ALL ITS PARENT LEVELS =====
echo =====================================================
input_path="/projects/output/merged/domain_delivery/$timewindow"
OUTDIR_HOME="/projects/output/merged/domain_delivery_with_verticals/$timewindow"

./mapred_domain_expand_domain2vertical_yan.sh ${input_path} ${OUTDIR_HOME}

# produce weighting schema file
# output file - d2v_impr.txt (dv2_impr.txt.bak)

#htext /projects/output/merged/domain_delivery_with_verticals/20121001-20121003/p* > d2v_impr.txt
echo =====================================================
echo ===== PRODUCING DOMAIN-CATE WEIGHTING FILE =====
echo =====================================================
hadoop fs -text ${OUTDIR_HOME}/p* > ${domain_vert_file}

# add verticals to output above (need to specific input/output/schema file/camp2name mappings
# output location:/projects/output/merged/domain_report_w_verticals/20111001-20111005
# output format: [camp id] [camp name] [domain] [categories] [impr] [click] [ctr] [ctr1] [vtr] [ctc] [vtc]

#./mapred_domain_add_verticals.sh #(!!! NEED to change input/output)

input=/projects/output/merged/domain_delivery_perform_merged/$timewindow
output=/projects/output/merged/domain_delivery_w_verticals/$timewindow
report=/projects/output/merged/vertical_report/$timewindow

echo =====================================================
echo ===== ADD VERITICALS TO OUTPUT ABOVE  =====
echo =====================================================
./mapred_domain_add_verticals_yan.sh ${input} ${output} ${domain_vert_file} #(!!! NEED to change input/output)

#ctr=click-thru-rate
#ctr1=click-thru-retarging

# aggregate to vertical-level report (!!! NEED to specificy input/output)
# output location: /projects/output/merged/vertical_report/20111001-20111005
# output format: [camp id] [camp name] [categories] [impr] [click] [ctr] [ctr1] [vtr] [ctc] [vtc]

#./mapred_vertical_report.sh #(!!! NEED to change input/output)

echo =====================================================
echo ===== AGGREGATE TO VERITICALS LEVEL  =====
echo =====================================================
./mapred_vertical_report_yan.sh ${output} ${report}



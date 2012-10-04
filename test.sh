n=1000000
#hadoop fs -text /projects/output/merged/merged_logs_classified/sampleA-20120725-20120805/*.gz|head -${n} >1.txt
#hadoop fs -text /projects/output/merged/adlogs/20120725-20120805-endingA/*.gz|head -${n} > 2.txt
#hadoop fs -text /projects/output/merged/retarg/20120725-20120805-endA/*.gz|head -${n} > 3.txt

cat 1.txt 2.txt 3.txt |python mapper_merge_all_events_all_cates.py equifax_pixels.txt |python /data/4/yandong/reducer.py 

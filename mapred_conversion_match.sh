hstream='hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.2.jar -D mapred.output.compress=true -D mapred.output.compression.codec=org.apache.hadoop.io.compress.GzipCodec'
## product count of event-camp or event-social for lift calculation 
##
##
##

pythonbin=/usr/bin/python2.7

fn=pixel_hsn.txt
OUTDIR="/projects/science/output/merged/conversion_match/20130401-20130414/$fn"
input_op="-input /projects/science/output/merged/userevents_adlogs_retarg/20130401-20130414"

lastday=20130414
#htext /projects/science/output/merged/userevents_adlogs_retarg/20130414-20130420/*gz|python conversion_match.py pixel_hsn.txt  20130419
 
echo $hstream $input_op -output ${OUTDIR} -mapper "$pythonbin conversion_match.py $fn $lastday" -file conversion_match.py -file $fn -reducer "$pythonbin reducer_conversion.py" -file reducer_conversion.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=1
$hstream $input_op -output ${OUTDIR} -mapper "$pythonbin conversion_match.py $fn $lastday" -file conversion_match.py -file $fn -reducer "$pythonbin reducer_conversion.py" -file reducer_conversion.py  -jobconf mapred.job.name=yandong_path_count -jobconf mapred.reduce.tasks=1 -jobconf mapred.job.queue.name=p1

#!/usr/bin/env bash
phtemp="4.5 5.0 5.5 6.5 6.5 7.0 7.5 8.0"
name1="pA"
range="1-500"
echo $name
sasa="7.7 8.0 8.3 8.8"
for k in $sasa; do
for r in $range; do
python3 avg_error.py pA_s1_1-500_bb_shppf_8.3.dat-pA_6.5_30_data.txt.txt pA_s2_1-500_bb_shppf_8.3.dat-pA_6.5_30_data.txt.txt pA_s3_1-500_bb_shppf_8.3.dat-pA_6.5_30_data.txt.txt pA_avg_error_shpf_6.5_8.3.dat
done;
done;

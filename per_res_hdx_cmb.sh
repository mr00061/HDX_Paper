#!/usr/bin/env bash
phtemp=6.5_30
num="1 2 3"
name="pA nt17 pS"
echo $name
sasa="7.7 8.0 8.3 8.6 8.8"
for i in $name; do 
for j in $num; do
for k in $sasa; do
python3 bk.py ${i}copy_$phtemp.txt ${i}_s${j}_1-500_bb_shwpf_$k.dat $k.dat data_$k.dat
done;
done;
done;

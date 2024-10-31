
source ../script/polyA_M3_bb_hdx.tcl
set rad 0.4
set distcutoff 3.5
set anglecutoff 179
set nf 19999
foreach d {7.7 8.0} {hdx-sasa 0 $nf $d $rad $distcutoff $anglecutoff polyA_s1_1-400_bb_shwo_$d.dat polyA_s1_1-400_bb_shw_$d.dat polyA_s1_1-400_bb_shwop_$d.dat polyA_s1_1-400_bb_shwp_$d.dat polyA_s1_1-400_bb_shwpf_$d.dat polyA_s1_1-400_bb_shwdG_$d.dat}


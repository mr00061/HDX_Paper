
source polyA_M3_bb_hdx.tcl
set rad 0.4
set distcutoff 3.5
set anglecutoff 179
set nf 2000
foreach d {8.6} {hdx-sasa 0 $nf $d $rad $distcutoff $anglecutoff polyA_test_bb_shwo_$d.dat polyA_test_bb_shw_$d.dat polyA_test_bb_shwop_$d.dat polyA_test_bb_shwp_$d.dat polyA_test_bb_shwpf_$d.dat polyA_test_bb_shwdG_$d.dat}


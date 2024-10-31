
source ../script/percenthelicity.tcl
set molid 0

foreach a {1} {percenthelicity $molid "protein" ph_pA_500ns_s1$a.dat}

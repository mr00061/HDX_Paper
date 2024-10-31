puts "Owner: Mohammad Azizur Rahman Jewel, Mertz Lab, Chemistry, WVU"
puts "Date: 03/25/2022 "
puts "Special direction-"
puts "Data Collection for HDX based on SASA"
puts "Each backbone NH vs probability of close and open state over trajectory"
puts "It will also collect date comprehensively for all open and close state as on off binary"
puts "usage: hdx-sasa <molid> <nf> <st> <rad> <chain>  <o_so.dat> <o_sc.dat> <o_sop.dat> <o_scp.dat> <o_spf.dat> <o_wo.dat> <o_wc.dat> <o_wop.dat> <o_wcp.dat> <o_wpf.dat> <o_shpo.dat> <o_shpc.dat> <o_shpop.dat> <o_shpcp.dat> <o_shppf.dat><o_shwo.dat> <o_shwc.dat> <o_shwop.dat> <o_shwcp.dat> <o_shwpf.dat> "


proc hdx-sasa {molid nf st rad distcutoff anglecutoff o_shwo o_shwc o_shwop o_shwcp o_shwpf o_shwdG} {

#Set outfile for hbond with water based raw open, close, open_probability close_probability, protection factor

set out_shwo [open "$o_shwo" w]
set out_shwc [open "$o_shwc" w]
set out_shwop [open "$o_shwop" w]
set out_shwcp [open "$o_shwcp" w]
set out_shwpf [open "$o_shwpf" w]
set out_shwdG [open "$o_shwdG" w]
set out_hdx_shw [open pA_M3_bb.dat a+]
#get total number of frame
#set nf [molinfo $molid get numframes]
#setting for all backbone N as acceptor
set indexH {21 31 41 51 61 83 93 103 113 123 145 155 165 175 185 207 217 227 237 247}
set indexD {20 30 40 50 60 82 92 102 112 122 144 154 164 174 184 206 216 226 236 246}
set l [llength $indexH]


set hdx_shw 0
#setting up for overall calculation
foreach x $indexH y $indexD {
set res [atomselect top "index $x"]
set resid [$res get resid]
$res delete

# Set initial parameter for protection factor calculation

set cl_shw 0
set op_shw 0

#Set index as 
set data_shwo $y
set data_shwc $y

#Atomselection for
set selP [atomselect $molid "protein"]
set selH [atomselect $molid "index $x"]
set selD [atomselect $molid "index $y"]
set selW [atomselect $molid "water and name OH2"]

#Loop through overall selected frame
	for {set i 1 } {$i < $nf } {incr i } {
	$selP frame $i
	$selH frame $i
	$selD frame $i
	$selW frame $i
	$selP update
	$selH update
	$selD update
	$selW update
	set s [measure sasa $rad $selP -restrict $selH]
        set hbww [lindex [measure hbonds $distcutoff $anglecutoff $selD $selW] 1]
	set n_hbww [llength $hbww]


#hdx calculation based on sasa and hb with water only
        if {$s > $st && $n_hbww >=2} {
                set shwo 1
                set op_shw [expr {$shwo + $op_shw }]
        } else {set shwo 0}
        #finding total, that will be used to find fraction contact in simulated>
        if {$s<$st && $n_hbww < 1}  {
                set shwc 1
                set cl_shw [expr {$cl_shw + $shwc }]
                } else {set shwc 0 }
append data_shwo \t $shwo
append data_shwc \t $shwc


}

#write in data file based on HB with water only
puts $out_shwo "$resid \t $data_shwo"
puts $out_shwc "$resid \t $data_shwc"
set opp_shw [expr $op_shw * 1.0 / $nf + 0.01]
set clp_shw [expr $cl_shw * 1.0 / $nf + 0.01 ]
set pf_shw [expr $clp_shw * 1.0 / $opp_shw]
puts $out_shwpf "$resid $pf_shw "
puts $out_shwop "$resid $opp_shw"
puts $out_shwcp "$resid  $clp_shw"
puts $out_shwdG "$resid \t [expr {1.0 * log($pf_shw)}]"

#Loop to calculate total D uptake
foreach v2 $pf_shw {
set h_shw [expr { log("$v2") }]
if {$h_shw < 0} {
set hx_shw 1 
set hdx_shw [expr {$hdx_shw + $hx_shw }]
} else {set hx_shw 0}

}

}
#write D uptake output in a file with file name 
puts "$o_shwpf \t $hdx_shw \t [expr {100.0 * $hdx_shw / $l }]"
puts $out_hdx_shw "\n $o_shwpf \t $hdx_shw \t [expr {100.0 * $hdx_shw / $l }]"


#Close datafile to complete for sasa and HB with water
close $out_shwo
close $out_shwc
close $out_shwop
close $out_shwcp
close $out_shwpf
#Close all uptake file for four model
close $out_hdx_shw
close $out_shwdG
$selP delete
$selH delete
$selD delete
$selW delete

}

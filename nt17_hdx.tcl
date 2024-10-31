puts "Owner: Mohammad Azizur Rahman Jewel, Mertz Lab, Chemistry, WVU"
puts "Date: 03/25/2022 "
puts "Special direction-"
puts "Data Collection for HDX based on SASA"
puts "Each backbone NH vs probability of close and open state over trajectory"
puts "It will also collect date comprehensively for all open and close state as on off binary"
puts "usage: hdx-sasa <molid> <nf> <st> <rad> <chain>  <o_so.dat> <o_sc.dat> <o_sop.dat> <o_scp.dat> <o_spf.dat> <o_wo.dat> <o_wc.dat> <o_wop.dat> <o_wcp.dat> <o_wpf.dat> <o_shpo.dat> <o_shpc.dat> <o_shpop.dat> <o_shpcp.dat> <o_shppf.dat><o_shwo.dat> <o_shwc.dat> <o_shwop.dat> <o_shwcp.dat> <o_shwpf.dat> "


proc hdx-sasa {molid nf st rad distcutoff anglecutoff o_so o_sc o_sop o_scp o_spf o_wo o_wc o_wop o_wcp o_wpf o_shpo o_shpc o_shpop o_shpcp o_shppf o_shwo o_shwc o_shwop o_shwcp o_shwpf} {

#Set outfile for sasa based raw open, close, open_probability close_probability, protection factor

set out_so [open "$o_so" w]
set out_sc [open "$o_sc" w]
set out_sop [open "$o_sop" w]
set out_scp [open "$o_scp" w]
set out_spf [open "$o_spf" w]
#Set outfile for hbond with water based raw open, close, open_probability close_probability, protection factor

set out_wo [open "$o_wo" w]
set out_wc [open "$o_wc" w]
set out_wop [open "$o_wop" w]
set out_wcp [open "$o_wcp" w]
set out_wpf [open "$o_wpf" w]

#Set outfile for SASA hbond with protein Oxygen based raw open, close, open_probability close_probability, protection factor

set out_shpo [open "$o_shpo" w]
set out_shpc [open "$o_shpc" w]
set out_shpop [open "$o_shpop" w]
set out_shpcp [open "$o_shpcp" w]
set out_shppf [open "$o_shppf" w]
#Set outfile for hbond with water based raw open, close, open_probability close_probability, protection factor

set out_shwo [open "$o_shwo" w]
set out_shwc [open "$o_shwc" w]
set out_shwop [open "$o_shwop" w]
set out_shwcp [open "$o_shwcp" w]
set out_shwpf [open "$o_shwpf" w]
#get total number of frame
#set nf [molinfo $molid get numframes]
#setting for all backbone N as acceptor

set indexH {1 2 3 20 30 36 44 63 78 94 95 96 100 119 136 152 153 154 158 168 188 203 210 214 233 249 250 251 255 262 266}
set indexD {0 0 0 19 29 35 43 62 77 93 93 93 99 118 135 151 151 151 157 167 187 202 209 213 232 248 248 248 254 261 265}
#setting up for overall calculation
foreach x $indexH y $indexD {
set res [atomselect top "index $x"]
set resid [$res get resid]
$res delete

# Set initial parameter for protection factor calculation

set cl_s 0
set op_s 0
set cl_w 0
set op_w 0
set cl_shp 0
set op_shp 0
set cl_shw 0
set op_shw 0

#Set index as 
set data_so $y
set data_sc $y
set data_wo $y
set data_wc $y
set data_shpo $y
set data_shpc $y
set data_shwo $y
set data_shwc $y

#Atomselection for
set selP [atomselect $molid "protein"]
set selH [atomselect $molid "index $x"]
set selA [atomselect $molid "protein and name O"]
set selD [atomselect $molid "index $y"]
set selW [atomselect $molid "water and name OH2"]

#Loop through overall selected frame
	for {set i 1 } {$i < $nf } {incr i } {
	$selP frame $i
	$selH frame $i
	$selA frame $i
	$selD frame $i
	$selW frame $i
	$selP update
	$selH update
	$selA update
	$selD update
	$selW update
	set s [measure sasa $rad $selP -restrict $selH]
        set hbww [lindex [measure hbonds $distcutoff $anglecutoff $selD $selW] 1]
	set hbwp [lindex [measure hbonds $distcutoff $anglecutoff $selD $selA] 1]
	set n_hbww [llength $hbww]
	set n_hbwp [llength $hbwp]
#hdx calculation based on sasa only
	if {$s > $st} {
       		set so 1
         	set op_s [expr {$so + $op_s }]
	} else {set so 0}
        #finding total, that will be used to find fraction contact in simulated>
	if {$s<$st}  {
		set sc 1
		set cl_s [expr {$cl_s + $sc }]
		} else {set sc 0 }
append data_so \t $so
append data_sc \t $sc

#hdx calculation based on hb with water only
        if {$n_hbww >= 2} {
                set wo 1
                set op_w [expr {$wo + $op_w }]
        } else {set wo 0}
        #finding total, that will be used to find fraction contact in simulated>
        if {$n_hbww<2}  {
                set wc 1
                set cl_w [expr {$cl_w + $wc }]
                } else {set wc 0 }
append data_wo \t $wo
append data_wc \t $wc
#hdx calculation based on sasa and hb with protein only
        if {$s > $st && $n_hbwp <1} {
                set shpo 1
                set op_shp [expr {$shpo + $op_shp }]
        } else {set shpo 0}
        #finding total, that will be used to find fraction contact in simulated>
        if {$s<$st && $n_hbwp > 0}  {
                set shpc 1
                set cl_shp [expr {$cl_shp + $shpc }]
                } else {set shpc 0 }
append data_shpo \t $shpo
append data_shpc \t $shpc

#hdx calculation based on sasa and hb with water only
        if {$s > $st && $n_hbww >=2} {
                set shwo 1
                set op_shw [expr {$shwo + $op_shw }]
        } else {set shwo 0}
        #finding total, that will be used to find fraction contact in simulated>
        if {$s<$st && $n_hbww < 2}  {
                set shwc 1
                set cl_shw [expr {$cl_shw + $shwc }]
                } else {set shwc 0 }
append data_shpo \t $shwo
append data_shpc \t $shwc


}
#write in data file based on sasa only
puts $out_so "$resid \t $data_so"
puts $out_sc "$resid \t $data_sc"
set opp_s [expr $op_s *1.0 / $nf + 0.01]
set clp_s [expr $cl_s * 1.0 / $nf]
set pf_s [expr $clp_s * 1.0 / $opp_s]
puts $out_spf "$resid $pf_s "
puts $out_sop "$resid $opp_s"
puts $out_scp "$resid  $clp_s"

#write in data file based on HB with water only
puts $out_wo "$resid \t $data_wo"
puts $out_wc "$resid \t $data_wc"
set opp_w [expr $op_w * 1.0 / $nf + 0.01 ]
set clp_w [expr $cl_w * 1.0 / $nf ]
set pf_w [expr $clp_w * 1.0 / $opp_w]
puts $out_wpf "$resid $pf_w "
puts $out_wop "$resid $opp_w"
puts $out_wcp "$resid  $clp_w"

#write in data file based on sasa and HB with protein only
puts $out_shpo "$resid \t $data_shpo"
puts $out_shpc "$resid \t $data_shpc"
set opp_shp [expr $op_shp * 1.0 / $nf + 0.01 ]
set clp_shp [expr $cl_shp * 1.0 / $nf  ]
set pf_shp [expr $clp_shp * 1.0 / $opp_shp]
puts $out_shppf "$resid $pf_shp"
puts $out_shpop "$resid $opp_shp"
puts $out_shpcp "$resid  $clp_shp"

#write in data file based on HB with water only
puts $out_shwo "$resid \t $data_shwo"
puts $out_shwc "$resid \t $data_shwc"
set opp_shw [expr $op_shw * 1.0 / $nf + 0.01]
set clp_shw [expr $cl_shw * 1.0 / $nf ]
set pf_shw [expr $clp_shw * 1.0 / $opp_shw]
puts $out_shwpf "$resid $pf_shw "
puts $out_shwop "$resid $opp_shw"
puts $out_shwcp "$resid  $clp_shw"
}
#close datafile for sasa only system
close $out_so
close $out_sc
close $out_sop
close $out_scp
close $out_spf

#close datafile for water only
close $out_wo
close $out_wc
close $out_wop
close $out_wcp
close $out_wpf

#Close datafile for sasa and hb with protein only
close $out_shpo
close $out_shpc
close $out_shpop
close $out_shpcp
close $out_shppf

#Close datafile to complete for sasa and HB with water
close $out_shwo
close $out_shwc
close $out_shwop
close $out_shwcp
close $out_shwpf
$selP delete
$selH delete
$selA delete
$selD delete
$selW delete

}

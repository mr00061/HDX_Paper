puts "Owner: Mohammad Azizur Rahman Jewel, Chemistry, Mertz Lab WVU"
puts "Date: 01/16/2021 "
puts "Special direction-"
puts "use dcd for percent helicity distribution over simulation period"
puts "Usage: percenthelicity <molid> <selection><datafile.dat>"

proc percenthelicity {molid selection datafile} {


set outfile [open "$datafile" w]
set lookup {H G I}
set nf [molinfo $molid get numframes]
set all [atomselect top "$selection"]
set len [llength [$all get resid]]
$all delete


for {set i 0 } { $i < $nf} {incr i} {
	animate goto $i
	set sel [atomselect top "$selection"]
	mol ssrecalc top
	set struc_string [$sel get structure]
	set helix 0
	foreach ss $lookup {
		set temp [expr {[llength [split $struc_string $ss]]-1}]
		incr helix $temp
 		}
	set percent [expr {double($helix) / double($len) * 100}]
	set x [expr 1 * $i * 0.04]
	puts $outfile "$x \t $percent"
	$sel delete
} 
close $outfile

}

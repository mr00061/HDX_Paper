
puts "Owner: Mohammad Azizur Rahman Jewel, Chemistry, Mertz Lab WVU"
puts "Date: 12/18/2022 "
puts "Special direction-"
puts "use dcd for rmsd distribution over simulation period"
puts "Usage: rmsd <molid> <datafile.dat>"

proc rmsd {molid datafile} {


set outfile [open "$datafile" w];                                             
set nf [molinfo $molid get numframes]
set frame0 [atomselect $molid "protein and backbone and noh" frame 0]
set sel [atomselect $molid "protein and backbone and noh"]
# rmsd calculation loop
for {set i 1 } {$i < $nf } { incr i } {
    $sel frame $i
    $sel move [measure fit $sel $frame0]
    set t [expr 2* $i * 0.02]
    puts $outfile " $t   [measure rmsd $sel $frame0]"
}
close $outfile
}

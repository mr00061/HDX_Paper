puts "Owner: Mohammad Azizur Rahman Jewel, Chemistry, Mertz Lab WVU"
puts "Date: 12/18/2022 "
puts "Special direction-"
puts "use dcd for rmsd distribution over simulation period"
puts "Usage: rg <molid> <selection><datafile.dat>"

proc rg {molid selection datafile} {



set outfileA [open "$datafile" w]
set nf [molinfo top get numframes]
set frameA0 [atomselect top "$selection" frame 0]
set selA [atomselect top "$selection"]
# rmsd calculation loop
for {set i 1 } {$i < $nf } { incr i } {
    $selA frame $i
    #$selA move [measure fit $selA $frameA0]
    set xA [expr 2 * $i * 0.01]
   # set out [measure rmsd $sel $frame0]
    puts $outfileA " $xA       [measure rgyr $selA]"
}
close $outfileA
}

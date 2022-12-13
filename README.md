# gCodeParser_offset
This is a small python script to modify gcodes meant for FDM 3D-Printing, using [Andy Everitts gCode parser.](https://github.com/AndyEveritt/GcodeParser)
It offsets every second layer a bit to the side to decrease interlaminar and inter-layer voids, thus increasing strength in Z-Direction. 
If this proves to be useful, it should be communicated as an issue for commonly used slicers or branches of them.

**This only makes sense when using following settings:**
* 100% Infill
* Infill Pattern: Lines or monotonic
* Infill Direction: 90° (or whatever gives you lines only in y-direction)

## Instructions

Paste filepath instead of example filepath in line 5, change nozzle size in line 3 according to the one you are using.

Paste output in editor, save as .gcode

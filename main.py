from gcodeparser import GcodeParser

# open gcode file and store contents as variable
with open(r'C:\Users\alorenz\PycharmProjects\gCodeParser\100prozentcube.gcode', 'r') as f:
  gcode = f.read()

parsed_gcode = GcodeParser(gcode)
parsed_gcode.lines   # get parsed gcode lines
for line in parsed_gcode.lines:

  zstat=line.params.get('Z')
  if zstat != None:
    offset=1
  else:
    offset=0
 

  print(offset)

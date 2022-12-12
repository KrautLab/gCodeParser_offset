from gcodeparser import GcodeParser

# open gcode file and store contents as variable
with open(r'C:\Users\alorenz\PycharmProjects\gCodeParser\100prozentcube.gcode', 'r') as f:
  gcode = f.read()

parsed_gcode = GcodeParser(gcode)
parsed_gcode.lines   # get parsed gcode lines
offset=False
for line in parsed_gcode.lines:

  if line.params.get('Z') != None:
    switch=1
  else:
    switch=0

  if switch==1:
    offset = not offset

  print(offset)


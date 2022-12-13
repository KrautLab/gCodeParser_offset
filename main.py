from gcodeparser import GcodeParser
# user inputs
nozzle_size=0.4
# open gcode file and store contents as variable
with open(r'C:\Users\name\projects\example.gcode', 'r') as f:
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

  if line.params.get('X') != None:
    x_coord=float(line.get_param('X'))
    if offset == True:
      line.update_param('X', x_coord + nozzle_size * 0.5)

  print(line.gcode_str)


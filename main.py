from gcodeparser import GcodeParser

# open gcode file and store contents as variable
with open(r'C:\Users\alorenz\PycharmProjects\gCodeParser\100prozentcube.gcode', 'r') as f:
  gcode = f.read()

parsed_gcode = GcodeParser(gcode)
parsed_gcode.lines   # get parsed gcode lines
for line in parsed_gcode.lines:
  switch=True
  def toggle(switch):
    switch=not switch
  zstat=line.params.get('Z')
  if zstat != None:
    toggle()
    print(switch)

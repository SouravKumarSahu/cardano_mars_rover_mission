# cardano_mars_rover_mission
interview take home project

Execute mission :
python3 ExecuteLanding.py -i-text input.txt [-o-text output2.txt]

Execute Unittest cases:
python3 -m unittest -v

Text input file format :
4 5
2 2 N
L L M
3 2 E
R R M
4 6 S
M M R

Text output file format :
4 5
2 1 S
Successful - ()
2 2 W
Successful - ()
4 6 S
Await rescue - ()
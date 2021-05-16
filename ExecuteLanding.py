from typing import final
from RoverMission.Operations import Landing, Turning, Moving
from RoverMission.InputOutput import ReadInput, WriteOutput
from RoverMission.Objects import Rover, Mars
from RoverMission.Constants.Parameters import rotations
import sys
import os

cwd = os.getcwd()
sys.path.append(cwd)


def main():
    
    print("Welcome to Mars Mission")
    
    parms = sys.argv

    try:
        if parms[1] == '-i-text':
            input_file = parms[2]
    except Exception as e:
        print('Please provide proper parameters <ExecuteLanding.py -i-text inFile.txt [-o-text outFile.txt]>')
        exit()

    try:
        if parms[3] == '-o-text':
            output_file = parms[4]
    except Exception as e:
        output_file = 'output.txt'
    
    
    try:
        json = ReadInput.read_input_text(input_file)
        print(f'Instructions received from earth : \n{json}')
    except IOError:
        print(f'Input read error: make sure input is at {cwd}')

    try:
        mars_grid = Mars.Mars2DGrid(json['grid'][0],json['grid'][1]) 
    except TypeError as e:
        print(e)
    except Mars.MarsError as e:
        print(e)

    rovers = []

    for rover_num, instruction in enumerate(json['instructions'],start=1):
        try:
            rover = Rover.Rover(instruction[0][0],instruction[0][1],instruction[0][2])
        except TypeError as e:
            print(e)
        except Rover.RoverError as e:
            print(e)
        except Exception as e:
            print(e)
        else:
            rovers.append(rover)
        finally:
            print(f'Rover {rover_num} : \n- Initial orientation - {rover}')
        
        try:
            Landing.land_rover(rovers[-1],mars_grid)
        except Landing.LandingProhibited as e:
            rovers[-1].status = 'Await rescue'
            rovers[-1].message = e.__str__()
        except TypeError as e:
            rovers[-1].status = 'Await rescue'
            rovers[-1].message = e.__str__()
        except Exception as e:
            rovers[-1].status = 'Unknown error'
            rovers[-1].message = e.__str__()
        else:
            rovers[-1].status = 'Successful'
            rovers[-1].message = 'Rover landed successfully'
        finally:
            print(f'- {rovers[-1].status} : {rovers[-1].message}')
        
        if rovers[-1].status == 'Successful':
            for moves in instruction[1]:
                if moves in rotations[0:2]:
                    try:
                        Turning.change_direction(moves,rovers[-1])
                    except Turning.TurningError as e:
                        rovers[-1].status = 'Await rescue'
                        rovers[-1].message = e.__str__()
                    except TypeError as e:
                        rovers[-1].status = 'Await rescue'
                        rovers[-1].message = e.__str__()
                    except Exception as e:
                        rovers[-1].status = 'Unknown error'
                        rovers[-1].message = e.__str__()
                    else:
                        rovers[-1].status = 'Successful'
                        rovers[-1].message = 'Rover turn successful'
                    finally:
                        print(f'- {rovers[-1].status} : {rovers[-1].message}')
                        print(f'-- Tried turning to {moves} : latest orientation - {rover}')
                else:
                    try:
                        Moving.change_position(rovers[-1],mars_grid)
                    except Moving.MoveProhibited as e:
                        rovers[-1].status = 'Await rescue'
                        rovers[-1].message = e.__str__()
                    except TypeError as e:
                        rovers[-1].status = 'Await rescue'
                        rovers[-1].message = e.__str__()
                    except Exception as e:
                        rovers[-1].status = 'Unknown error'
                        rovers[-1].message = e.__str__()
                    else:
                        rovers[-1].status = 'Successful'
                        rovers[-1].message = 'Rover move successful'
                    finally:
                        print(f'- {rovers[-1].status} : {rovers[-1].message}')
                        print(f'-- Tried moving forward in {rovers[-1].d} : latest orientation - {rover}')

    print(mars_grid)

    
    try:
        WriteOutput.write_output_text(output_file,rovers,json)
        print(f'Output written to file : output.txt')
    except IOError:
        print(f'Input read error: make sure input is at {cwd}')
    


if __name__ == "__main__":
    main()

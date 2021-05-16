from rover_mission.operations import landing, turning, moving
from rover_mission.io import ReadInput, WriteOutput
from rover_mission.objects import mars
from rover_mission.objects.rover import Rover, RoverError
from rover_mission.constants.params import ROTATIONS
import sys
import os
import logging

cwd = os.getcwd()
sys.path.append(cwd)


def main():
       
    parms = sys.argv

    try:
        if parms[5] == '-o-log':
            log_file = parms[6]
    except Exception as e:
        log_file = 'log_output.txt'

    LOG_FORMAT = "%(asctime)s :: %(levelname)s :: %(message)s"
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
    logger = logging.getLogger()

    logger.info("Welcome to Mars Mission")

    try:
        if parms[1] == '-i-text':
            input_file = parms[2]
    except Exception as e:
        logger.error('Please provide proper parameters <ExecuteLanding.py -i-text inFile.txt [-o-text outFile.txt]>')
        exit()

    try:
        if parms[3] == '-o-text':
            output_file = parms[4]
    except Exception as e:
        output_file = 'output.txt'
  
    
    try:
        json = ReadInput.read_input_text(input_file)
        logger.info(f'Instructions received from earth : \n{json}')
    except IOError:
        logger.error(f'Input read error: make sure input is at {cwd}')

    try:
        mars_grid = mars.Mars2DGrid(json['grid'][0],json['grid'][1]) 
    except TypeError as e:
        logger.error(e)
    except mars.MarsError as e:
        logger.error(e)

    rovers = []

    for rover_num, instruction in enumerate(json['instructions'],start=1):
        try:
            rover = Rover(instruction[0][0],instruction[0][1],instruction[0][2])
        except TypeError as e:
            logger.error(e)
        except RoverError as e:
            logger.error(e)
        except Exception as e:
            logger.error(e)
        else:
            rovers.append(rover)
        finally:
            logger.info(f'Rover {rover_num} : Initial orientation - {rover}')
        
        try:
            landing.land_rover(rovers[-1],mars_grid)
        except landing.LandingProhibited as e:
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
            logger.info(f'- {rovers[-1].status} : {rovers[-1].message}')
        
        if rovers[-1].status == 'Successful':
            for moves in instruction[1]:
                if moves in ROTATIONS[0:2]:
                    try:
                        turning.change_direction(moves,rovers[-1])
                    except turning.TurningError as e:
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
                        logger.info(f'- {rovers[-1].status} : {rovers[-1].message}')
                        logger.info(f'-- Tried turning to {moves} : latest orientation - {rover}')
                else:
                    try:
                        moving.change_position(rovers[-1],mars_grid)
                    except moving.MoveProhibited as e:
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
                        logger.info(f'- {rovers[-1].status} : {rovers[-1].message}')
                        logger.info(f'-- Tried moving forward in {rovers[-1].d} : latest orientation - {rover}')

    logger.info(f'\n{mars_grid}')

    
    try:
        WriteOutput.write_output_text(output_file,rovers,json)
        logger.info(f'Output written to file : output.txt')
    except IOError:
        logger.error(f'Input read error: make sure input is at {cwd}')
    


if __name__ == "__main__":
    main()

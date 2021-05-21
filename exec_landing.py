from rover_mission.execute.execute_rovers import operate_rover, OperateException
from rover_mission.io import ReadInput, WriteOutput
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
    logging.basicConfig(filename=log_file, level=logging.DEBUG,
                        format=LOG_FORMAT, filemode='w')
    logger = logging.getLogger()

    logger.info("Welcome to Mars Mission")

    try:
        if parms[1] == '-i-text':
            input_file = parms[2]
            json_inst = ReadInput.read_input_text(input_file)
            logger.info(f'Instructions received from earth : \n{json_inst}')
    except IOError:
        logger.error(f'Input read error: make sure input is at {cwd}')
        exit()
    except Exception as e:
        logger.error(
            'Please provide proper parameters <ExecuteLanding.py -i-text inFile.txt [-o-text outFile.txt]>')
        exit()

    try:
        if parms[3] == '-o-text':
            output_file = parms[4]
    except Exception as e:
        output_file = 'output.txt'

    rovers = []
    try:
        rovers, mars_grid, json_output = operate_rover(json_inst)
        logger.info(f'\n{mars_grid}')
    except OperateException as e:
        logger.info(e)
    except Exception as e:
        logger.error(e)


    try:
        if len(rovers) > 0:
            WriteOutput.write_output_text(output_file, json_output)
            logger.info(f'Output written to file : output.txt')
    except IOError:
        logger.error(f'Input read error: make sure input is at {cwd}')


if __name__ == "__main__":
    main()

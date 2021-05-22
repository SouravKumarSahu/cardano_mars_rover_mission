import json
from rover_mission.operations import landing, turning, moving
from rover_mission.objects import mars
from rover_mission.objects.rover import Rover, RoverError
from rover_mission.constants.params import ROTATIONS


class OperateException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def operate_rover(json_inst):

    dict_input = json.loads(json_inst)

    rovers = []

    try:
        mars_grid = mars.Mars2DGrid(
            dict_input['grid'][0], dict_input['grid'][1])
    except TypeError as e:
        raise TypeError(e.__str__())
    except mars.MarsError as e:
        raise mars.MarsError(e.__str__())
    except Exception as e:
        raise OperateException(e.__str__())

    for rover_num, instruction in enumerate(dict_input['instructions'], start=1):

        try:
            rover = Rover(instruction[0][0],
                          instruction[0][1], instruction[0][2], rover_num)
        except TypeError as e:
            raise TypeError(e.__str__())
        except RoverError as e:
            raise RoverError(e.__str__())
        except Exception as e:
            raise OperateException(e.__str__())
        else:
            rovers.append(rover)

        try:
            landing.land_rover(rovers[-1], mars_grid)
        except (landing.LandingProhibited, TypeError) as e:
            rovers[-1].status = 'Await rescue'
            rovers[-1].message = e.__str__()
        except Exception as e:
            rovers[-1].status = 'Unknown error'
            rovers[-1].message = e.__str__()
        else:
            rovers[-1].status = 'Successful'
            rovers[-1].message = f'Rover {rovers[-1].id} landed successfully'

        if rovers[-1].status == 'Successful':
            for moves in instruction[1]:
                if moves in ROTATIONS[0:2]:
                    try:
                        turning.change_direction(moves, rovers[-1], mars_grid)
                    except (turning.TurningError, TypeError) as e:
                        rovers[-1].status = 'Await rescue'
                        rovers[-1].message = e.__str__()
                    except Exception as e:
                        rovers[-1].status = 'Unknown error'
                        rovers[-1].message = e.__str__()
                    else:
                        rovers[-1].status = 'Successful'
                        rovers[-1].message = f'Rover {rovers[-1].id} turn successful'
                else:
                    try:
                        moving.change_position(rovers[-1], mars_grid)
                    except (moving.MoveProhibited, TypeError) as e:
                        rovers[-1].status = 'Await rescue'
                        rovers[-1].message = e.__str__()
                    except Exception as e:
                        rovers[-1].status = 'Unknown error'
                        rovers[-1].message = e.__str__()
                    else:
                        rovers[-1].status = 'Successful'
                        rovers[-1].message = f'Rover {rovers[-1].id} move successful'

    dict_output = {}
    dict_output['grid'] = dict_input['grid']
    dict_output['rovers'] = []

    for rover in rovers:
        dict_output['rovers'].append(
            [rover.__str__(), str(f"{rover.status} - ({rover.message})")])

    json_output = json.dumps(dict_output)

    return rovers, mars_grid, json_output

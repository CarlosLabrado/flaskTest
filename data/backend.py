import yaml
import zerorpc
from random import random


class Setup(object):

    def write_to_yaml(self, new_id, new_connection_string):
        file_name = '/data/env_vars.yaml'

        stream = open(file_name, 'r')
        settings = yaml.load(stream)

        settings['azure']['id'] = int(new_id)  # we force casting to int
        settings['azure']['connection_string'] = new_connection_string
        settings['azure']['polling_rate'] = 10
        settings['on_boarding']['do_setup'] = 0
        with open(file_name, 'w') as yaml_file:
            yaml_file.write(yaml.safe_dump(settings, default_flow_style=False))
        print('setup: successful on boarding process')

    def get_dyna_point(self):
        data = [random() * 100, random() * 100]
        return data

    def get_status(self):
        status = {'well_status': 'On',
                  'automatic': 'Yes',
                  'percent_fillage': int(random() * 100),
                  'run_time': int(random() * 100),
                  'strokes_this': int(random() * 1000),
                  'strokes_last': int(random() * 10)}
        return status

    def get_settings(self):
        settings = {'pump_off_strokes': int(random() * 10),
                    'pump_up_strokes': int(random() * 10),
                    }
        return settings

    def update_settings(self, new_settings):
        print(new_settings)


s = zerorpc.Server(Setup())
s.bind("tcp://0.0.0.0:4242")
s.run()

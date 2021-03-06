import yaml
import zerorpc
from random import random
import arrow


class Setup(object):
    def write_to_yaml(self, new_id, new_connection_string):
        try:
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
        except Exception as e:
            print("write to yaml backend error {0}".format(e))

    def get_dyna_point(self):
        try:
            data = [random() * 100, random() * 100]
            return data
        except Exception as e:
            print("Get dyna point backend error {0}".format(e))

    def get_status(self):
        try:
            status = {'well_status': 'On',
                      'automatic': 'Yes',
                      'percent_fillage': int(random() * 100),
                      'run_time': int(random() * 100),
                      'strokes_this': int(random() * 1000),
                      'strokes_last': int(random() * 10)
                      }
            return status
        except Exception as e:
            print("Get status backend error {0}".format(e))

    def get_settings(self):
        try:
            utc = arrow.utcnow()
            local = utc.to('US/Central')

            settings = {'pump_off_strokes': int(random() * 10),
                        'pump_up_strokes': int(random() * 10),
                        'clock_date': local.format('YYYY-MM-DD'),
                        'clock_time': local.format('HH:mm'),
                        'fillage_setting': int(random() * 90),
                        'auto_time_out': True,
                        'time_out': "00:20"
                        }
            return settings
        except Exception as e:
            print("Get settings backend error {0}".format(e))

    def update_settings(self, new_settings):
        try:
            print(new_settings)
            from dbus_commands import DBUSCommands
            dbus_obj = DBUSCommands()
        except Exception as e:
            print("update settings backend error {0}".format(e))


s = zerorpc.Server(Setup())
s.bind("tcp://0.0.0.0:4242")
s.run()

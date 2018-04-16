import yaml
import zerorpc


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


s = zerorpc.Server(Setup())
s.bind("tcp://0.0.0.0:4242")
s.run()
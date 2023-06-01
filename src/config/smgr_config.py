
import ruamel.yaml as yaml
import os

class Config(object):
    
    def __init__(self, yaml_config_file):
        with open(yaml_config_file) as stream:
            try:
                yaml_config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        self.CFG_APPNAME = "SCORES-MANAGER-UI-PYSIDE"
        self.CFG_APPSHORTNAME = yaml_config['appShortName']

        assert self.CFG_APPNAME == yaml_config['appName']

        self.CFG_WORKING_PATH = yaml_config['paths']['workingpath']

        if not os.path.exists(self.CFG_WORKING_PATH):
            os.makedirs(self.CFG_WORKING_PATH)


if __name__ == '__main__':

    config = Config(r"src\config\smgr_config.yaml")
    print(config.CFG_APPSHORTNAME)
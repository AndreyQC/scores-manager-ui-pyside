
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

        self.PG_DB_HOST = yaml_config['databases']['postgres']['host']
        self.PG_DB_PORT = yaml_config['databases']['postgres']['port']
        self.PG_DB_SSLMODE = yaml_config['databases']['postgres']['sslmode']
        self.PG_DB_DBNAME = yaml_config['databases']['postgres']['dbname']
        self.PG_DB_USER = yaml_config['databases']['postgres']['user']
        self.PG_DB_TARGET_SESSION_ATTRS = yaml_config['databases']['postgres']['target_session_attrs']
        self.PG_DB_PWD = os.environ[yaml_config['databases']['postgres']['password']] 
        self.PG_DB_CONNECTION_STRING = f"""
            host={self.PG_DB_HOST}
            port={self.PG_DB_PORT}
            sslmode={self.PG_DB_SSLMODE}
            dbname={self.PG_DB_DBNAME}
            user={self.PG_DB_USER}
            password={self.PG_DB_PWD}
            target_session_attrs={self.PG_DB_TARGET_SESSION_ATTRS}
            """

if __name__ == '__main__':

    config = Config(r"src\config\smgr_config.yaml")
    print(config.CFG_APPSHORTNAME)
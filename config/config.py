import ConfigParser


class Config:
    config_parser = None

    def __init__(self):
        self.config_parser = ConfigParser.RawConfigParser()
        config_file = 'config/config.ini'
        self.config_parser.read(config_file)

    def get_key(self, section, key):
        return self.config_parser.get(section, key)

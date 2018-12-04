import ConfigParser
import os


def config():
    cfg = ConfigParser.ConfigParser()
    cfg.read(os.path.dirname(os.path.abspath(__file__)) + "/config/config.cfg")
    return cfg
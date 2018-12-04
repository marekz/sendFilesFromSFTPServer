import re
from config import config

class ParseFileName():
    def __init__(self, file):
        self.file = file

    def parseFileName(self):
        folder_name = config().get('local_settings','local_dir') + '/'
        separator = config().get('local_settings','mpk_file_name_separator')
        file_name = re.sub(folder_name, '', self.file)
        mpk_name = file_name.split(separator)[0]
        return mpk_name

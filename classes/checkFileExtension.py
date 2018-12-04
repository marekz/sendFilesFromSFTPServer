import re


class CheckExtension():
    def __init__(self, file):
        self.file = file

    def check_extension(self):
        if re.search('.pdf', self.file, flags=re.IGNORECASE):
            return True
        else:
            return False
from config import config
from os import remove
from time import time


class MoveArchiveFile():
    def __init__(self, file, sftp):
        self.file = file
        self.sftp_c = sftp
        self.archive_folder = config().get('sftp_connection','sftp_output_dir')
        self.archive_folder_check()

    def archive_folder_check(self):
        if(self.sftp_c.exists(self.archive_folder)):
            self.move_file_to_archive()
        else:
            self.create_folder()
        return True

    def create_folder(self):
        print "Create folder"
        self.sftp_c.mkdir(self.archive_folder, mode=755)
        self.move_file_to_archive()
        return True

    def move_file_to_archive(self):
        ts = time()
        local_file = config().get('local_settings','local_dir') + '/' + self.file
        remote_file_arch = config().get('sftp_connection', 'sftp_output_dir') + str(ts) + "_"+ self.file
        self.sftp_c.put(local_file, remotepath=remote_file_arch, callback=None, confirm=True,
            preserve_mtime=True)
        self.sftp_c.remove(self.file)
        remove(local_file)

        return True

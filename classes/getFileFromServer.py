from config import config


class GetFileFromServer():
    def __init__(self, sftpConnection, file):
        self.sftpConnection = sftpConnection
        self.remote_path = config().get('sftp_connection','sftp_input_dir')
        self.local_path = config().get('local_settings', 'local_dir')
        self.full_remote_path = self.remote_path + '/' + file
        self.full_local_path = self.local_path + '/' + file

    def getFile(self):
        sftpServer = self.sftpConnection
        sftpServer.get(self.full_remote_path, localpath=self.full_local_path, preserve_mtime=True)
        return self.full_local_path
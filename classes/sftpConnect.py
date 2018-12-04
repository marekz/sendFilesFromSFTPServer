import pysftp


class SFTPConnect():
    def __init__(self, config):
        self.username = config.get("sftp_connection", "sftp_login")
        self.host = config.get("sftp_connection", "sftp_host")
        self.input_dir = config.get("sftp_connection", "sftp_input_dir")
        self.output_dir = config.get("sftp_connection", "sftp_output_dir")
        self.private_key = config.get("sftp_connection", "sftp_key_path")

    def connect_to_sftp(self):
        return pysftp.Connection(self.host, username=self.username, private_key=self.private_key,
                 port=22, default_path=self.input_dir)
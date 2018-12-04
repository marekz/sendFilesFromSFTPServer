from classes.sftpConnect import SFTPConnect
from config import config
from classes.processFiles import ProcessFiles

sftpConn = SFTPConnect(config())
sftpConnection = sftpConn.connect_to_sftp()
listFiles =  sftpConnection.listdir()

processFiles = ProcessFiles(listFiles, sftpConnection)
processFiles.processFiles()

from classes.getFileFromServer import GetFileFromServer
from classes.executeOperationOnFile import ExecuteFile
from classes.moveFileToArchive import MoveArchiveFile
from classes.checkFileExtension import CheckExtension

class ProcessFiles():
    def __init__(self, files, sftp_connection):
        self.files = files
        self.sftp_connection = sftp_connection

    def processFiles(self):
        for file in self.files:
            check_extension = CheckExtension(file)
            isAcceptedExtension = check_extension.check_extension()

            if (self.sftp_connection.isfile(file) and isAcceptedExtension):
                getFile = GetFileFromServer(self.sftp_connection, file)
                importedFile = getFile.getFile()
                executeFile = ExecuteFile(importedFile)
                executeFileStatus = executeFile.sendMailToMpk()
                moveFileToArchive = MoveArchiveFile(file, self.sftp_connection)

        return True
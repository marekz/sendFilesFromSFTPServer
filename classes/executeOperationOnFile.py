import re
from config import config
from classes.parseFileName import ParseFileName
import os
import os.path
import base64
import mimetypes
import smtplib
from config import config
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

class ExecuteFile():
    def __init__(self, file):
        self.file = file
        self.mail_host = config().get('mail_config', 'mail_host')
        self.mail_user = config().get('mail_config','mail_user')
        self.mail_from = config().get('mail_config','mail_from')
        self.mail_pass = config().get('mail_config','mail_pass')
        self.domain = config().get('mail_config','mail_user_domain')
        self.subject = config().get('mail_config','mail_subject')
        self.content = config().get('mail_config','mail_content')
        self.port = config().get('mail_config','mail_smtp_port_tls')
        self.tmp_folder = config().get('local_settings','local_dir') + '/'

    def sendMailToMpk(self):
        parsedName = ParseFileName(self.file)
        mpk = parsedName.parseFileName()
        fileName = re.sub(self.tmp_folder, '', self.file)

        if len(mpk) == 4:
            mpk = str(0) + mpk

        print "Execute: " + fileName + ' - ' + mpk

        msg = MIMEMultipart()
        msg['Subject'] = self.subject

        msg['From'] = self.mail_user
        msg.preamble = 'Send attachment test'

        fp = open(self.file, 'rb')
        csv = MIMEBase('application','octet-stream')
        csv.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(csv)
        csv.add_header('Content-Disposition', 'attachment', filename=fileName)

        toaddr = mpk + config().get('mail_config','mail_user_domain')

        msg.attach(csv)

        server = smtplib.SMTP(self.mail_host, self.port)
        server.ehlo()
        server.login(self.mail_user, self.mail_pass)
        server.sendmail(self.mail_from, toaddr, msg.as_string())
        server.close()
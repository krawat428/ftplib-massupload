import ftplib
import os


directory=''
host=''
username=''
password=''


command1='ls {x1}'.format(x1=directory)
os.chdir(dire)


a=os.popen(command1).read()
b=a.split()
ftp = ftplib.FTP(host,username,password)
for i in b:
	ftp.storbinary('STOR {x}'.format(x=i), open(i, 'rb'))
ftp.quit()

# If files are large or uploading process will consume much time, Please execute the script as a background process.

#nohup python ftp.py &

import requests
import xlwt
import  smtplib
from os.path import basename
from email.mime.application  import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


Base_url="https://remoteok.com/api/"
User_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
REQUEST_header={
    'user-agent': User_agent,
    'Accept-Langage':'ens-US ,  en;q=0.5',

}



def getjobremote():
    res=requests.get(url=Base_url  ,headers=  REQUEST_header)
    return  res.json()

if __name__ == "__main__":

    json=  getjobremote()[1]
    print(json)

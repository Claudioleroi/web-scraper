import requests
import xlwt
from xlwt import Workbook
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
def  getjob_xls(data):
    wb=Workbook()
    job_sheet=wb.add_sheet('job')
    headers=list(data[0].keys())
    for i in range(0 ,len(headers)):

        job_sheet.write(0,i,headers[i])

    for  i  in range(0,len(data)):
       job=data[i]
       values=list(job.values())
       for  x in range  (0, len(values)):
            job_sheet.write(i+1, x , values[x])

    wb.save('job_sheet_remote.xls')


def getjobremote():
    res=requests.get(url=Base_url  ,headers=  REQUEST_header)
    return  res.json()

if __name__ == "__main__":

    json=  getjobremote()[1:]
    getjob_xls(json)

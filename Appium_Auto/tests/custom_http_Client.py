'''
Created on Aug 13, 2018

@author: sysadmin
'''


# importing the requests library
import requests
import datetime
# defining the api-endpoint 
def sendReq(topicName,message):
    API_ENDPOINT = "http://192.168.1.3:8080/vauto/vauto/kafkaProducer"
    
    # your API key here
    API_KEY = "XXXXXXXXXXXXXXXXX"
    now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



    # data to be sent to api
    if(type(message) is str):
    
        data = {"topicName":topicName,"message":"INFO:  "+now+'::  '+message}
    elif(type(message) is list):
        data = {"topicName":topicName,"message":"INFO:  "+now+'::  '+'\n'.join(str(v) for v in message)}
        
    
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, json=data ,headers = {'Content-type': 'application/json'})
    
    # extracting response text 
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)
def get_appium_server_logs(sessionId):
    API_ENDPOINT = 'http://localhost:4723/wd/hub/session/'+sessionId+'/log'
    
    print 'sessionId::'+API_ENDPOINT
    r=requests.post(API_ENDPOINT,json={"type":"driver"})
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)

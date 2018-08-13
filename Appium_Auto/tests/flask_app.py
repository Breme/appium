'''
Created on Aug 13, 2018

@author: sysadmin
'''
from flask import Flask,request #import main Flask class and request object
import json
import unittest
from appium import webdriver
import time
import sys
import traceback
from appium.webdriver.common.touch_action import TouchAction
import httplib, urllib
import json
headers = {"Content-type": "application/json"}
conn = httplib.HTTPConnection("192.168.1.3",8080)
app = Flask(__name__) #create the Flask app
import custom_http_Client
@app.route('/query-example')
def query_example():
    return 'Todo...'
@app.route('/LGI_Android_Automation/openurl', methods=['POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        data=request.get_json()
        print request.get_json()
        desired_caps = {}
        desired_caps['browserName']=data['browserName']
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']

        try:

            driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)
            driver.get(data['url'])
            time.sleep(10)
            driver.close()
            driver.quit()

        except:
            print('Some Problem in Login')
            driver.quit()
            return json.dumps({"RESULT":"1"})


        return json.dumps({"RESULT":"0"})

@app.route('/LGI_Android_Automation/playVideo', methods=['POST']) #allow both GET and POST requests
def playVideo():
    if request.method == 'POST': #this block is only entered when the form is submitted
        data=request.get_json()
        
        desired_caps = {}
        desired_caps['browserName']=data['browserName']
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']

        try:
            print data['searchPharse']
            driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)
            driver.get(data['url'])
            driver.find_element_by_xpath('//*[@id="app"]/ytm-header-bar/header/div/div/button').click()
            driver.implicitly_wait(15000)
            driver.find_element_by_xpath('//*[@id="app"]/ytm-header-bar/header/ytm-searchbox/form/div[1]/input').send_keys(data['searchPharse'])
            driver.implicitly_wait(15000)
            driver.find_element_by_xpath('//*[@id="app"]/ytm-header-bar/header/ytm-searchbox/form/div[1]/input').submit()
            driver.implicitly_wait(10000)
            driver.find_element_by_xpath('//*[@id="app"]/div[3]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[1]/div/a/div/img').click()
            driver.implicitly_wait(10000)
       
            # driver.find_element_by_xpath('//*[@id="sdppromo"]/div/div[4]/div[2]/a').click()
            time.sleep(15)
            driver.close()
            driver.quit()

        except Exception,e:
            print('Some Problem in Login',str(e))
            driver.quit()
            return json.dumps({"RESULT":"1"})


        return json.dumps({"RESULT":"0"})
@app.route('/LGI_Android_Automation/readMail', methods=['POST']) #allow both GET and POST requests
def readMail():
    if request.method == 'POST': #this block is only entered when the form is submitted
        data=request.get_json()
        
        desired_caps = {}

        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        try:

            driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)

            driver.tap([(298,1022),(423,1178)])
            time.sleep(5)
            driver.tap([(298,1022),(423,1178)])
            time.sleep(8)
            driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Liberty global")').click()
            time.sleep(7)
            driver.quit()

        except:
            print('Some Problem in Login')
            driver.quit()
            return json.dumps({"RESULT":"1"})


        return json.dumps({"RESULT":"0"})
@app.route('/LGI_Android_Automation/composeMail', methods=['POST']) #allow both GET and POST requests
def composeMail():
    if request.method == 'POST': #this block is only entered when the form is submitted
        data=request.get_json()
        print data
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        try:

            driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)

            driver.tap([(298,1022),(423,1178)])
            time.sleep(5)
            driver.tap([(298,1022),(423,1178)])

            time.sleep(5)
            driver.tap([(576,1040),(668,1152)])
            time.sleep(10)
            driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.google.android.gm:id/to")').send_keys(data['toAddress'])
            driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.google.android.gm:id/subject")').send_keys(data['subject'])
            driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Compose email")').send_keys(data['mailBody'])
            driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.google.android.gm:id/send")').click()
            time.sleep(5)
            driver.quit()

        except:
            print('Some Problem in Login')
            driver.quit()
            return json.dumps({"RESULT":"1"})


        return json.dumps({"RESULT":"0"})
@app.route('/LGI_Android_Automation/youtubeFastForward', methods=['POST']) #allow both GET and POST requests
def youtubeSeekbarFastForward():
    if request.method == 'POST': #this block is only entered when the form is submitted
        data=request.get_json()
        print data
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['youtubeAppPackage']
        desired_caps['appActivity'] = data['youtubeActivity']

        try:

            
            custom_http_Client.sendReq(data["topicName"],"Connecting to appium driver")
            driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)
            custom_http_Client.sendReq(data["topicName"],"Connected to appium driver")
            print 'waiting'
            driver.implicitly_wait(10)
            custom_http_Client.sendReq(data["topicName"],"Finding Search Element...")
            driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Search']").click()
            print 'element crossed'
            driver.implicitly_wait(10)
            searchPhrase=driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.google.android.youtube:id/search_edit_text']")
            searchPhrase.send_keys(data['searchPhrase'])
            driver.implicitly_wait(10)
            driver.long_press_keycode(66)
            # time.sleep(10)
            custom_http_Client.sendReq(data["topicName"],"Clicking target Video..")
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'LGI Winner')]").click()
            # time.sleep(10)
            driver.implicitly_wait(10)
            custom_http_Client.sendReq(data["topicName"],"Finding Seekbar...")
            seekbar=driver.find_element_by_xpath('//android.widget.SeekBar')
            
            print seekbar.location
            seelLoc=seekbar.location
            seekX=int(seelLoc['x'])
            seekY=int(seelLoc['y'])
            seekMoveTo=seekbar.size
            print 'width::',type(seekbar)
            progress_bar=driver.find_elements_by_xpath('//android.widget.ProgressBar').count > 0
            while(progress_bar==False):
                progress_bar=driver.find_elements_by_xpath('//android.widget.ProgressBar').count > 0
            seekbar.click()
            custom_http_Client.sendReq(data["topicName"],"Fast Forward with seekBar..")
            TouchAction(driver=driver).long_press(None,18,451).move_to(None,200, 451).release().perform()
            custom_http_Client.sendReq(data["topicName"],"Test Success")
            driver.quit()

        except Exception,e:
            print('Some Problem in Login')
            custom_http_Client.sendReq(data["topicName"],"Error"+str(e.message))
            traceback.print_exc()
            driver.quit()
            return json.dumps({"RESULT":"1"})


        return json.dumps({"RESULT":"0"})
@app.route('/LGI_Android_Automation/filesRearrange', methods=['POST']) #allow both GET and POST requests
def filesRearrange():
    if request.method == 'POST': #this block is only entered when the form is submitted
        
        # data=request.get_json()
        # print data
        # desired_caps = {}
        # desired_caps['platformName'] = data['platformName']
        # desired_caps['platformVersion'] = data['platformVersion']
        # desired_caps['deviceName'] = data['deviceName']
        # desired_caps['appPackage'] = data['googleMusicPackage']
        # desired_caps['appActivity'] = data['googleMusicActivity']

        try:
            data=request.get_json()
            print data
            desired_caps = {}
            desired_caps['platformName'] = data['platformName']
            desired_caps['platformVersion'] = data['platformVersion']
            desired_caps['deviceName'] = data['deviceName']
            desired_caps['appPackage'] = data['googleMusicPackage']
            desired_caps['appActivity'] = data['googleMusicActivity']

            
            # custom_http_Client.sendReq(data["topicName"],"Connecting to appium driver")
            driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)
            # custom_http_Client.sendReq(data["topicName"],"Connected to appium driver")
            driver.implicitly_wait(10)
            time.sleep(10)
            # custom_http_Client.sendReq(data["topicName"],"Skipping App Advertisements...")
            driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.google.android.music:id/btn_decline']").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.google.android.music:id/btn_skip']").click()
            driver.implicitly_wait(10)
            # driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.google.android.music:id/button_0']").click()
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.google.android.music:id/navigation_button']").click()
            # custom_http_Client.sendReq(data["topicName"],"Selecting Music Library..")
            driver.implicitly_wait(10)
            driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,744][640,840]' and @text='Music library' and @index='6']").click()
            # driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.google.android.music:id/li_subtitle']").click()
            driver.implicitly_wait(10)
            # custom_http_Client.sendReq(data["topicName"],"Selecting Playlist...")
            driver.find_element_by_xpath("//android.widget.TextView[@text='PLAYLISTS']").click()
            driver.implicitly_wait(10)
            # custom_http_Client.sendReq(data["topicName"],"Scrolling to select Playlist..")
            scroll_element=driver.find_element_by_xpath("//android.widget.TextView[@text='Auto-Playlists']")
            scroll_till_element=driver.find_element_by_xpath("//android.widget.TextView[@text='All Playlists']")
            actions = TouchAction(driver)

            scroll_element_location=scroll_element.location
            scroll_till_element_X=scroll_element_location['x']
            scroll_till_element_Y=scroll_element_location['y']

            scroll_till_element_location=scroll_till_element.location
            scroll_element_X=scroll_till_element_location['x']
            scroll_element_Y=scroll_till_element_location['y']
            # From Element
            driver.swipe(scroll_element_X, scroll_element_Y, scroll_till_element_X, scroll_till_element_Y,2000 )

            driver.implicitly_wait(10)
            # custom_http_Client.sendReq(data["topicName"],"Selecting My Playlist..")
            driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.google.android.music:id/li_thumbnail_frame' and @bounds='[24,743][352,1071]']").click()
            driver.implicitly_wait(10)
            my_playlist_scroll=driver.find_element_by_xpath("//android.widget.TextView[@text='My playist']")
            my_playlist_scroll_location=my_playlist_scroll.location
            driver.swipe(my_playlist_scroll_location['x'], my_playlist_scroll_location['y'], 150, 240, 2000)
            # driver.find_element_by_xpath("//android.widget.TextView[@text='Top charts']")
            rearrange_song1_element=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.google.android.music:id/li_title' and @text='Me and My Shadow (feat. Zooey Deschanel)']")
            rearrange_song2_element=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.google.android.music:id/li_title' and @text='Exclusive Ninja Tune Mix']")
            # custom_http_Client.sendReq(data["topicName"],"Swapping Files...")
            # From Element
            rearrange_song1_element_location=rearrange_song1_element.location
            rearrange_element_X=int(rearrange_song1_element_location['x'])
            rearrange_element_y=int(rearrange_song1_element_location['y'])
            # To Element
            rearrange_song2_element_location=rearrange_song2_element.location
            rearrange_element_2_X=int(rearrange_song2_element_location['x'])
            rearrange_element_2_y=int(rearrange_song2_element_location['y'])

            TouchAction(driver=driver).long_press(rearrange_song1_element,rearrange_element_X,rearrange_element_y).move_to(rearrange_song2_element,200, 451).release().perform()
            driver.implicitly_wait(10)
            logs = driver.get_log("server")
            print type(logs)
            sess_id=driver.session_id
            # custom_http_Client.get_appium_server_logs(sess_id)
            driver.quit()
            # custom_http_Client.sendReq(data["topicName"],logs)
    
  

        except:
            print('Some Problem in Login')
            traceback.print_exc()
            driver.quit()
            return json.dumps({"RESULT":"1"})


        return json.dumps({"RESULT":"0"})

if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.9' ,port=5000) 
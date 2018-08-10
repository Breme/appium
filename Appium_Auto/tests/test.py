'''
Created on Aug 9, 2018

@author: sysadmin
'''



from appium import webdriver
import traceback
import time
from uiautomator import Device
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['appPackage'] = 'com.google.android.music'
desired_caps['appActivity'] = 'com.android.music.activitymanagement.TopLevelActivity'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'

try:

    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities=desired_caps)
    print 'waiting'
    driver.implicitly_wait(15)
    


    
    
    
    # driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.google.android.music:id/btn_decline']").click()
    
#     print('----------------------------',elem1.get_attribute
    for attempt in range(3):
        try:
    # do thing
            print 'hi'
        except:
            pass
    # perhaps reconnect, etc.
        else:
            break
    else:
        print 'hey'
    def findElementByText(element_className,element_text):
#         textElement=driver.find_element_by_xpath("//android.widget.Button[@text='Got it']")
        textElement=driver.find_element_by_xpath("//"+element_className+"[contains(@text,"+element_text+")]")
        print "//"+element_className+"[contains(@text,"+element_text+")]"
        
        print('----------------------------',dir(textElement))
        print('----------------------------',textElement.text)
        print('----------------------------',textElement.id)
        print('----------------------------',textElement.__class__)
        print('----------------------------',textElement.is_enabled())
        print('----------------------------',textElement.tag_name)
        print('----------------------------',textElement.rect)
        print('----------------------------',textElement.parent)
        print('----------------------------',textElement.get_property)
        return textElement
    def getAllElementDetails(elem1):
        elementJson={}
        elementJson["resourceId"] =elem1.get_attribute("resourceId")
        elementJson["text"]= elem1.get_attribute("text")
        elementJson["className"] =elem1.get_attribute("className")
#         elementJson["package"]=driver.current_package()
        elementJson["contentDesc"]=elem1.get_attribute("contentDescription")
        elementJson["enabled"]=elem1.get_attribute("enabled")
        elementJson["checkable"]=elem1.get_attribute("checkable")
        elementJson["checked"]=elem1.get_attribute("checked")
        elementJson["clickable"]=elem1.get_attribute("clickable")
        elementJson["focusable"]=elem1.get_attribute("focusable")
        elementJson["focused"]=elem1.get_attribute("focused")
        elementJson["scrollable"]=elem1.get_attribute("scrollable")
        elementJson["selected"]=elem1.get_attribute("selected")
        elementJson["displayed"]=elem1.get_attribute("displayed")
        elementJson["longClickable"]=elem1.get_attribute("longClickable")
     
        return elementJson
    print getAllElementDetails(findElementByText("android.widget.Button",u'Got'))
    
    
    
    # print d(text=elem.text).exists 
    # print d(text='Got it').exists 
    # if(d(text=elem.text).exists ):
    #     print 'Yes'
    #     print d(text=elem.text).info
    # print 'out'
    driver.implicitly_wait(15)
    # driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.google.android.music:id/btn_skip']").click()
    # driver.implicitly_wait(10)
    # # driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.google.android.music:id/button_0']").click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.google.android.music:id/navigation_button']").click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath("//android.widget.TextView[@bounds='[0,744][640,840]' and @text='Music library' and @index='6']").click()
    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='PLAYLISTS']").click()
    # driver.implicitly_wait(10)
    # scroll_element=driver.find_element_by_xpath("//android.widget.TextView[@text='Auto-Playlists']")
    # scroll_till_element=driver.find_element_by_xpath("//android.widget.TextView[@text='All Playlists']")
    # actions = TouchAction(driver)

    # scroll_element_location=scroll_element.location
    # scroll_till_element_X=scroll_element_location['x']
    # scroll_till_element_Y=scroll_element_location['y']

    # scroll_till_element_location=scroll_till_element.location
    # scroll_element_X=scroll_till_element_location['x']
    # scroll_element_Y=scroll_till_element_location['y']
    # # From Element
    # driver.swipe(scroll_element_X, scroll_element_Y, scroll_till_element_X, scroll_till_element_Y,2000 )

    # driver.implicitly_wait(10)
    # driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.google.android.music:id/li_thumbnail_frame' and @bounds='[24,743][352,1071]']").click()
    # driver.implicitly_wait(10)
    # my_playlist_scroll=driver.find_element_by_xpath("//android.widget.TextView[@text='My playist']")
    # my_playlist_scroll_location=my_playlist_scroll.location
    # driver.swipe(my_playlist_scroll_location['x'], my_playlist_scroll_location['y'], 150, 240, 2000)

    # rearrange_song1_element=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.google.android.music:id/li_title' and @text='Me and My Shadow (feat. Zooey Deschanel)']")
    # rearrange_song2_element=driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.google.android.music:id/li_title' and @text='Exclusive Ninja Tune Mix']")
   
    # # From Element
    # rearrange_song1_element_location=rearrange_song1_element.location
    # rearrange_element_X=int(rearrange_song1_element_location['x'])
    # rearrange_element_y=int(rearrange_song1_element_location['y'])
    # # To Element
    # rearrange_song2_element_location=rearrange_song2_element.location
    # rearrange_element_2_X=int(rearrange_song2_element_location['x'])
    # rearrange_element_2_y=int(rearrange_song2_element_location['y'])

    # TouchAction(driver=driver).long_press(rearrange_song1_element,rearrange_element_X,rearrange_element_y).move_to(rearrange_song2_element,200, 451).release().perform()
    # driver.implicitly_wait(10)
    # driver.quit()
    time.sleep(10)
    driver.quit()
    def elementCheck(element):
        print 'hi'
  
    
except Exception,e:
    print  traceback.print_exc();
    driver.quit()
    
   
    print('Some Problem in Login',str(e))


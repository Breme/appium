'''
Created on Aug 13, 2018

@author: sysadmin
'''

from pymongo import MongoClient



mng_client = MongoClient('mongodb://localhost:27017')
mng_db = mng_client['Appium_Auto'];
def create_Regression(regId):
    print 'Inside create regression'
    regJson = {}
    
    regJson['regId'] = regId
    regJson['testcases'] = []
    
    mng_db.APPIUM_TC_DETAILS.insert(regJson)
    mng_client.close()
    print 'Regression Created'
def insert_testcase(regId,testId, testcaseName):
    print 'Inside insert testcase'
    tcJson = {}
    tcJson['elements'] = []
    tcJson['testcaseName'] = testcaseName
    tcJson['testId'] = testId
    tcJson['description'] = 'test'
    
    mng_db.APPIUM_TC_DETAILS.update({"regId":regId},{"$push":{"testcases":tcJson}},True)
    
    mng_client.close()
    print 'Testcase Inserted'
def insert_element_data(regId,testId, testcaseName,testElementJson):
    

    
#     mng_db.APPIUM_TC_DETAILS.update({"regId":regId},{"$push":{"elements":testElementJson}},True)
    mng_db.APPIUM_TC_DETAILS.update({"regId":regId, "testcases.testId":testId},{"$push":{"testcases.$.elements":testElementJson}},True)
    mng_client.close()
    print 'Testcase Inserted'
# create_Regression('1000')
# insert_testcase('1000','100', 'clickButton')
# insert_testcase('1000','101', 'dragitem')

def main():
    pass
if __name__ == "__main__":
    create_Regression('1000')
    insert_testcase('1000','100', 'clickButton')
    insert_testcase('1000','101', 'dragitem')
    main()

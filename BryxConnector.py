import json
import time
from selenium import webdriver
import requests
import base64


def getCallData(token):
    request = requests.get('https://bryx911.com/api/2.2/calls?department=us.ny.monroe.chif',
                     headers={'X-AUTH-TOKEN':token,
                          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                          'Referer':'https://bryx911.com/dashboard',
                          'Host':'bryx911.com'})
    if request.status_code == 401:
        return ''
    elif request.status_code == 200:
        parsed = json.loads(request.content)
        return parsed
    else:
        print('Unexpected Status Code')
        return


def getToken(config):
    wd = webdriver.Firefox()
    wd.get('https://bryx911.com/signin')
    wd.implicitly_wait(15)
    wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/form/div[1]/div/input").send_keys(config.bryxusername)
    wd.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div/form/div[2]/div/input").send_keys(config.bryxpassword)
    wd.find_element_by_xpath("//*[@id=\"SigninButton\"]").click()
    time.sleep(5)
    api = wd.execute_script('return window.localStorage.getItem("com.bryx.account.apiKey");')
    id = wd.execute_script('return window.localStorage.getItem("com.bryx.account.id");')
    wd.close()
    tokenBinary = base64.b64encode(bytes('{"key":'+api+',"id":'+id+'}', 'utf-8'))
    token = tokenBinary.decode("utf-8")
    return token


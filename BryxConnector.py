import json
import time
from selenium import webdriver
import requests


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
    wd.get('https://bryx911.com')
    wd.implicitly_wait(15)
    test = wd.find_element_by_id('navbar-signin.email').send_keys(config.bryxusername)
    wd.find_element_by_id('navbar-signin.password').send_keys(config.bryxpassword)
    wd.find_element_by_xpath(
        "/html/body/section/div/div/div[1]/div[2]/div/div[1]/form/div[4]/div/div[2]/button").click()
    time.sleep(5)
    token = wd.execute_script('return window.localStorage.getItem("authToken");')
    wd.close()
    return token


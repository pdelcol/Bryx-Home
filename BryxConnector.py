import urllib3
import json

def getCallData(token):
    http = urllib3.PoolManager()
    urllib3.disable_warnings()
    r = http.request('GET','https://bryx911.com/api/2.2/calls?department=us.ny.monroe.chif',
                     headers={'X-AUTH-TOKEN':token,
                          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                          'Referer':'https://bryx911.com/dashboard',
                          'Host':'bryx911.com'})
    parsed = json.loads(r.data)
    print(json.dumps(parsed, indent=4, sort_keys=True))


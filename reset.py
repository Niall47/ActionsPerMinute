import urllib.request
import time

def reset_request():
    var =1
    while var == 1 :
        time.sleep(10)
        url = "http://localhost:3048/reset"
        r = urllib.request.urlopen(url)

reset_request()
import requests

def scrapeCheckProxy():
    r = requests.get("https://api.proxyscrape.com?request=displayproxies&proxytype=http&timeout=7000&country=DE&anonymity=elite&ssl=no")
    proxies = r.text
    badProxy = []
    for i in proxies:
        test = requests.get("https://www.google.com", proxies = {"http" : f"http://{i}"})
        if test.status_code != 200: 
            badProxy.append(i)
    if len(badProxy) == 0:
        print("All proxies functioning!")
    else:
        print(badProxy)

scrapeCheckProxy()


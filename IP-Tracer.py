import requests
import urllib
import colorama
import json
colorama.init(autoreset=True)
print(colorama.Fore.GREEN+ """
  ALPXHAX's 
  ___ ____     _____ ____      _    ____ _____ ____  
 |_ _|  _ \   |_   _|  _ \    / \  / ___| ____|  _ \ 
  | || |_) |____| | | |_) |  / _ \| |   |  _| | |_) |
  | ||  __/_____| | |  _ <  / ___ \ |___| |___|  _ < 
 |___|_|        |_| |_| \_\/_/   \_\____|_____|_| \_\
     
 Available EVERYWHERE!  github.com/ALPXHAX
""")
print ("\r")
choice=int(input("Enter your choice\n1.My IP Address\n2.Track custom IP Address\nEnter your choice here:"))
if choice==1:
    response=requests.get('https://ip-fast.com/api/ip/')
    ip=response.text
    print("Your IP Address is:",ip)
    url="http://ip-api.com/json/"
    request=urllib.request.urlopen(url+ip)
    json_1=json.loads(request.read())
    #condition
    if json_1['status'] == "success":
    	print(f"Country : {json_1['country']}")
    	print(f"Region : {json_1['regionName']}")
    	print(f"City : {json_1['city']}")
    	print(f"Latitude : {json_1['lat']}")
    	print(f"Longitude : {json_1['lon']}")
    	print(f"ISP : {json_1['isp']}")
    else:
    	print("Failed to find the IP informations.")
elif choice==2:
        ip=input("What's the IP of victim? ")
        url="http://ip-api.com/json/"
        request=urllib.request.urlopen(url+ip)
        json_1=json.loads(request.read())
        #condition
        if json_1['status'] == "success":
        	print(f"IP : {json_1['query']}")
        	print(f"Country : {json_1['country']}")
        	print(f"Region : {json_1['regionName']}")
        	print(f"City : {json_1['city']}")
        	print(f"Latitude : {json_1['lat']}")
        	print(f"Longitude : {json_1['lon']}")
        	print(f"ISP : {json_1['isp']}")
        else:
        	print("Failed to find the IP informations.")
else:
    print("Wrong Option, Please enter 1 or 2")

        
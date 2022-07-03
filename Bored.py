import imp
from urllib import response
import requests
import json 

# url = "http://www.boredapi.com/api/activity?type="
activity = ""
participants = ""
link = ""
activityType = ""
res = ""
type = ""
price = .5
error = ""

def getData(type):
    data = {}
    try:
        url = "http://www.boredapi.com/api/activity?type="+type.lower()+"&price="+str(price)
        response = requests.get(url)
        data = response.json()
    except:
        data["error"] = "Something went wrong"
    
    return data

print ("1 = Education")
print ("2 = Recretional")
print ("3 = Social")
print ("4 = Diy")
print ("5 = Charity")
print ("6 = Cooking")
print ("7 = Relaxation")
print ("8 = Music")
print ("9 = BusyWork")

menu = int(input("Choose "))
if menu == 1:
    type = "education"
elif menu ==2:
    type = "recreational"
elif menu ==3:
    type = "Social"
elif menu ==4:
    type = "Diy"
elif menu ==5:
    type = "Charity"
elif menu ==6:
    type = "Cooking"
elif menu ==7:
    type = "Relaxation"
elif menu ==8:
    type = "Music"
elif menu ==9:
    type = "BusyWork"
else:
    type = "Diy"
    
res = getData(type)   
if "error" in res:
    error = res["error"]
    print (error)
else:
    activity = res["activity"]
    participants = res["participants"]
    activityType = res["type"]
    if res["link"]:
        link = res["link"]
    else:
        link = "No Link"

    print (link)
    print (activity)
    print (participants)
    print (type)
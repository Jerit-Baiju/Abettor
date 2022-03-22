import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
global op
def weather():
    try:
        url = "https://www.google.com/search?q=weather+in+kerala"
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.content,'html.parser')
        temperature = soup.find('span',attrs={'id':'wob_ttm'}).text
        status = soup.find('span',attrs={'id':'wob_dc'}).text
        location = soup.find('div',attrs={'id':'wob_loc'}).text
        temperature_op = (f"Temperature - {temperature}°F \n\t")
        status_op = (f"Status - {status} \n\t")
        location_op = (f"Location - {location}")
        a = datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%H:%M")
        time = (f"    Refreshed at {a} \n\t")
        op = (time+temperature_op+status_op+location_op)
    except:
        op = "NO NETWORK"
    return op
def ajent_submits():
    try:
        url = "https://ajent.pythonanywhere.com/api-key=submit"
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.content,'html.parser')
        logs = soup.text
    except:
        logs = "NO NETWORK"
    return logs

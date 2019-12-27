from fbchat import Client
from fbchat.models import *
import requests
import time

def get_info():
    url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3a420d3c1ad04181bdd80b8d60584a44'
    content = requests.get(url).json()
    compreh_content = [inside['title'] + "\n" + inside['content'] + "\n\n" for inside in content['articles']]
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = "Prague"
    url = api_address + city
    json_data = requests.get(url).json()

    temperature = json_data['main']['temp']
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    mes = "".join(compreh_content[0:5])
    return "Good morning Mat. Have a good day\n" "Temperature: " + str(temperature) + " K\nPressure: " + str(pressure) + " mbar\nHumidity: " + str(humidity) + "%\n\n"   "Here are some news from tech\n" + mes


def send_mes(message):
    client = Client('example@mail.com', 'password')
    client.send(Message(message), thread_type=ThreadType.USER, thread_id='users id')


def main():
    time_1 = time.localtime()
    if time_1.tm_hour == 6 and time_1.tm_min == 30 and time_1.tm_sec == 0:
        send_mes(get_info())
if __name__ == '__main__':
        while True:
            main()




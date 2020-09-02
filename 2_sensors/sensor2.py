from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client

sensor = DistanceSensor(echo=17, trigger=4)
sensor1 = DistanceSensor(echo=27, trigger=22)
sender = udp_client.SimpleUDPClient('127.0.0.1',4560)
sender1 = udp_client.SimpleUDPClient('127.0.0.1',4560)

while True:
    #pitch = 75
    pitch = round(sensor.distance * 100 + 30)
    sender.send_message('/play_this_p', pitch)
    volume = round((sensor1.distance * 10),2)
    sender1.send_message('/play_this_v', volume)
    sleep(0.1)
    print(sensor.distance,sensor1.distance,volume)
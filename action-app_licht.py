#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import requests

url1="192.168.178.22" #bridge EG
url2="192.168.178.34" #bridge Treppe

user1="8DHvuFP5WyokDpR9hqUilC6qdSQyV9qN0C9hUNip" #User bridge EG - HueZero
user2="NkzHsagBAMkjxMwzAzpUqY4zorvDClkPkwfMRHmk" #user bridge Treppe - HueZero2

url_sensor1_1="http://" + url1 + "/api/" + user1 + "/sensors/1/config" #bridge EG - Flur
url_sensor2_1="http://" + url2 + "/api/" + user2 + "/sensors/1/config" #bridge Treppe - KG
url_sensor2_2="http://" + url2 + "/api/" + user2 + "/sensors/2/config" #bridge Treppe - EG
url_sensor2_3="http://" + url2 + "/api/" + user2 + "/sensors/3/config" #bridge Treppe - OG
url_sensor2_4="http://" + url2 + "/api/" + user2 + "/sensors/4/config" #bridge Treppe - DG

url_lampe_blumenlampe="http://" + url1 + "/api/" + user1 + "/lights/13/state"
url_lampe_stehlampe="http://" + url1 + "/api/" + user1 + "/lights/18/state"
url_lampe_regal1="http://" + url1 + "/api/" + user1 + "/lights/8/state"
url_lampe_regal2="http://" + url1 + "/api/" + user1 + "/lights/9/state"
url_lampe_stripWhite="http://" + url1 + "/api/" + user1 + "/lights/15/state"
url_lampe_stripColor="http://" + url1 + "/api/" + user1 + "/lights/14/state"
url_lampe_pendel="http://" + url1 + "/api/" + user1 + "/lights/16/state"
url_lampe_kueche="http://" + url1 + "/api/" + user1 + "/lights/17/state"
url_lampe_kuecheL="http://" + url1 + "/api/" + user1 + "/lights/22/state"
url_lampe_kuecheM="http://" + url1 + "/api/" + user1 + "/lights/21/state"
url_lampe_kuecheR="http://" + url1 + "/api/" + user1 + "/lights/23/state"

url_lampeDG="http://" + url2 + "/api/" + user2 + "/lights/2/state"
url_lampeOGDG="http://" + url2 + "/api/" + user2 + "/lights/1/state"
url_lampeOG="http://" + url2 + "/api/" + user2 + "/lights/3/state"
url_lampeEGOG="http://" + url2 + "/api/" + user2 + "/lights/4/state"
url_lampeEG="http://" + url2 + "/api/" + user2 + "/lights/5/state"
url_lampeKGEG="http://" + url2 + "/api/" + user2 + "/lights/6/state"
url_lampeKG="http://" + url2 + "/api/" + user2 + "/lights/7/state"

data_on={'on':True}
data_off={'on':False}
data_on_50={'on':True, 'bri':50}
data_on_80={'on':True, 'bri':80}
data_on_100={'on':True, 'bri':100}
data_on_150={'on':True, 'bri':150}
data_on_200={'on':True, 'bri':200}
data_on_255={'on':True, 'bri':255}

headers={'Content-type':'application/json'}


CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Licht(object):
    """Class used to wrap action code with mqtt connection
        
        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()
        
    # --> Sub callback function, one per intent
    def intent_1_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        # hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        r = requests.put(url_lampe_blumenlampe, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_stehlampe, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_regal1, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_regal2, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_stripWhite, json=data_on_80, headers=headers)
        print r.content
        r = requests.put(url_lampe_stripColor, json=data_on_80, headers=headers)
        print r.content
        r = requests.put(url_lampe_pendel, json=data_on_50, headers=headers)
        print r.content
        r = requests.put(url_lampe_kueche, json=data_on_50, headers=headers)
        print r.content
        r = requests.put(url_lampe_kuecheL, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_kuecheM, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_kuecheR, json=data_off, headers=headers)
        print r.content


        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Der Fernsehabend kann beginnen", "")

    def intent_2_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        # hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        r = requests.put(url_lampe_blumenlampe, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_stehlampe, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_regal1, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_regal2, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_stripWhite, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_stripColor, json=data_off, headers=headers)
        print r.content
        r = requests.put(url_lampe_pendel, json=data_on_255, headers=headers)
        print r.content
        r = requests.put(url_lampe_kueche, json=data_on_100, headers=headers)
        print r.content
        r = requests.put(url_lampe_kuecheL, json=data_on_100, headers=headers)
        print r.content
        r = requests.put(url_lampe_kuecheM, json=data_on_100, headers=headers)
        print r.content
        r = requests.put(url_lampe_kuecheR, json=data_on_100, headers=headers)
        print r.content


        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Guten Appetit", "")

    # More callback function goes here...

    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'schlammracer:Licht_Fernsehabend':
            self.intent_1_callback(hermes, intent_message)
        if coming_intent == 'schlammracer:Licht_Essen':
            self.intent_2_callback(hermes, intent_message)

        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Licht()

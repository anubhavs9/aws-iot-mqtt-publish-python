'''
Title : Publish data to AWS IoT Core using MQTT
@author : Anubhav Sharma
          https://anubhavsharma.dev
@Date : 11/10/2020
'''

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import os

class AWSUpload:
    PATH_TO_CONFIG = "config.json"
    ENDPOINT = ""
    CLIENT_ID = ""
    PATH_TO_CERT = ""
    PATH_TO_KEY = ""
    PATH_TO_ROOT = ""
    MESSAGE = ""
    TOPIC = "test/testing"

    def __init__(self):
        print("Initializing AWS MQTT ")
        self.setVariables()


    '''
    Description : Parse json config file and set the variables
    '''
    def setVariables(self):
        configData = {}
        if os.path.exists(self.PATH_TO_CONFIG):
            with open(self.PATH_TO_CONFIG) as fp:
                configData = json.load(fp)
            self.ENDPOINT = configData["ENDPOINT"]
            self.CLIENT_ID = configData["CLIENT_ID"]
            self.PATH_TO_CERT = configData["PATH_TO_CERT"]
            self.PATH_TO_KEY = configData["PATH_TO_KEY"]
            self.PATH_TO_ROOT = configData["PATH_TO_ROOT"]
            self.TOPIC = configData["TOPIC"]
        else:
            print("ERROR : config file not found")
            exit(-1)


    '''
    Description : Connect to AWS Endpoint
                    Start MQTT connection
                    Take user input
                    Publish to AWS MQTT topic
    '''
    def mqttStart(self):
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        mqtt_connection = mqtt_connection_builder.mtls_from_path(
                    endpoint=self.ENDPOINT,
                    cert_filepath=self.PATH_TO_CERT,
                    pri_key_filepath=self.PATH_TO_KEY,
                    client_bootstrap=client_bootstrap,
                    ca_filepath=self.PATH_TO_ROOT,
                    client_id=self.CLIENT_ID,
                    clean_session=False,
                    keep_alive_secs=6
                    )
        print("Connecting to {} with client ID '{}'...".format(
                self.ENDPOINT, self.CLIENT_ID))
        connect_future = mqtt_connection.connect()
        connect_future.result()
        print("Connected!")
        print()
        print("Enter message to Publish. or Enter 'exit' to close.")
        while True:
            self.MESSAGE = input(">> ")
            if self.MESSAGE == "exit":
                break
            message = {"message" : self.MESSAGE}
            mqtt_connection.publish(topic=self.TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
            print("Published: '" + json.dumps(message) + "' to the topic: " + self.TOPIC)
            t.sleep(1)
        print('Closing connection')
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()


if __name__ == "__main__":
    aws = AWSUpload()
    aws.mqttStart()
    print("Closing Application")
    exit(0)
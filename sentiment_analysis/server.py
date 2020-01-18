import redis
import time
import traceback
from os import environ
from sentiment_analysis import get_sentiment


import os


def ServerMain():
    '''
    The main server logic which connects to the webserver and redis
    '''
    try:
        r = redis.StrictRedis.from_url(environ['REDIS_URI'])

        p = r.pubsub()
        p.subscribe('sentiment_analysis_py')

        while True:
            message = p.get_message()
            if message and message['data'] != 1:
                command = message['data'].decode('utf-8').split(':')

                if command[0] == "param":
                    r.publish("diarization_node_log",
                              f"Got file name: {command[0]}")
                    print("sending hello " + command[1])
                    r.publish(
                        "diarization_node", "Welcome to RE:VERB api server. Upload a file to /upload in order to get diarization results (use HTTP POST request)!")
                elif command[0] == "file":
                    r.publish("diarization_node_log",
                              f"Got file name: {command[1]}")
                    r.publish("diarization_node_log",
                              f"Got os dir: {os.listdir()}")
                    print(f"Got file name: {command[1]}")
                    print(os.listdir())
                    sentiment_analysis_result = get_sentiment(command[1])
                    r.publish("diarization_node", f"{sentiment_analysis_result}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    ServerMain()

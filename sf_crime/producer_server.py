from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        '''
        Sends one message per 1 seconds frpm the input json file, to the topic specified on instantiation.
        '''
        with open(self.input_file) as f:
            json_list = json.load(f)
            for json_entry in json_list:
                message = self.dict_to_binary(json_entry)
                # TODO send the correct data
                self.send(self.topic,value=message)
                print('Sending: '+str(json_entry))
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return str(json_dict).encode()
        
import paho.mqtt.client as mqttclient


def on_connect(self, client, userdata, flags, rc):
    if rc == 0:
        print("client connect")
        client.loop_start()
        client.subscribe(self.topic)
        # connect_state = True
    else:
        # self.connect_state = True
        print("client is not connected")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        # self.connect_state = False
        # self.client.connect(self.address, port=self.port)
        # self.client.subscribe(self.topic)
        # self.client.loop_start()
        print("MQTT reconnect")


def on_messages(client, userdata, message):
    m_str = str(message.payload.decode("utf-8"))
    try:
        my_dict = eval(m_str)
        # self.smab_db.add_record(my_dict)
        # self.upload.convert_excel(my_dict)
        # self.upload.convert_excel_form(my_dict)
    except:
        pass


class Backend:
    def __init__(self):
        self.client = mqttclient.Client(mqttclient.CallbackAPIVersion.VERSION1)
        self.connect_state = False
        self.address = ""
        self.port = 1883
        self.topic = ""

    def connect_client(self, address, topic):
        self.address = address
        self.topic = topic
        self.client.connect(address, port=1883)
        self.client.subscribe(topic)
        self.client.on_connect = on_connect
        self.client.on_disconnect = on_disconnect
        self.client.on_message = on_messages
        self.client.loop_start()

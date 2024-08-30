import time
import json
import socket


class Client():

    def __init__(self, server = "server", port = 5050, header = 640) -> None:
        """
        Constructor
        """

        # Params 
        self.ID = None
        self.PORT = port
        self.HEADER = header
        self.FORMAT = "utf-8"   
        self.DISCONNECT_MSG = "!DISCONNECTED"

        # Server 
        self.SERVER = ""
        if not server: self.SERVER = socket.gethostbyname(socket.gethostname())
        else: self.SERVER = server
        self.ADDR = ("server-app", self.PORT) 
        print(self.ADDR)

        # Making Client and connecting to server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
    

    def send(self, msg):
        """
        Function to send msg to server
        Inputs - msg (string): message to be sent to the server
        """

        # Encode string to bytes
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        # Padded length of the message
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        # Sedning msg
        self.client.send(send_length)
        self.client.send(message)


    def __call__(self, msg = None, output_file_name = "output"):
        
        # Sending prompt to the server
        self.send(msg)

        # Length of llm response
        msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
        msg_length = int(msg_length)
        # llm response
        llm_response = self.client.recv(msg_length).decode(self.FORMAT)

        # Checking if response from the server
        check = llm_response[-7:]
        llm_response = llm_response[0:-7]
        llm_response_dict = json.loads(llm_response)
        if check != "_SERVER": llm_response_dict["Source"] = "User"

        # Length of client ID
        msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
        msg_length = int(msg_length)
        # client ID
        self.ID = self.client.recv(msg_length).decode(self.FORMAT)

        # Writing to .json file
        llm_response_dict["CliendID"] = self.ID
        with open(f"/data/{output_file_name}_{self.ID}.json", 'w') as file:
            json.dump(llm_response_dict, file, indent = 4)

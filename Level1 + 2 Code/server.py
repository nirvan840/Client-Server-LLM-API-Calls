import time
import socket
import threading
from API_class import APIcall


class Server():

    def __init__(self, server = None, port = 5050, header = 640) -> None:
        """
        Constructor
        """

        # URL/Endpoint used by a server to listen for incoming connections from clients.
        self.PORT = port
        # Get the hostname of the current machine using socket.gethostname(). Find and return the IP address associated with this hostname using socket using gethostbyname().
        self.SERVER = ""
        if not server: self.SERVER = socket.gethostbyname(socket.gethostname())
        else: self.SERVER = server
        self.ADDR = (self.SERVER, self.PORT)

        # Initializing the server (Adress Family - Internet uses IPv4)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        # Client 
        self.HEADER = header
        self.FORMAT = "utf-8"   # Message sent in bytes and needs to be decoded to string
        self.DISCONNECT_MSG = "!DISCONNECTED"

        # API Object
        self.gemma1 = APIcall()


    def send(self, msg, conn, auth = False):
        """
        Function to send llm_response back to client
        Inputs - msg (string): message to be sent to the server
        """

        # Encode string to bytes
        if auth: msg += "_SERVER"
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        # Padded length of the message
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        # Sedning msg
        conn.send(send_length)
        conn.send(message)


    def handle_client(self, conn, addr):
        """
        Funtion to handle client prompt, make API call and returns the response, the llm_response_dict (string) to the respective client
        """
        
        # New connection message
        print(f"\n[NEW CONNECTION] {addr} connected")

        # Blocking line: wont proceed untill mesasge recived from client Blocking lines is why we need multi-threading
        connected = True
        while connected:
            # First we recive msg length and chck if valid
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length: 
                msg_length = int(msg_length)
                # Next we recive the actual message
                msg = conn.recv(msg_length).decode(self.FORMAT)
                # Checking if client wants to disconnect 
                if msg == self.DISCONNECT_MSG: break
                # Printing msg
                time.sleep(0.05)
                print(f"[{addr}] | Msg: {msg}")
                # Making API Call
                llm_response = self.gemma1(user_prmpt=msg)
                # Sending response and ID back to client 
                self.send(llm_response, conn, auth = True)
                self.send(str(addr[1]), conn)

        # Closing connection
        conn.close()


    def __call__(self):
        """
        Function defining server behaviour
        """

        # Checking for clients sending requests
        self.server.listen()
        print(f"\n[LISTENING] Server is listening on {self.SERVER}\n")
        while True:
            conn, addr = self.server.accept()
            # Create a new thread; allowing server to handle >1 clients
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

            # Printing # of active clients
            time.sleep(0.008)
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            


#---------------------------------------------------------------

server1 = Server()
server1()

#---------------------------------------------------------------
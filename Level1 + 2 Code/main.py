"""
LEVEL 1
- Reads prompt from input1.txt
- Stores json in output1.txt
"""

level1 = True
if level1:
    # Making an API calss object to make an API call
    from API_class import APIcall

    gemma1 = APIcall()
    gemma1("input1", "output1", print_llm_response=True)



#----------------------------------------------------------------



"""
LEVEL 2
- Reads prompts from input2.txt
- Each line in input2.txt is considered as a distinct prompt
- Makes a client to deal with each prompt
- Stores responses recieved by client in output_ID.json
"""

from client import Client
import time

# Each client gets one line from the file
with open('input2.txt', 'r') as file: lines = file.readlines()
for line in lines:
    client = Client()
    client(line)
    time.sleep(1)
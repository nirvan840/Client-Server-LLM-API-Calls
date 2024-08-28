"""
- Script to make API Calls to LLM using Groq API
- Different LLM Parameters can be Tweaked

Input: From input.txt file
Output: To output.json file
"""

# Dependancies
import os
import sys
import json
import groq
from groq import Groq


class APIcall():

    def __init__(self, key = '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', model_choice = "Gemma 2 9B", stop_token = None, context_size = 1024, temperature = 0.5, top_p = 1) -> None:
       
        # Setting up API key
        self.client = Groq(
            api_key = key,
        )

        # Setting LLM Parameters
        self.model_choice = model_choice 
        models_dict = {
            "Distil-Whisper": "distil-whisper-large-v3-en",
            "Gemma 2 9B": "gemma2-9b-it",
            "Gemma 7B": "gemma-7b-it",
            "Llama 3 Groq 70B Tool Use (Preview)": "llama3-groq-70b-8192-tool-use-preview",
            "Llama 3 Groq 8B Tool Use (Preview)": "llama3-groq-8b-8192-tool-use-preview",
            "Llama 3.1 70B (Preview)": "llama-3.1-70b-versatile",
            "Llama 3.1 8B (Preview)": "llama-3.1-8b-instant",
            "Llama Guard 3 8B": "llama-guard-3-8b",
            "Meta Llama 3 70B": "llama3-70b-8192",
            "Meta Llama 3 8B": "llama3-8b-8192",
            "Mixtral 8x7B": "mixtral-8x7b-32768",
            "Whisper": "whisper-large-v3"
        }
        if len(sys.argv) > 1: model_choice = sys.argv[1]
        self.stop_token = stop_token
        self.context = context_size
        self.temp = temperature
        self.top_p = top_p

        # Setting up model name
        self.model_name = models_dict[model_choice]


    def __call__(self, input_file_name, output_file_name, print_llm_response = True):
        
        # Reading user prompt
        user_prompt = ""
        with open(f"{input_file_name}.txt", 'r') as file: 
            user_prompt = file.read()

        # Making API call
        system_prompt = """
        Your job is to answer the user prompt and output the structured data in JSON.
        The JSON schema should include:
        {
            "Prompt": "string which stores the original prompt sent by the user",
            "Message": "string which stores the response string from the API",
            "TimeSent": "Stores the Time that the prompt was originally sent out by the client as a UNIX Timestamp",
            "TimeRecvd": "Stores the Time that the response was received by the client as a UNIX Timestamp",
            "Source":  "Stores the source of the response, such as Gemma, Grok or ChatGPT etc."
        }
        """
        chat_completion = self.client.chat.completions.create(
            # Required Params
            messages = [
            # System
            {
                "role": "system",
                "content": system_prompt
            },
            # User
            {
                "role": "user",
                "content": user_prompt,
            }
            ],
            # The language model which will generate the completion.
            model = self.model_name,

            # Optional params
            temperature = self.temp,
            max_tokens  = self.context,
            top_p       = self.top_p,
            stop        = self.stop_token,
            response_format = {"type": "json_object"},
            stream      = False,
        )

        # Storing in output.json file
        llm_response = chat_completion.choices[0].message.content
        llm_response_dict = json.loads(llm_response)
        with open(f"{output_file_name}.json", 'w') as file:
            json.dump(llm_response_dict, file, indent = 4)

        # Print the completion returned by the LLM.
        if print_llm_response: print(chat_completion.choices[0].message.content)
   
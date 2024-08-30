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

# Setting up API key
key = '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'
client = Groq(
    api_key = key,
)
    
if __name__ == "__main__":

    # Setting LLM Parameters
    model_choice = "Gemma 2 9B"  # Default choice
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
    stop_token = None
    context = 1024
    temp = 0.5
    top_p = 1

    # Checking for command line inputs
    if len(sys.argv) > 1:
        model_choice = sys.argv[1]
    model_name = models_dict[model_choice]

    # Reading user prompt
    user_prompt = ""
    with open('input.txt', 'r') as file:
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
    chat_completion = client.chat.completions.create(
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
        model = model_name,

        # Optional params
        temperature = temp,
        max_tokens = context,
        top_p=1,
        stop = stop_token,
        response_format={"type": "json_object"},
        stream = False,
    )

    # Storing in output.json file
    llm_response = chat_completion.choices[0].message.content
    llm_response_dict = json.loads(llm_response)
    with open("output.json", 'w') as file:
        json.dump(llm_response_dict, file, indent = 4)

    # Print the completion returned by the LLM.
    print(chat_completion.choices[0].message.content)
   
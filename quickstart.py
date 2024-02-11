import os
import requests
import json
import openai
openai.api_key="4aadaecf017c474cbb681f55c9be8d9b"
openai.api_base="https://openaimartns1.openai.azure.com/"
openai.api_type="azure"
openai.api_version="2022-12-01"
deployment_name="text-davinci-003"
os.system('cls')
start_phrase="What can we learn from Schiller about the dangers of GPT4?\n\n"
print("Sending a test completion job to the Davinci algorithm...\n")
response = openai.Completion.create(engine="text-davinci-003", prompt=start_phrase, max_tokens=400)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(text+"\n")
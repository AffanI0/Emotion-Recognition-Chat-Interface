import requests
import json

# this is a simle chatbot that connects to ollama, llama 3 model
def botChat(message):
    url = "http://localhost:11434/api/chat"
    payload = {"model": "llama3:8b", "messages": [{"role": "user", "content": message}], "stream": False }
     # making a post rquets to the ollama api
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status() # Raising an error for any bad responses

        data = response.json()
        # Extract the content from the message object
        answer = data.get("message", {}).get("content", "").strip()
        return answer
    except requests.exceptions.RequestException as e:
        return print("Error connecting to ollama: {e}")

# Simple chat loop for tesing with a users imput
print("Chatbot started:")
while True:
    userInput = input("User: ")
    if userInput.lower() == 'quit':
        break
    response = botChat(userInput)
    print("Bot: ", response)


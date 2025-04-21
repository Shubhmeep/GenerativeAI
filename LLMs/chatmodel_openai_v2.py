from langchain_openai import ChatOpenAI

'''
Chat models are often backed by LLMs but tuned specifically for having conversations. 
Crucially, their provider APIs use a different interface than pure text completion models. 
Instead of a single string, they take a list of chat messages as input and they return an AI message as output. 

chatmodel() and openAI() llm have the same base class internally.
'''

from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-4', temperature=1) # temperature value range from 0 -> 2 

res = model.invoke("capital of india?")

print(res.content)
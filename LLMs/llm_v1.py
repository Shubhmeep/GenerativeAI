from langchain_openai import OpenAI # refers to llm
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("what is the capital of india")
print(result)

'''

LLMs in LangChain refer to pure text completion models. 
The APIs they wrap take a string prompt as input and output a string completion. 
OpenAI's GPT-3 is implemented as an LLM.

'''

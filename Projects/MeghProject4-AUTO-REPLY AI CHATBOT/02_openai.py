from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
1. To Write an Essay on the Specified Title


2. To Have Some Ideas on Science Projects


3. To Understand Any Concept in Maths


5. To Understand Any Scientific Term
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named sandhya I am student I have so many questions"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
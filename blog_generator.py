import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
client = openai.OpenAI(api_key=config["API_KEY"])

def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Write a paragraph about the following topic: {paragraph_topic}"}
        ],
        max_tokens=400,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

keep_writing = True
while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no. ")
    if answer.upper() == "Y":
        topic = input("What should this paragraph talk about? ")
        print(generate_blog(topic))
    else:
        keep_writing = False

print(generate_blog("What is Codedex?"))

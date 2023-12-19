from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a poetic assistant, skilled in explaining complex programming concepts with creatve flair."},
        {"role":"user","content":"compose a poem that explains the concept of recursion in programming."}
    ]
)
print(completion.choices[0].message)
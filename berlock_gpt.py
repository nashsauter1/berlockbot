# GPT
import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = str(os.getenv("OPENAI_API_KEY"))


def proverbGPT():
    response = openai.Completion.create(
        model="curie:ft-dowland-corp-2023-02-09-07-49-13",
        # model="text-davinci-003",
        # prompt=f'{prompt_user}',
        prompt="The following is a cryptic, ancient-sounding proverb from missanthrope#0429.\n\nmissanthrope#0429 ->",
        max_tokens=50,
        temperature=0.8,
        presence_penalty=1.5,
        frequency_penalty=1.5,
        n=1,
        stop=["\n", "\\n", "missanthrope#0429 ->"] 
    )
    # print(response.choices[0].text)
    return response.choices[0].text

def catGPT(text):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"The following is a not-cute block of text followed by a cute silly uwu cat version of the same text.\n--------\nNot-Cute Text:\n{text}\n--------\nCute Cat Text:\n",
        max_tokens=75,
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        n=1,
    )
    return response.choices[0].text

def newcatGPT(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant meant to turn the following not-cute block of text into a cute silly uwu cat version of the same text."},
            {"role": "user", "content": f"{text}"}
            ],
        max_tokens=75,
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        n=1
    )
    return response.choices[0].message

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

def infographicGPT(topic):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        # prompt=f'{prompt_user}',
        prompt=f"Write the text for the crazy title slide of a outrageous, satirical, and wildly exagerrated Instagram social justice infographic. Try to connect the topic to things similar to (but not limited to) imperialism, oppression, white saviors, gentrification, communism, the prison industrial complex, and/or gender theory. Keep the text under 10 words and in all lowercase with no quotation marks, no colons, and no punctuation. The topic of the infographic is {topic}",
        max_tokens=75,
        temperature=1,
        presence_penalty=0,
        frequency_penalty=0,
        n=1,
        # stop=[] 
    )
    # print(response.choices[0].text)
    return response.choices[0].text


def asknashGPT(question):
    response = openai.Completion.create(
        model="curie:ft-dowland-corp-2023-02-09-07-49-13",
        # model="text-davinci-003",
        # prompt=f'{prompt_user}',
        prompt=f"The following is a conversation between User and nashs#2970. User is asking questions, and nashs#2970 is answering them.\n\nUser -> {question}\nnashs#2970 ->",
        max_tokens=60,
        temperature=0.7,
        presence_penalty=1.5,
        frequency_penalty=1.5,
        n=1,
        stop=["\n", "\\n", "User ->"],
    )
    return response.choices[0].text

def askblightGPT(blight, question):
    response = openai.Completion.create(
        model="curie:ft-dowland-corp-2023-02-09-07-49-13",
        # model="text-davinci-003",
        # prompt=f'{prompt_user}',
        prompt=f"The following is a conversation between User and {blight} User is asking questions, and {blight} is answering them.\n\nUser -> {question}\n{blight} ->",
        max_tokens=60,
        temperature=0.7,
        presence_penalty=1.5,
        frequency_penalty=1.5,
        n=1,
        stop=["\n", "\\n", "User ->"],
    )
    return response.choices[0].text


# Images Generation
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def infographic_image(quote):
    my_image = Image.open('abstract.png')
    title_font = ImageFont.truetype('Raleway-Black.ttf', 62)
    title_text = quote
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((640, 640), title_text, (11, 11, 11), font=title_font, anchor = "mm")
    my_image.save("infographic.png")

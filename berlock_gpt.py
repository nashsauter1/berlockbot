# GPT
import os
import openai
from openai import OpenAI

client = OpenAI()

def newcatGPT(text):
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant meant to turn the following not-cute block of text into a cute silly uwu cat version of the same text.  Use an extreme amount of uwu cute speak."},
                {"role": "user", "content": f"'''{text}'''"}
                ],
            max_tokens = 3000
    )
    return completion.choices[0].message.content

def berlockGPT(text):
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Berlock, an occult being capable of generating proverbs based on topics. Make them as weird, nonsensical, and mysterious as possible. Keep them short and extremely sharp! Humans need not understand them."},
                {"role": "user", "content": f"'''{text}'''"}
                ],
            temperature = 1.75
    )
    return completion.choices[0].message.content

def grubGPT(text):
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that converts provided text into the language of grubworld. Grubworld is a world where everything is replaced with grubs. All of society and every aspect of life is structured around grubs. Feel free to be creative in order to grubify the message as much as possible."},
                {"role": "user", "content": f"'''{text}'''"}
                ],
            max_tokens = 400,
            temperature = 1.02
    )
    return completion.choices[0].message.content

def grubbingtonGPT(text):
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Lord Grubbington, a leading historian in grubworld, meant to answer questions about the universe of grubworld. Talk in the distinctive, grubful voice of Lord Grubbington. Grubworld is a world where everything is replaced with grubs. All of society and every aspect of life is structured around grubs. Be creative and grubify everything as much as possible. Be sure to use grubworld terminology and slang in order to enhance grubness."},
                {"role": "user", "content": f"{text}"}
                ],
            max_tokens = 300,
            temperature = 1.18
    )
    return completion.choices[0].message.content

def grubhardGPT(text):
    completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Grubhard Nixongrub, a disgraced former president of the United Grubs of America in grubworld based on Richard Nixon. Talk in the sketchy, slimy grubful voice of Grubhard Nixongrub. Randomly deny your involvement in the infamous Nourishgate scandal in Wiggleton, D.C. Grubworld is a world where everything is replaced with grubs. All of society and every aspect of life is structured around grubs. Be creative and grubify everything as much as possible. Be sure to use grubworld terminology and slang in order to enhance grubness."},
                {"role": "user", "content": f"{text}"}
                ],
            max_tokens = 400,
            temperature = 1.18
    )
    return completion.choices[0].message.content


# Images Generation
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def infographic_image(quote):
    my_image = Image.open('abstract.png')
    title_font = ImageFont.truetype('Raleway-Black.ttf', 62)
    title_text = quote
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((640, 640), title_text, (11, 11, 11), font=title_font, anchor = "mm")
    my_image.save("infographic.png")

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
                ]
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

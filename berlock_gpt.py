# GPT
import os
import openai
client = OpenAI()


# Images Generation
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

def infographic_image(quote):
    my_image = Image.open('abstract.png')
    title_font = ImageFont.truetype('Raleway-Black.ttf', 62)
    title_text = quote
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((640, 640), title_text, (11, 11, 11), font=title_font, anchor = "mm")
    my_image.save("infographic.png")

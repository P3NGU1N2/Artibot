import openai
import requests
import json
import random
import string 

def generate_image(prompt):
    #generate the image using openai api

    openai.api_key = input("Enter your OpenAI api> ")
    image_resp = openai.Image.create(prompt=prompt)
    data = image_resp.data
    image_url = data[0]['url']
    return image_url

      
def download_image(url):
    #downloading the requested image from url

    img_offline = requests.get(url)
    image_data = img_offline.content
    filename_change = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '.jpg'

    # Save the image to a file
    with open(filename_change, "wb") as f:
        f.write(image_data)


# Generate an image using the OpenAI API
prompt = input("Enter the Image you want to generate: ")
image_url = generate_image(prompt)

# Download the image from the URL
download_image(image_url)




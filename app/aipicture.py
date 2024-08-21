import openai
import config
import requests
openai.api_key = config.OPENAI_API_KEY

def DALL_E_Query(query):
    response = openai.Image.create(
        prompt="Je veux une image illustrant un podcast sur le theme de {}".format(query),
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    open("static/image.jpg", "wb").write(requests.get(image_url).content)
    return image_url
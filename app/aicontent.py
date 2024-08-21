import openai
import config
openai.api_key = config.OPENAI_API_KEY


# def openAIQuery(query):
#     response = openai.Completion.create(
#         # engine="davinci-instruct-beta-v3",
#         engine="text-davinci-003",
#         # prompt=query,
#         prompt="genere moi le texte pour un podcast sur le theme de {}".format(query),
#         temperature=0.8,
#         max_tokens=2000,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0)

#     if 'choices' in response:
#         if len(response['choices']) > 0:
#             answer = response['choices'][0]['text']
#         else:
#             answer = 'Opps sorry, you beat the AI this time'
#     else:
#         answer = 'Opps sorry, you beat the AI this time'

#     return answer

def openAIQuery(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "Tu est un rédacteur très expérimenté dans le domaine du podcast audio"
            },
            {
            "role": "user",
            "content": "Genere moi le texte d'un podcast d'environ trente secondes à propos de {}, je veux uniquement le texte qui sera lu par le lecteur du podcast, il faut que le texte ai une finalité et une conclusion / morale".format(query)
            }
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['message']['content']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'

    return answer
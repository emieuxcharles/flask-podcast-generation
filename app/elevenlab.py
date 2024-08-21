from elevenlabs import set_api_key, generate, play, save
import config
set_api_key(config.ELEVENLAB_API_KEY)

def text_to_speech(text):
    audio = generate(
        text="{}".format(text),
        voice="Bella",
        model="eleven_multilingual_v2"
    )
    save(audio, "static/audio.mp3")
    # return audio

# play(audio)

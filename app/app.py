from flask import Flask, render_template, request, session
import config
import aicontent
import aipicture
import elevenlab
from moviepy.editor import ImageClip, AudioFileClip

def page_not_found(e):
    return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/generate', methods=["GET", "POST"])
def generatePodcast():
    if request.method == "POST":
        generatePodcast = request.form['generatePodcast']
        query = "{}".format(generatePodcast)
        session['podcast_name'] = query.replace(" ", "_").replace("'", "_")
        openAIAnswerUnformatted = aicontent.openAIQuery(query)
        # openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        openAIAnswer = openAIAnswerUnformatted
        
        openAIAnswerPicture = aipicture.DALL_E_Query(query)
        

    # generate_video("static/image.jpg", "tmp/audio.mp3", "generated/{}.mp4".format(query.replace(" ", "_")))

    return render_template('index.html', **locals())

@app.route('/generate-audio', methods=["GET", "POST"])
def generateAudio():
    if request.method == "POST":
        openAIAnswer = request.form['generatePodcastAudio']
        elevenlab.text_to_speech(openAIAnswer)
        audioIsGenerated = True
    return render_template('index.html', **locals())

@app.route('/generate-video', methods=["GET", "POST"])
def generateVideo():
    if request.method == "POST":
        podcastName = request.form['podcastName']
        image_path = "./static/image.jpg"
        audio_path = "./static/audio.mp3"
        background_image = ImageClip(image_path)
        audio_clip = AudioFileClip(audio_path)
        background_image = background_image.set_duration(audio_clip.duration)
        video_clip = background_image.set_audio(audio_clip)
        output_path = "./generated/generated_{}.mp4".format(session['podcast_name'])
        video_clip.write_videofile(output_path, codec='libx264', fps=24)
    return render_template('index.html', **locals())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
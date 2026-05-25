from flask import Flask, render_template, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/transcript/<video_id>")
def transcript(video_id):

    try:

        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        text = " ".join(
            [x["text"] for x in transcript_data]
        )

        return jsonify({
            "transcript": text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run()
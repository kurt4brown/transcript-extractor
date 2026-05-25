from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/transcript/<video_id>")
def transcript(video_id):

    transcript = YouTubeTranscriptApi.get_transcript(
        video_id
    )

    text = " ".join(
        [x["text"] for x in transcript]
    )

    return jsonify({
        "transcript": text
    })

app.run()
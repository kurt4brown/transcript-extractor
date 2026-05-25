from flask import Flask, render_template, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)


def extract_video_id(url_or_id):

    patterns = [
        r"v=([a-zA-Z0-9_-]{11})",
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"youtube\.com/shorts/([a-zA-Z0-9_-]{11})",
    ]

    for pattern in patterns:

        match = re.search(pattern, url_or_id)

        if match:
            return match.group(1)

    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", url_or_id):
        return url_or_id

    raise ValueError("Invalid YouTube URL or ID")


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/transcript/<video_id>")
def transcript(video_id):

    try:

        video_id = extract_video_id(video_id)

        api = YouTubeTranscriptApi()

        transcript = api.fetch(
            video_id,
            languages=["en"]
        )

        text = "\n".join(
            [snippet.text for snippet in transcript]
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

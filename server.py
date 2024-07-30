"""
This module sets up a Flask web application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the sentiment of a given input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    emotion_scores = {key: response[key] for key in response if key != 'dominant_emotion'}
    emotion_scores_join = ", ".join(f"'{key}': {value}" for key, value in emotion_scores.items())
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "¡ Texto no válido! ¡Inténtalo de nuevo !"

    return (f"For the given statement, the system response is {emotion_scores_join}. "
           f"The dominant emotion is <strong>{dominant_emotion}<strong>.")

@app.route("/")
def render_index_page():
    """
    Render the index page of the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

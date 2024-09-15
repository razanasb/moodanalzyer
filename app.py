import gradio as gr
from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# analyze user's mood from text
def analyze_mood(user_input):
    result = sentiment_analysis(user_input)[0]
    
    # assign mood based on sentiment
    if result["label"] == "POSITIVE":
        mood = "Happy"
        suggestion = "Keep enjoying your day 😊"
    elif result["label"] == "NEGATIVE":
        mood = "Sad"
        suggestion = "Try playing a game you like or practice some deep breathing exercises it might help!🍃"
    else:
        mood = "Neutral"
        suggestion = "You're doing well! Stay calm 🌸"
    
    # Output mood and suggestion
    return "Your mood is " + mood + ". " + suggestion

inputs = gr.Textbox(label="How are you feeling today?", placeholder="Type your thoughts here...")
outputs = gr.Textbox(label="Mood and Suggestion")

gr.Interface(fn=analyze_mood, inputs=inputs, outputs=outputs, title="Mood Analyzer with Suggestions").launch()

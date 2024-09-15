import gradio as gr
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Function to analyze user's mood based on input
def analyze_mood(user_input):
    # Analyze the mood from the input text
    result = sentiment_analysis(user_input)[0]
    # Define mood and suggestion based on sentiment analysis
    if result["label"] == "POSITIVE":
        mood = "Happy"
        suggestion = "Keep doing what you're doing! 😊"
    elif result["label"] == "NEGATIVE":
        mood = "Sad"
        suggestion = "Try to talk to someone, or take a break 💡"
    else:
        mood = "Neutral"
        suggestion = "You're doing okay! Stay calm 🌸"
    
    # Return mood and suggestion
    return "Your mood is: " + mood, suggestion

inputs = gr.Textbox(label="How are you feeling today?", placeholder="Type your thoughts here...")
outputs = gr.Textbox(label="Mood and Suggestion")

gr.Interface(fn=analyze_mood, inputs=inputs, outputs=outputs, title="Mood Analyzer").launch()

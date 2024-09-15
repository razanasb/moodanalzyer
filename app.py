import gradio as gr
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Function to analyze mood
def analyze_mood(user_input):
    # analyze mood from text
    results = sentiment_analysis(user_input)
    mood_summary = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}
    suggestions = []

    # sum up scores
    for result in results:
        label = result["label"]
        score = result["score"]
        mood_summary[label] += score

    # find most mood
    main_mood = max(mood_summary, key=mood_summary.get)

    # suggest based on mood
    if main_mood == "POSITIVE":
        suggestion = "Keep enjoying your day :)"
    elif main_mood == "NEGATIVE":
        suggestion = "Maybe play a game or breathe deeply could help!"
    else:
        suggestion = "Doing well! stay calm"

    # return mood and suggestion
    return "Your mood seems mostly " + main_mood.lower() + ". " + suggestion

inputs = gr.Textbox(label="How are you today?", placeholder="Type your feelings here...")
outputs = gr.Textbox(label="Mood and Suggestion")
interface = gr.Interface(fn=analyze_mood, inputs=inputs, outputs=outputs, title="Mood Analyzer with Suggestions")

interface.launch()

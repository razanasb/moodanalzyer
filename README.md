# Mental Health Mood Analyzer
## Project Description: 
This project analyze the mood from text input by the user.

## Why This Idea?
The idea is to help people quickly understand their emotional state from their own text. It can be a helpful tool for mental health awareness.

## Why This Model?
I chose **distilbert-base-uncased-finetuned-sst-2-english** model because it's designed for sentiment analysis, offering a balance between accuracy and performance, suitable for real-time applications.

## Model Details
Model Link: https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

Model Type: DistilBERT is a streamlined version of BERT, designed to perform well while being computationally efficient.

### The Code:
```python
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
```

## Limitations:
- The model i used is pretty good but sometimes it doesn't catch the complex feelings well, so it might get the mood wrong.

- It's trained on English texts mostly, so it might not get things right with other languages or specific ways people talk.

- The tips it gives based on your mood are very basic and might not fit everyone or every situation.

## Next Steps:
Future improvements might include using more advanced models for better emotional understanding or creating a custom model for specific text types. Adding arabic version.

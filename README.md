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

# Define Gradio interface inputs and outputs directly without the '.inputs' or '.outputs' module
inputs = gr.Textbox(label="How are you feeling today?", placeholder="Type your thoughts here...")
outputs = gr.Textbox(label="Mood and Suggestion")

# Create and launch the Gradio interface
gr.Interface(fn=analyze_mood, inputs=inputs, outputs=outputs, title="Mood Analyzer").launch()
```

## Limitations:
- The model i used is pretty good but sometimes it doesn't catch the complex feelings well, so it might get the mood wrong.

- It's trained on English texts mostly, so it might not get things right with other languages or specific ways people talk.

- The tips it gives based on your mood are very basic and might not fit everyone or every situation.

## Next Steps:
Future improvements might include using more advanced models for better emotional understanding or creating a custom model for specific text types. Adding arabic version.

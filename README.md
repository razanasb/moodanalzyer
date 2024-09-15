# Mental Health Mood Analyzer
## Project Description: 
This project analyze the mood from text input by the user.

## Why This Idea?
The idea is to help people quickly understand their emotional state from their own text. It can be a helpful tool for mental health awareness.

## Why This Model?
I chose the distilbert-base-uncased-finetuned-sst-2-english model because it's designed for sentiment analysis, offering a balance between accuracy and performance, suitable for real-time applications.

## Model Details
Model Link: https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

Model Type: DistilBERT is a streamlined version of BERT, designed to perform well while being computationally efficient.

## The Code:
```python
import gradio as gr
from transformers import pipeline

# Define the sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Define a function to analyze the mood based on user input
def analyze_mood(user_input):
    # Get the result from the model
    result = sentiment_analysis(user_input)[0]
    
    # Determine mood and provide suggestions
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
interface = gr.Interface(fn=analyze_mood, inputs=inputs, outputs=outputs, title="Mood Analyzer")

interface.launch()

## Limitations:
- The model i used is pretty good but sometimes it doesn't catch the complex feelings well, so it might get the mood wrong.

- It's trained on English texts mostly, so it might not get things right with other languages or specific ways people talk.

- The tips it gives based on your mood are very basic and might not fit everyone or every situation.

## Challenges:
**Model Limitations:** The model does well for simple sentiments but may not fully capture complex emotional moods.

## Next Steps:
Future improvements might include using more advanced models for better emotional understanding or creating a custom model for specific text types. Adding arabic version.

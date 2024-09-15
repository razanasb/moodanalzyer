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
```

## Limitations:
- The model i used is pretty good but sometimes it doesn't catch the complex feelings well, so it might get the mood wrong.

- It's trained on English texts mostly, so it might not get things right with other languages or specific ways people talk.

- The tips it gives based on your mood are very basic and might not fit everyone or every situation.

## Next Steps:
Future improvements might include using more advanced models for better emotional understanding or creating a custom model for specific text types. Adding arabic version.

## Code Explaination :
https://youtu.be/W0QNDh5s?s7gZ

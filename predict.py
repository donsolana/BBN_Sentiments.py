from transformers import pipeline
import torch


def predict(data):
    """Predicts sentiment and score """
    
    # Load the model
    senti_pipeline = pipeline('sentiment-analysis', model="cardiffnlp/twitter-roberta-base-sentiment-latest")
    
    def sentiment(text):
        "Takes text as input and returns sentiment label and score"
        pipeline_output = senti_pipeline(text)
        label =  pipeline_output[0]['label']
        return label

    data['sentiment'] = data['tweets'].apply(sentiment)
    
    return data
    





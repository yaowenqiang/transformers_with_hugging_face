from transformers import pipeline
import torch
import pandas as pd
print(torch.cuda.is_available())
#print(torch.cuda.current_device())
classifier = pipeline("sentiment-analysis", device=0)
df_ = pd.read_csv('csvfile_path')

print(df_head())
df = df_[['aireline_sentiment', 'text']].copy()
df['aireline_sentiment'].hist()
df = df[df.aireline_sentiment != 'neutral'].copy()

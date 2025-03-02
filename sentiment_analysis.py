from transformers import pipeline

# 加载情感分析模型
sentiment_analyzer = pipeline("sentiment-analysis")

# 分析情感
result = sentiment_analyzer("I love this product! It's amazing.")
print(result)

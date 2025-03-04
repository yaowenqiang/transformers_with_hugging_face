from transformers import pipeline

featurizer = pipeline('feature-extraction')
result = featurizer('Here is my text')
print(result)

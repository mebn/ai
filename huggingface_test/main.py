from transformers import pipeline

classifier = pipeline("text-generation")

res = classifier("what is the capital of sweden?")
print(res)
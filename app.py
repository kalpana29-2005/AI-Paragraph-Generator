from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

# Take input
topic = input("Enter topic: ")

# Generate text
result = generator(topic, max_length=60, num_return_sequences=1)

# Output
print("\nGenerated Paragraph:\n")
print(result[0]["generated_text"])

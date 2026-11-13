from transformers import pipeline

model_id = "google/gemma-3-4b-it"
pipe = pipeline("image-text-to-text", model=model_id)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Explain what a Hugging Face pipeline does in one sentence."}
        ],
    }
]

output = pipe(text=messages, max_new_tokens=100)
print(output[0]["generated_text"][-1]["content"])

import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Purnesh Kalavagunta"

tokens = enc.encode(text)

print("Tokens", tokens)

# Tokens [25216, 3274, 0, 3673, 1308, 382, 398, 494, 8382, 22187, 66525, 23235]

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 398, 494, 8382, 22187, 66525, 23235])

print("Decoded Tokens : ", decoded)
# Estruturas Condicionais
## If
model = "gpt-5.1"

if "gpt" in model:
    print("Model is GPT")

## If-else
if "gpt" in model:
    print("Model is GPT")
else:
    print("Model is not GPT")

## If-elif-else
if "gpt" in model:
    print("Model is GPT")
elif "gemini" in model:
    print("Model is Gemini")
else:
    print("Model is not GPT or Gemini")
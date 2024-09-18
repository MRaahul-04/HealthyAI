# chatbot.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Function to load the chatbot model and tokenizer
def load_model():
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    return tokenizer, model

# Load the chatbot model and tokenizer at the start
tokenizer, model = load_model()

# Function to process incoming user messages and generate a response
def generate_response(message, tokenizer, model):
    inputs = tokenizer.encode(message, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)

    return response

# Process message fallback
def process_message(message):
    response = "I'm here to help with your health and mental well-being!"
    return response
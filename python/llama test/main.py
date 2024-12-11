import re
from llama_cpp import Llama

# Load the model
model = Llama(model_path="/home/abdullah/mymodels/qwen1_5-4b-chat-q4_k_m.gguf", n_ctx=512, verbose=False)

def chatbot():
    print("Chatbot is ready! Type 'quit' to exit.")
    
    conversation_history = ["You: Please respond in English."]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        
        # Add user input to the conversation history
        conversation_history.append(f"You: {user_input}")
        
        # Prepare prompt by joining conversation history with the new user input
        prompt = "\n".join(conversation_history) + "\nBot:"
        
        # Generate response from the model
        response = model(prompt, max_tokens=100)  # adjust `max_tokens` as needed
        
        # Extract text from the response object
        bot_response = response["choices"][0]["text"].strip()
        math_expression = re.search(r'(\d+\s*[\+\-\*/]\s*\d+)', user_input)
        if math_expression:
            try:
                correct_answer = eval(math_expression.group(0))
                bot_response = f"{math_expression.group(0)} is {correct_answer}."
            except:
                pass
        # Add bot response to history and display it
        conversation_history.append(f"Bot: {bot_response}")
        print("Bot:", bot_response)

chatbot()
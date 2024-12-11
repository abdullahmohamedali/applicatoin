from llama_cpp import Llama
llm = Llama(
        verbose=False,
        model_path="/home/abdullah/mymodels/qwen1_5-4b-chat-q4_k_m.gguf",
        chat_format="llama-2"
)
llm.create_chat_completion(
        messages = [
            {"role": "system", "content": "you are helpfull assistant and answer my questions"},
            {
                "role": "user",
                "content": "hello how are you"
            }
        ]
)



# print(out.items)
# while True:
#     user_msg = input("user:")
#     print(f"model:{send(user_msg)}")

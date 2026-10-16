print("Bot: Hi! Type bye to exit")
while True:
    user = input("You: ").lower()
    if user in ["hi", "hello"]: print("Bot: Hi!")
    elif "how are you" in user: print("Bot: I'm fine, thanks!")
    elif "name" in user: print("Bot: I'm CodeAlpha Bot")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else: print("Bot: Sorry, I don't understand")
import random
def chatbot_response(user_input):
    user_input=user_input.lower().strip()
    if any(a in user_input for a in["hi","hello","nice to meet you"]):
        return random.choice(["hi , how are you?", "hello!how may i help you"])
    elif any (b in user_input for b in["can you help me ","help me","can you help","i need help","can you assist"]):
        return random.choice(["Im here to help","sure,how can i help you","of course, go ahead","lets solve it"])
    elif any (c in user_input for c in["who are you","what are you","are you human","tell about yourself"] ):
        return random.choice(["Im a virtual assiatant","Im a chatbot , I live in computer system data ","Im chatbot ,My purpose is to chat with you and help you "])
    elif any(d in user_input for d in["how are you","are you fine","are you okay","how r u","you good"]):
        return random.choice(["Im fine , thank you for asking","Im good , what about you?","Im doing fine , and you?","Im good here, thanks!"])
    elif any(e in user_input for e in["good morning","good afternoon","good evening","greeting"]):
        return random.choice(["good day to you" , "good day!how can i help you?","Hello! How may i assist?",])
    elif any(f in user_input for f in["this is confusing","im lost","explain again","what does this mean"]):
        return random.choice(["let me simplify it","i'll explain it step by step","lets break it down"])
    elif any(g in user_input for g in["code not working","fix this code","explain this program","whats the error"]):
        return random.choice(["i see a syntax error","let me correct it","here's the fix"])
    elif any(h in user_input for h in["explain this","define this","give example","what is this concept"]):
        return random.choice(["here's the defination","this concept means...","i'll explain it simply"])
    elif any(i in user_input for i in["what should i do","give advice","quide me","help me decide"]):
        return random.choice(["i'll give you options","think longterm","i'll give you honest advice","here's the pros and cons"])
    elif any(j in user_input for j in["im bored","talk to me","say something","entertain me","lets chat"]):
        return random.choice(["sure,lets talk","want a funtalk","im here","how's ur day going"])
    elif any(k in user_input for k in["im tired","im stressed","feeling low","im frustrated","not feeling good"]):
        return random.choice(["that sounds tough","take a deep breath","im listening","want to talk about it?"])
    elif any(l in user_input for l in["what if","is it possible","why is that","how does this work"]):
        return random.choice(["good question","let me explain","there's a reason behind it"])
    elif any(m in user_input for m in["summarise this","make it shorter"]):
        return random.choice(["ok let me explain","sure i will help you",])
    elif "thankyou" in user_input or "thanks" in user_input or "thats all" in user_input:
        return random.choice(["You're welcome","Happy to help","glad it helped","anytime"])
    else:
        return random.choice(["I do not understand that can you rephrase it","could you be more specific","i dint understand that"])
def run_chatbot():
    print("chat with chatbot(write exit to end)")
    while True:
        user_input=input("you:")
        if user_input.lower()=="exit":
            print("bye")
            break
        response=chatbot_response(user_input)
        print("chatbot:",response)
if __name__=="__main__":
    run_chatbot()
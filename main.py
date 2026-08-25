from chatbot import ai_answer



def start_chat():

    while True:

        question=input("你:")


        if question=="exit":

            print("KK:再见")

            break


        answer=ai_answer(question)





if __name__=="__main__":

    start_chat()
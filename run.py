import os
from dotenv import load_dotenv
from tkinter import filedialog
from esr.esr import *
from model.model import *

def extract_question(text):
    question_index = text.find("Question:")
    if question_index != -1:
        question = "Question: " + text[question_index + len("Question:"):].strip()
        return question
    else:
        return text


def ask_question(file_path, question, topic_sentences, hf_api_key, hf_model_id):
    sentences = extract_sentences(from_file(file_path))
    topic_sentences = format_sentences(rank_sentences(sentences, question)[:10])
    context = "\n".join(topic_sentences) + "\nQuestion: " + question + "\nAnswer: "
    response = query(context, hf_api_key, hf_model_id)
    os.system('clear')
    print(extract_question(response))
    return topic_sentences, response

if __name__ == "__main__":
    load_dotenv()
    hf_api_key = os.environ["HF_API_KEY"]
    hf_model_id = os.environ["HF_MODEL_ID"]
    file_path = filedialog.askopenfilename()
    question = input("Question: ")
    if question == "exit":
        exit()
    topic_sentences, response = ask_question(file_path, question, [], hf_api_key, hf_model_id)
    while True:
        text = input('"q" for new question, "a" to continue current answer, "exit" to exit: ').lower()
        if text == "exit":
            break
        elif text == "q":
            question = input("Query: ")
            if question == "exit":
                break
            topic_sentences, response = ask_question(file_path, question, topic_sentences, hf_api_key, hf_model_id)
        elif text == "a":
            response = query(response, hf_api_key, hf_model_id)
            print(extract_question(response))

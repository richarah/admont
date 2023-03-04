from tkinter import filedialog
from esr.esr import *
from model.model import *
from dotenv import load_dotenv
import os



if __name__ == "__main__":
    load_dotenv()
    hf_api_key = os.environ["HF_API_KEY"]
    hf_model_id = os.environ["HF_MODEL_ID"]
    
    file_path = filedialog.askopenfilename()

    question = input("Query: ")
    
    sentences = extract_sentences(from_file(file_path))
    topic_sentences = format_sentences(rank_sentences(sentences, question)[:10])
    
    # WIP: BLOOM integration
    # Create context
    context = "\n".join(topic_sentences) + "\nQuestion: " + question + "\nAnswer: "
    response = query(context, hf_api_key, hf_model_id)
    print(response)
    while True:
        text = input('"q" for new question, "a" to continue current answer, "exit" to exit: ').lower()
        if text.lower() in "exit":
            break
        elif text.lower() in "q":
            # TODO: DRY this mess w/ Codex
            os.system('clear')
            question = input("Query: ")
            sentences = extract_sentences(from_file(file_path))
            topic_sentences = format_sentences(rank_sentences(sentences, question)[:10])
            context = "\n".join(topic_sentences) + "\nQuestion: "
            response = query(context, hf_api_key, hf_model_id)
            print(response)
        elif text.lower() in "a":
            os.system('clear')
            context = response
            response = query(context, hf_api_key, hf_model_id)
            print(response)
            
    

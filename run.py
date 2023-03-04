from tkinter import filedialog
from esr.esr import rank_sentences
from model import *

if __name__ == "__main__":
    file_path = filedialog.askopenfilename()
    query = input("Query: ")
    sentences = extract_sentences(from_file(file_path))
    result = format_sentences(rank_sentences(sentences, query)[:10])
    for sent in result:
        print(sent.strip())
    # WIP: BLOOM integration


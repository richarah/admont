# admont

A chatbot and accompanying utilities, designed with the aim of helping users answer questions about and make sense of large piles of unstructured data. It is currently designed to work with text files, with support for other formats & processing entire directories to be implemented in the future.

#### Why not just use e.g. GODEL?

Different approaches for different problems.

While extractive models such as GODEL offer better all-round performance, Admont as a whole is more geared towards "messy", unstructured corpora and zero-shot training (ie. no examples).

However, due to huge strides in LLM development, programmatically-generated training examples & text preprocessing may prove a better approach.

#### What's in a name?

Named after [Admont Abbey](https://en.wikipedia.org/wiki/Admont_Abbey), which holds the record for the largest monastic library in the world.

## Usage

#### #### A note on HuggingFace API

Admont requires a HuggingFace API key and model ID to work - this is set in the `.env` file of the root directory:

```
HF_API_KEY=(your API key)
HF_MODEL_ID=bigscience/bloom	# default, this may be any text-generation model
```

#### Running Admont

To use admont, navigate to the project directory and run the `run.py` file. This will launch the chatbot and prompt the user for a text file:

`python run.py`

Once a file has been selected, the user is prompted for a question. The chatbot then searches the file for relevant information and returns an answer. After receiving an answer, the user can enter a command to either move on to the next question, continue writing on the current answer or exit the program.

The available commands are:

- "q": move on to the next question.
- "a": continue writing on the current answer.
- "exit": close the program.

## Limitations

#### Input format

Admont is currently limited to working with single text files. Support for processing multiple files and directories is planned for future releases.

#### Garbage in, garbage out

Providing a query unrelated to the text corpus may also result in bizarre responses (notably, providing it a knowledge base of cryptography lectures and subsequently asking it to bake a cake caused the chatbot to respond in Japanese)

It is also worth noting that the chatbot's accuracy is dependent on the quality of the data provided, and even in ideal circumstances it may not always provide the correct answer.

#### Known bugs/quirks

As it is based on a text-generation algorithm and not an extractive question-answering program, this part of the program retains a few quirks: notably, the program itself has a tendency to start "asking questions" after providing an answer.

import pandas as pd
import json


# read csv data
data_df = pd.read_csv('author_data.csv')


# Split the data into train, valid, and test DataFrames
train_df = data_df[data_df['train_ix'] == 'train']
valid_df = data_df[data_df['train_ix'] == 'valid']
test_df = data_df[data_df['train_ix'] == 'test']

# Function to append a document to the formatted data list
# Function to append a document to the formatted data list
def append_document(formatted_data, text, prompt_len, label):
    if text:
        print('='*100)
        print('\n\n\n')
        print(text[:prompt_len])
        print('\n\n\n')
        print(text[prompt_len:])
        print(label)
        print('\n\n\n')
        formatted_data.append({
            "text": text,
            "prompt_len": prompt_len,
            "label": label
        })

def obtain_jsonl(data_df, data_type):

    # Process the data to create multiple documents per session with varying labels
    formatted_data = []
    current_session = ""
    current_text = ""
    prompt_len = 0
    current_label = ""

    for idx, entry in data_df.iterrows():
        if entry["session_id"] != current_session:
            # Append the previous document if it exists
            if current_label == 'user':
                current_label = 'api'
            append_document(formatted_data, current_text, prompt_len, current_label)

            # Start a new document
            current_session = entry["session_id"]
            current_text = entry["sentence_text"]
            current_label = entry["sentence_source"]
            prompt_len = len(current_text) if current_label == "user" else 0
        else:
            if current_label != entry["sentence_source"]:
                if current_label == "user":
                    prompt_len = len(current_text)
                    current_text += " " + entry["sentence_text"]
                else:

                    if entry["sentence_source"] == "user":
                        # non-user to user
                        append_document(formatted_data, current_text, prompt_len, current_label)
                        current_text = entry["sentence_text"]
                        prompt_len = len(current_text)
                        current_label = entry["sentence_source"]
                    else:
                        # non-user to another non-user
                        append_document(formatted_data, current_text, prompt_len, current_label)
                        current_text = entry["sentence_text"]
                        prompt_len = 0
                        current_label = entry["sentence_source"]

                current_label = entry["sentence_source"]
            else:
                if entry["sentence_source"] == "user":
                    current_text += " " + entry["sentence_text"]
                    prompt_len = len(current_text)
                else:
                    current_text += " " + entry["sentence_text"]

    if current_label == 'user':
        current_label = 'api'
    # Append the last document
    append_document(formatted_data, current_text, prompt_len, current_label)

    # Convert the result to JSON format
    jsonl_data = "\n".join(json.dumps(doc) for doc in formatted_data)

    # write to jsonl file
    with open(data_type + '.jsonl', 'w') as f:
        f.write(jsonl_data)
        f.close()

obtain_jsonl(train_df, 'train')
obtain_jsonl(valid_df, 'valid')
obtain_jsonl(test_df, 'test')
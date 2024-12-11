import csv
import json
import random
#this code converts a .csv dataset to a jsonl and splits it to 80% training and 20% validation
def csv_to_chat_jsonl(csv_file, train_jsonl_file, val_jsonl_file, train_ratio=0.8):
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)       
        data = []

        for row in reader:
            prompt = row[0]
            answer = row[1]
           
            chat_data = {
                "messages": [
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": answer}
                ]
            }
            data.append(chat_data)

        random.shuffle(data)


        split_index = int(len(data) * train_ratio)
        train_data = data[:split_index]
        val_data = data[split_index:]

        with open(train_jsonl_file, 'w', encoding='utf-8') as train_file:
            for entry in train_data:
                train_file.write(json.dumps(entry) + "\n")

        with open(val_jsonl_file, 'w', encoding='utf-8') as val_file:
            for entry in val_data:
                val_file.write(json.dumps(entry) + "\n")

csv_to_chat_jsonl("Dataset.csv", "Dataset_train.jsonl", "Dataset_val.jsonl")

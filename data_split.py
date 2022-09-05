import json
import os

data_paths = [
    r'F:\project\python\line_generator\asset\address.json',
    r'F:\project\python\line_generator\asset\company.json',
    r'F:\project\python\line_generator\asset\gender.json',
    r'F:\project\python\line_generator\asset\job.json',
    r'F:\project\python\line_generator\asset\mail.json',
    r'F:\project\python\line_generator\asset\name.json',
    r'F:\project\python\line_generator\asset\phone.json',
]

train_data = []
valid_data = []
for data_path in data_paths:
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    train_len = int(len(data) * 0.95)
    train_data.extend(data[:train_len])
    valid_data.extend(data[train_len:])

save_path = r'F:\project\python\line_generator\material'
with open(os.path.join(save_path, 'train.json'), 'w', encoding='utf-8') as f:
    print(len(train_data))
    f.write(json.dumps(train_data, indent=4))
with open(os.path.join(save_path, 'valid.json'), 'w', encoding='utf-8') as f:
    print(len(valid_data))
    f.write(json.dumps(valid_data, indent=4))

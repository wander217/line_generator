import json
import os
import textwrap
import pandas as pd

phone = []
address = []
name = []
data_path = r'F:\project\python\line_generator\raw\7.600 NHA GIAU HCM.xls'
for s_name in ["Sheet1", "Sheet2"]:
    data = pd.read_excel(data_path, sheet_name=s_name)
    for idx, item in data.iterrows():
        contents = [
            "Số điện thoại: ",
            "Điện thoại: ",
            ""
        ]
        for content in contents:
            phone.append(content + str(item['Di động']).strip())
        contents = [
            "2. Địa chỉ trụ sở chính: ",
            "Nơi đăng ký hộ khẩu thường trú: ",
            "Chỗ ở hiện tại: ",
            ""
        ]
        for content in contents:
            address.extend(textwrap.wrap(content + item['Địa chỉ'].strip(), 100))
        contents = [
            "Họ và tên",
            ""
        ]
        for content in contents:
            name.extend(textwrap.wrap(item['Họ Tên'].strip(), 100))

data_path = r'raw/12 000 DOANH NGHIEP MOI THANH LAP NAM 2010.xls'
data = pd.read_excel(data_path, sheet_name="Sheet1")
job = []
company = []
mail = []
for item in data['E-MAIL'].dropna().tolist():
    for content in ["Email: ", "Fax: ", ""]:
        mail.append(content + item)
for idx, item in data.iterrows():
    contents = [
        "Tên ngành nghề kinh doanh: ",
        ""
    ]
    for content in contents:
        job.extend(textwrap.wrap(content + item['NGANH'].strip(), 100))
    contents = [
        "Tên công ty viết bằng tiếng việt: ",
        "Tên công ty viết bằng tiếng nước ngoài: ",
        "Tên công ty viết tắt: ",
    ]
    for content in contents:
        company.extend(textwrap.wrap(content + item['DOANH NGHIEP'].strip(), 100))

save_path = r'F:\project\python\line_generator\asset'
with open(os.path.join(save_path, 'phone.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(set(phone)), indent=4))
with open(os.path.join(save_path, 'address.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(set(address)), indent=4))
with open(os.path.join(save_path, 'name.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(set(name)), indent=4))
with open(os.path.join(save_path, 'job.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(set(job)), indent=4))
with open(os.path.join(save_path, 'mail.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(set(mail)), indent=4))
with open(os.path.join(save_path, 'company.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps(list(set(company)), indent=4))
with open(os.path.join(save_path, 'gender.json'), 'w', encoding='utf-8') as f:
    f.write(json.dumps([
        "Nam/nữ: Nam",
        "Nam/nữ: Nữ",
        "Nam/nữ: nữ",
        "Nam/nữ: nam",
        "Giới tính: nam",
        "Giới tính: nữ",
        "Giới tính: Nam",
        "Giới tính: Nữ",
        "- Nam",
        "- Nữ",
    ], indent=4))

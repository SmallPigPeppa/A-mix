import json

# 读取原始数据
with open('input/llava_v1_5_mix665k-ocr_vqa-Aold-deduped.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 计算每个分文件应该包含的数据量
total_entries = len(data)
entries_per_part = total_entries // 10

# 分解数据到各个部分
for i in range(10):
    start_index = i * entries_per_part
    # 对最后一个文件进行特殊处理，以包含所有剩余的数据
    if i == 9:
        end_index = total_entries
    else:
        end_index = start_index + entries_per_part
    part_data = data[start_index:end_index]

    # 写入数据到新的json文件
    part_filename = f'part{i + 1}.json'
    with open(part_filename, 'w', encoding='utf-8') as part_file:
        json.dump(part_data, part_file, ensure_ascii=False, indent=4)

    print(f'Created {part_filename} with {len(part_data)} entries.')

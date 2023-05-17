import json
import csv
import sys


def json_to_csv(json_file, csv_file):
    # 读取JSON文件
    with open(json_file, 'r') as f:
        data = json.load(f)

    # 获取所有字段名
    fieldnames = list(data.keys())

    # 创建CSV文件并写入字段名
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # 写入JSON数据到CSV文件
        writer.writerow(data)


# main
if __name__ == '__main__':
    json_file = sys.argv[1]
    csv_file = sys.argv[2]
    json_to_csv(json_file, csv_file)

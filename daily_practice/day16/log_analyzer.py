"""
日志分析工具
- 读取日志文件
- 提取每行的 IP 地址
- 统计每个 IP 出现的次数
- 将结果写入 CSV 文件
"""

import csv
from collections import Counter
from file_utils import read_lines_generator
from regex_utils import extract_ip
from decorator_utils import decorator_time

@decorator_time
def analyze_log(file_path, output_csv):
    """
    分析日志文件，统计 IP 出现次数，写入 CSV

    参数:
        file_path: 日志文件路径
        output_csv: 输出的 CSV 文件路径
    """
    ip_counter = Counter()
    try:
        for line in read_lines_generator(file_path):
            ip_addr = extract_ip(line)
            if ip_addr:
                ip_counter[ip_addr] += 1
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到")
        return
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return

    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['IP', 'Count'])
            for ip_addr, count in ip_counter.items():
                writer.writerow([ip_addr, count])
        print(f"统计完成，结果已保存至 {output_csv}")
    except IOError as e:
        print(f"写入 CSV 文件失败：{e}")

if __name__ == "__main__":
    analyze_log('access.log', 'ip_count.csv')
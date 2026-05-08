from collections import Counter
import string


def read_file(file_path):
    """读取文件内容并返回文本字符串"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('错误：找不到文件')
        return ""


def clean_word(word):
    """去除单词两端标点符号并转为小写"""
    return word.strip(string.punctuation).lower()


def tokenize(text):
    """将文本拆分为单词列表，并清洗每个单词"""
    a = text.split()
    b = [clean_word(word) for word in a]
    return b


def count_word_frequency(source):
    """
    统计词频，支持两种输入方式：
    - 传入 .txt 文件路径：自动读取文件内容
    - 传入普通字符串：直接统计
    """
    # 判断是文件路径还是普通字符串
    if isinstance(source, str) and source.endswith(".txt"):
        text = read_file(source)
        if not text:
            return Counter()
    else:
        text = source

    # 分词并统计词频
    text_list = tokenize(text)
    return Counter(text_list)


def display_result(counter):
    """打印词频统计结果，按出现次数从高到低排列"""
    if not counter:
        print("没有数据")
        return

    print("词频统计结果：")
    for word, count in counter.most_common():
        print(f"{word}: {count}")


if __name__ == "__main__":
    # 测试1：直接统计字符串
    text = "Hello world! hello python. Hello WORLD"
    result = count_word_frequency(text)
    display_result(result)

    # 测试2：统计文件内容（路径用正斜杠避免转义问题）
    result2 = count_word_frequency('daily_practice/day8/sample.txt')
    display_result(result2)

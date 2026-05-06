def split_string(s, delimiter):
    """Splits the input string `s` using the specified `delimiter` and returns a list of substrings."""
    return s.split(delimiter)

def reverse_string(s):
    """Reverses the input string `s` and returns the reversed string."""
    return s[::-1]

def count_vowels(s):
    """Counts the number of vowels in the input string `s` and returns the count."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    """检查输入字符串 `s` 是否是回文字符串（忽略大小写和空格）。"""
    # 移除空格并转换为小写
    s = s.replace(" ", "").lower()
    # 反转字符串
    reversed_s = s[::-1]
    # 比较原字符串和反转后的字符串
    return s == reversed_s
# 创建测试文件（运行一次即可）
def create_test_file():
    content = """第一行：这是第1行
第二行：这是第2行
第三行：这是第3行
第四行：这是第4行
第五行：这是第5行
第六行：这是第6行
第七行：这是第7行
第八行：这是第8行
第九行：这是第9行
第十行：这是第10行"""
    
    with open("test_file.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("test_file.txt 已创建")

# 执行创建
create_test_file()
import os
# 以下编码用以将字符串输入到粘贴板,不可输出列表文件
# import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
def muti_input():
    list = []
    merge = ""
    # 用于获取控制台多行输入
    # iter函数用于生成迭代器
    for line in iter(input, ''):
        list.append(line.replace(',', ''))
    for str in list:
        merge += str
        merge += " "
    if merge == " ":
        return ""
    return merge
def readme():
    print("-" * 50)
    print("本软件可以将多行字符串拼接成一行，如：\n"
          "一次性粘贴进多行内容\n"
          "aa\n"
          "bb\n"
          "cc\n"
          "...\n"
          "回车后即可得到拼接后字符串\n"
          "aa bb cc ...\n"
          "且拼接内容会直接复制到系统剪切板，供粘贴使用！")
    print("*" * 50)


print("*" * 50)
print("欢迎使用字符串拼接器 V1.1!")
input("按回车键查看使用说明！")
readme()
print("请输入需要拼接的多行字符串，按回车键结束！")
print("*" * 50)

while True:
    merge = muti_input()
    if merge == "":
        break
    print("拼接完成，拼接结果已经复制到剪切板！")
    print("请输入下一项需要拼接的字符串或直接回车退出程序！")
    addToClipBoard(merge)


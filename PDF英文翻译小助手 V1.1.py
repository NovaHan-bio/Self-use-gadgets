# 作者：红色甲基橙
# 邮箱：371790283@qq.com
# 版本 V1.0

def translate(words):
    # 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
    # coding=utf-8

    import http.client
    import hashlib
    import urllib
    import random
    import json

    appid = '20170814000073448'  # 填写你的appid
    secretKey = 'eHo6dfncP6W0vlk4BnQD'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'  # 原文语种
    toLang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    q = words
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        # 将result中的翻译后结果提取出
        list = result["trans_result"]

        for dic in list:
            zh_result = dic["dst"]
            ori_str = dic["src"]

        return zh_result

    except Exception as e:
        return "网络连接失败，请等待网络稳定后重试。"
    finally:
        if httpClient:
            httpClient.close()

import os
# 以下编码用以将字符串输入到粘贴板,不可输出列表文件
# import os
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
# 以下代码用于获取控制台多行输入
def muti_input():
    list = []
    merge = ""
    # 用于获取控制台多行输入
    # iter函数用于生成迭代器
    for line in iter(input, ''):
        list.append(line.replace(',', ''))
        if line == "exit": # 尝试输入一个空格来退出
            return "exit"
        elif line == "":
            break
    for str in list:
        merge += str
        merge += " "
    # if merge == " ":
    #     return ""
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


print("*" * 70)
print("欢迎使用PDF英文翻译小助手 V1.0!")
print("")
print("本程序可将带有换行的英文句子拼成一句，再翻译成中文，并同时输出原文和翻译结果。")
print("")
print("本程序翻译功能需联网实现，如程序发生错误或有建议请发邮件至371790283@qq.com")
print("")
print("请将从PDF中复制的段落粘贴至窗口，按两次回车键结束！")
print("*" * 70)

while True:
    merge = muti_input()
    if merge == "exit":
        break
    zh = translate(merge)
    print("=" * 70)
    print("翻译的原文是:")
    print(merge)
    print("翻译后的中文结果是:")
    print("")
    print(zh)
    print("")
    print("=" * 70)
    print("请输入下一段需要翻译的段落并按两次回车键结束，或输入“exit”后按回车键退出程序！")

    # print("拼接完成，拼接结果已经复制到剪切板！")
    # print("请输入下一项需要拼接的字符串或直接回车退出程序！")
    # addToClipBoard(merge)



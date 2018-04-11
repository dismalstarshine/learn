import os


def find(key, a=os.path.abspath('.')):  # key 是要查找的字符串，a 为当前路径
    for root, dirs, files in os.walk(a):  # 使用walk 函数进行目录遍历
        allpaths = []  # 所有文件路径存为列表
        for everyone in files:  # 从files 导入所有文件
            allpaths.append(os.path.join(root, everyone))  # 路径合成

        for i in allpaths:
            if key in os.path.split(i)[1]:  # 路径拆分，查找路径是否存在需要的字符串
                print(i)  # 打印包含该字符串文件的绝对路径

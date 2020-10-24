# -*- coding: utf-8 -*-
# @Time : 2020/10/24 14:40
# @Author : Jclian91
# @File : read_corpus.py
# @Place : Yangpu, Shanghai

# 读取文件
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    return content


# MSRA语料
msra_train = read_file("./data/BIO_train.txt")
msra_test = read_file("./data/BIO_test.txt")

# Chinese NER语料
example_train = read_file("./data/example.train")
example_dev = read_file("./data/example.dev")
example_test = read_file("./data/example.test")

# 形成新的数据文档
with open("./data/ner_train.txt", "w", encoding="utf-8") as f:
    for line in msra_train:
        f.write(line.replace("\t", "\tn\t"))

    for line in example_train:
        f.write(line.replace(" ", "\t").replace("\t", "\tn\t"))

with open("./data/ner_test.txt", "w", encoding="utf-8") as f:
    for line in msra_test:
        f.write(line)

    for line in example_dev:
        f.write(line.replace(" ", "\t").replace("\t", "\tn\t"))
    for line in example_test:
        f.write(line.replace(" ", "\t").replace("\t", "\tn\t"))

# -*- coding: utf-8 -*-
# @Time : 2020/10/20 13:46
# @Author : Jclian91
# @File : predict_crf.py
# @Place : Yangpu, Shanghai
import CRFPP
CRF_MODEL_PATH = "model"


# 利用CRF实现中文NER功能
def crf_chinese_ner(text):
    """
    :param text: type: string, 需要进行中文NER的文档
    :return: {"document": "...", "entities": [{"name": ..., "type": ..., "index": ...}, ..., ...]}
    """
    # 加载模型文件
    tagger = CRFPP.Tagger("-m %s" % CRF_MODEL_PATH)
    tagger.clear()
    for word in text:
        tagger.add("{}\tn\tO".format(word))
    tagger.parse()
    size = tagger.size()

    # 获取模型预测标签
    predict_tags = []
    for i in range(0, size):
        tag = tagger.y2(i)
        predict_tags.append(tag)

    # 对预测标签进行后处理，得到中文分词后的结果
    entities = []
    for i in range(len(predict_tags)):
        word = ""
        if predict_tags[i] == "B-LOC":
            word += text[i]
            j = i + 1
            while j < len(text) and predict_tags[j] == "I-LOC":
                word += text[j]
                j += 1

        if word:
            entities.append([{"name": word, "type": "LOC", "index": i}])

        word = ""
        if predict_tags[i] == "B-PER":
            word += text[i]
            j = i + 1
            while j < len(text) and predict_tags[j] == "I-PER":
                word += text[j]
                j += 1

        if word:
            entities.append([{"name": word, "type": "PER", "index": i}])

        word = ""
        if predict_tags[i] == "B-ORG":
            word += text[i]
            j = i + 1
            while j < len(text) and predict_tags[j] == "I-ORG":
                word += text[j]
                j += 1

        if word:
            entities.append([{"name": word, "type": "ORG", "index": i}])

    return {"document": text, "entities": entities}


if __name__ == '__main__':
    text2 = "北京时间10月23日晚19点35分，2020年中超第二阶段第二轮（总第16轮）争冠组上海上港和上海申花的比赛，在苏州奥林匹克体育中心进行。第52分钟上港外援连续配合，奥斯卡外围送球，阿瑙后脚跟磕传，穆伊禁区内杀入拿球，艾迪从侧推倒穆伊，马宁判罚点球，胡尔克打球门左下角得分。"
    print(crf_chinese_ner(text2))

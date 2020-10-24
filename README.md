利用CRF++进行中文命名实体识别（NER）

维护者：lianmingjie

### 语料

- 微软中文NER语料(data/BIO_*.txt)
- ChineseNER Github项目的语料(data/example.*)

数据集处理脚本可以参考`read_corpus.py`。

### CRF模型训练

工具采用CRF++(因此系统中需要安装CRF++)，训练命令如下：

```shell script
crf_learn  -f 3 -c 4.0 template ./data/ner_train.txt model -t
```

### CRF模型评估

先使用如下命令生成模型预测文件：

```shell script
crf_test -m model ./data/ner_test.txt > crf_pred.txt
```

利用`model_evaluate_crf.py`脚本进行评估，评估结果如下：

```
accuary:  0.6799018474369504
p:  0.7088883506902398
r:  0.6612074320890043
f1:  0.6842182158197703
classification report: 
           precision    recall  f1-score   support

      LOC       0.99      0.66      0.79      8486
      PER       1.00      0.63      0.77      4721
      ORG       0.40      0.70      0.51      4500

micro avg       0.71      0.66      0.68     17707
macro avg       0.84      0.66      0.71     17707
```

### CRF模型预测

```
被誉为“中国遗传学之父”的谈家桢校友，他毕生追求真理，不屈服于任何非学术压力对遗传学的干扰，为推动中国生命科学迈向世界作出重大贡献。
[{'name': '中国', 'type': 'LOC', 'index': 4}], [{'name': '中国', 'type': 'LOC', 'index': 49}]

10月16日，教育部举行新闻发布会，教育部体育卫生与艺术教育司司长王登峰指出，学校的体育中考要不断总结经验，逐年增加分值，要达到跟语数外同分值的水平。
[{'name': '教育部', 'type': 'ORG', 'index': 7}], [{'name': '教育部体育卫生与艺术教育司', 'type': 'ORG', 'index': 18}], [{'name': '王登峰', 'type': 'PER', 'index': 33}]

10月15日，广州市花都区再次开展隔离酒店工作人员的定期检查，王某某核酸检测结果为阳性，已转入广州市第八人民医院隔离医学观察，目前没有发热、咳嗽等不适。
[{'name': '广州', 'type': 'LOC', 'index': 7}], [{'name': '王', 'type': 'PER', 'index': 31}], [{'name': '广州市第八人民医院', 'type': 'ORG', 'index': 47}]

长期以来，印度海军一直在积极推动建造第三艘航空母舰，但拉瓦特将军今年2月表示，印度政府可能暂时不会批准建造第三艘航母。
{'name': '印度海', 'type': 'LOC', 'index': 5}], [{'name': '拉瓦特', 'type': 'PER', 'index': 27}], [{'name': '印度', 'type': 'LOC', 'index': 39}]

当一篇描写北京郊区普通人生活的文章，冠以“名媛”的标题《昌平名媛生活指南》，就成了阅读量10万+的爆款文章。
[{'name': '北京', 'type': 'LOC', 'index': 5}]

北京时间10月23日晚19点35分，2020年中超第二阶段第二轮（总第16轮）争冠组上海上港和上海申花的比赛，在苏州奥林匹克体育中心进行。第52分钟上港外援连续配合，奥斯卡外围送球，阿瑙后脚跟磕传，穆伊禁区内杀入拿球，艾迪从侧推倒穆伊，马宁判罚点球，胡尔克打球门左下角得分。
[{'name': '上海上港', 'type': 'LOC', 'index': 42}], [{'name': '上海申花', 'type': 'ORG', 'index': 47}], [{'name': '苏州', 'type': 'LOC', 'index': 56}], [{'name': '奥林匹克体育中心', 'type': 'LOC', 'index': 58}], [{'name': '阿瑙', 'type': 'LOC', 'index': 91}], [{'name': '穆伊', 'type': 'PER', 'index': 99}], [{'name': '艾迪', 'type': 'PER', 'index': 109}], [{'name': '穆伊', 'type': 'PER', 'index': 115}], [{'name': '马宁', 'type': 'PER', 'index': 118}], [{'name': '胡尔克', 'type': 'PER', 'index': 125}]
```

### 中分分词服务

已将中文NER封装成HTTP服务，运行`flask_server.py`即可。
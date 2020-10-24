# -*- coding: utf-8 -*-
# @Time : 2020/10/24 15:00
# @Author : Jclian91
# @File : flask_server.py
# @Place : Yangpu, Shanghai
import traceback
from flask import Flask
from flask import request

from predict_crf import crf_chinese_ner

app = Flask(__name__)


# 利用CRF实现中文NER的接口
@app.route("/model/chinese_ner", methods=['GET', 'POST'])
def chinese_ner():
    return_dict = {"code": 200, "message": "success", "data": {}}
    try:
        # 利用CRF实现中文NER
        document = request.get_json()["document"].replace(" ", "")
        result = crf_chinese_ner(document)
        return_dict["data"] = result
    except Exception:
        return_dict["code"] = 400
        return_dict["message"] = traceback.format_exc()

    return return_dict


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
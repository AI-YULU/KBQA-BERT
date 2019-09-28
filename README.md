# KBQA-BERT
基于知识图谱的QA系统，BERT模型
需要下载BERT预训练模型（中文）chinese_L-12_H-768_A-12  https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip   解压缩后放在./ModelParams文件夹里面
需要在根目录建立Output文件夹存放模型参数文件
分为Output/NER（命名实体识别）文件夹和Output/SIM（相似度）文件夹

1.run_ner.sh训练（命名实体识别）

2.terminal_ner.sh（命名实体识别测试）

3.args.py

train = true 预训练模式

test = true 相似度测试

4.run_similarity 相似度的训练或测试（根据第3步的设置决定）

5.qa_my.sh（连接了本地的neo4j知识库）

问答

参考：https://github.com/WenRichard/KBQA-BERT

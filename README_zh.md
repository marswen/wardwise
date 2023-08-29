# Wardwise
A ward round assistant who helps medical personnel to query medical record data with LLM

中文 | [English](README.md)

### 背景
* 医务人员在查房会诊等临床行为中需要频繁查询患者的检查结果和进展情况。
* 从电子病历里查找信息时，会涉及时间条件、逻辑条件、术语标准化等推理过程，简单的结构化查询很难满足需求。
* 大语言模型改变了自然语言处理的任务逻辑，可以探索新的思路下的应用机会。


### 目标
* 建立电子病历和大语言模型推理的流程框架。
* 实现对电子病历信息的交互式问答接口。
* 探索不同场景和领域内使用大模型推理的最佳实践。


### 使用方法
* 加载数据：  
    `load_data.py`:  
        - `digest_doc`: 基于最小信息量模型，从纯文本里提取id和时间戳等必要信息。  
        - `load_std_data`: 从符合最小信息量模型的数据里加载数据。  
* 检索病历：  
    `query_record.py`: 找出符合要求的病历记录  
* 回答问题：  
    `answer_question.py`: 根据病历记录回答查询问题  
* 示例:  
见`example.py`

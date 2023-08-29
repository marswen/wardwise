# Wardwise

[中文](README_zh.md) | English


### Background
* In clinical activities such as ward rounds and consultations, medical staff need to frequently query patients' test results and progress.
* Searching for information from electronic medical records involves reasoning processes such as time conditions, logical conditions, and terminology standardization. Simple structured queries are difficult to meet the requirements.
* Large language models have changed the task logic of natural language processing and can explore application opportunities under new ideas.


### Objectives
* Establish a workflow framework for electronic medical records and large language model inference.
* Implement an interactive question-and-answer interface for electronic medical record information.
* Explore the best practices of using large model inference in different scenarios and domains.


### How to use
* Load Data:  
    `load_data.py`:    
        - `digest_doc`: Extract essential information such as ID and timestamps from plain text based on the minimal information model.  
        - `load_std_data`: Load data in standard fields.  
* Retrieve Medical Records:  
    `query_record.py`: Find medical records that meet the requirements.  
* Answer Questions:  
    `answer_question.py`: Answer query questions based on medical record entries.  
* Example:  
See`example.py`

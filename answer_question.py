
def answer(parser, record, question: str):
    """
    Provide answer for user's question
    :param parser: parser object from parsers module
    :param record: a Record object
    :param question: user's question
    :return: answer text
    """
    empty_output = '没找到'
    if record is None:
        return empty_output
    content = record.content
    output = parser.query_answer(content, question)
    return output

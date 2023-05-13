import re


def query_patient(records, patient_id: str):
    """
    query patient records by patient id
    :param records: a dict of MedicalRecord objects
    :param patient_id: a patient id
    :return: a MedicalRecord object for specific patient id
    """
    return records[patient_id]


def query_condition(parser, record, condition: str):
    """
    query specific record for one patient by a complex condition
    :param parser: parser object from parsers module
    :param record: a MedicalRecord for specific patient id
    :param condition: text describing complex query condition
    :return: a Record object matching condition
    """
    timeline = '\n\n'.join([f'编号：{i}\n时间：{e.timestamp}\n标题：{e.title}\n摘要：{e.abstract}'
                            for i, e in enumerate(record.records)])
    output = parser.query_lexical_chain(timeline, condition)
    result_no = re.search('<res>\s*(.+?)\s*</res>', output)
    if result_no is not None:
        result_no = int(result_no.group(1))
    else:
        return None
    if result_no == -1 or result_no >= len(record.records):
        return None
    else:
        return record.records[result_no]

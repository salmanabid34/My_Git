import requests
import csv
import json
url = '''
http://ClinicalTrials.gov/api/query/study_fields?expr=heart+attack&fmt=JSON&fields=NCTId,Condition,BriefTitle
'''
data = requests.get(url)
data_dict = data.json()
with open('StudyFeildsResponce.csv', 'w') as f:
    fieldname = ['APIVrs', 'DataVrs', 'Expression', 'NStudiesAvail', 'NStudiesFound', 'MinRank', 'MaxRank', 'NStudiesReturned', 'FieldList']
    file_ = csv.DictWriter(f, fieldname, delimiter='\t')
    file_.writeheader()
    data_mod = data_dict['StudyFieldsResponse'].items()
    final_data = {}
    counter = 0
    for idx,i in enumerate(data_mod):
        if idx < 9:
            final_data.update({i[0] : i[1]})
    file_.writerow(final_data)
    
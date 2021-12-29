import ast

def clean_data(data):
    data_str = str(data)
    if '\\n' in data_str or '\\r' in data_str:
        data_str = data_str.replace('\\r','').replace('\\n','')
    if '\n' in data_str or '\r' in data_str:
        data_str =  data_str.replace('\r','').replace('\n','')

    return ast.literal_eval(data_str)

import ast

def clean_array_to_export(data):
    if '\r' in data and '\\r' not in data:
        return ast.literal_eval(data.replace('\r','\\r').replace('\n','\\n'))

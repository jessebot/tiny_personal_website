import yaml

def get_global_variable(global_variable):
    """ gets global variable given string variable name"""
    with open('./config.yaml', 'r') as f:
        doc = yaml.load(f)
    txt = doc["Globals"][global_variable]
    return txt

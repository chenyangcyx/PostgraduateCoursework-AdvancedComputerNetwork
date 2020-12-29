import re

def shorten_int_name(interface_name):
    short = None
    regex = "(\w{2}).*?(\d+(?:/\d+)?(?:/\d+)?)"
    
    match = re.match(regex, interface_name)
    
    if match is not None:
        short = ""
        for group in match.groups():
            short += group
            
    return short


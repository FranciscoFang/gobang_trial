def search_for_4(chain) -> int:
    chain_str = ''.join(chain)
    if chain_str.find('BBBBOW') != -1: #4-0
        return 1
    elif chain_str.find('BBBBOO') != -1: 
        return 1
    elif chain_str.find('BBBBOZ') != -1:
        return 1
    elif chain_str.find('WOBBBB') != -1:
        return 1
    elif chain_str.find('OOBBBB') != -1:
        return 1
    elif chain_str.find('ZOBBBB') != -1:
        return 1
    elif chain_str.find('OBOBBBW') != -1: #1-3
        return 1
    elif chain_str.find('OBOBBBO') != -1: # 重复
        return 1
    elif chain_str.find('OBOBBBZ') != -1:
        return 1
    elif chain_str.find('WBOBBBO') != -1:
        return 1
    elif chain_str.find('ZBOBBBO') != -1:
        return 1
    elif chain_str.find('OBBOBBW') != -1: #2-2
        return 1
    elif chain_str.find('OBBOBBO') != -1: # 重复
        return 1
    elif chain_str.find('OBBOBBZ') != -1:
        return 1
    elif chain_str.find('WBBOBBO') != -1:
        return 1
    elif chain_str.find('ZBBOBBO') != -1:
        return 1
    elif chain_str.find('OBBBOBW') != -1: #3-1
        return 1
    elif chain_str.find('OBBBOBO') != -1: # 重复
        return 1
    elif chain_str.find('OBBBOBZ') != -1:
        return 1
    elif chain_str.find('WBBBOBO') != -1:
        return 1
    elif chain_str.find('ZBBBOBO') != -1:
        return 1
    else:
        return 0
    
def search_for_3(chain) -> int:
    chain_str = ''.join(chain)
    if chain_str.find('OBBBOOW') != -1: #3-0
        return 1
    elif chain_str.find('OBBBOOO') != -1: 
        return 1
    elif chain_str.find('OBBBOOZ') != -1: 
        return 1
    elif chain_str.find('WOOBBBO') != -1: 
        return 1
    elif chain_str.find('OOOBBBO') != -1: 
        return 1
    elif chain_str.find('ZOOBBBO') != -1: 
        return 1
    elif chain_str.find('WOBBOBOW') != -1: #2-1
        return 1
    elif chain_str.find('WOBBOBOO') != -1: 
        return 1
    elif chain_str.find('WOBBOBOZ') != -1: 
        return 1
    elif chain_str.find('OOBBOBOW') != -1: 
        return 1
    elif chain_str.find('OOBBOBOO') != -1: 
        return 1
    elif chain_str.find('OOBBOBOZ') != -1: 
        return 1
    elif chain_str.find('ZOBBOBOW') != -1: 
        return 1
    elif chain_str.find('ZOBBOBOO') != -1: 
        return 1
    elif chain_str.find('ZOBBOBOZ') != -1: 
        return 1
    elif chain_str.find('WOBOBBOW') != -1: #1-2
        return 1
    elif chain_str.find('WOBOBBOO') != -1: 
        return 1
    elif chain_str.find('WOBOBBOZ') != -1: 
        return 1
    elif chain_str.find('OOBOBBOW') != -1: 
        return 1
    elif chain_str.find('OOBOBBOO') != -1: 
        return 1
    elif chain_str.find('OOBOBBOZ') != -1: 
        return 1
    elif chain_str.find('ZOBOBBOW') != -1: 
        return 1
    elif chain_str.find('ZOBOBBOO') != -1: 
        return 1
    elif chain_str.find('ZOBOBBOZ') != -1: 
        return 1
    else:
        return 0
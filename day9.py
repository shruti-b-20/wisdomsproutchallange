def commanprefix(s):
    if not s:
        return ''
    prefix=s[0]
    for st in s[1:]:
        while  not st.startswith(prefix):
            prefix=prefix[:-1]
        if not prefix:
            return ''
    return prefix
strs = ["flower", "flow", "flight"]

#TESTCASES
print(commanprefix(["flower", "flow", "flight"]))  
print(commanprefix(["dog", "racecar", "car"]))     
print(commanprefix(["apple", "ape", "april"]))     
print(commanprefix([""]))                          
print(commanprefix(["alone"]))                     

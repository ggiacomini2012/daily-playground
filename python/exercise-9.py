list = ['bob', 'max', 'liberte']

def returnMaxLenString(param_list):
    return max(param_list, key=len)

print(returnMaxLenString(list))
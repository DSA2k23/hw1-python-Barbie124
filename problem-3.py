def basefourtobi(num):
    binary = bin(num)
    binary = binary[2:]
    return binary
 
def convert(num):
    resultstr = ""
    numstring = str(num)
    for i in numstring:
        i = int(i)
        if(i == 1 or i == 0):
            resultstr = resultstr+'0'
        binary = basefourtobi(i)
        resultstr = resultstr+binary
    resultstr = int(resultstr)
    return resultstr

Number = 11002233
print(convert(Number))

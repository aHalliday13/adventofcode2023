import os
cwd = os.path.dirname(__file__)
absPath = os.path.join(cwd, "input.txt")

lines=[""]
finalValue=0


with open(absPath,"r") as file:
    chars=file.read()
    for char in chars:
        if (char=="\n"):
            lines.append("")
        else:
            lines[-1]+=char
    for line in lines:
        foundDigits=0
        for forwardDigit in line:
            try:
                firstDigit=int(forwardDigit)
                break
            except ValueError:
                pass
        for reverseDigit in line:
            try:
                lastDigit=int(reverseDigit)
            except ValueError:
                pass
        for checkDigit in line:
            try:
                int(reverseDigit)
                foundDigits+=1
            except:
                pass
        if (foundDigits==1):
            finalValue+=firstDigit
        else: 
            finalValue+=((firstDigit*10)+lastDigit)
print(finalValue)
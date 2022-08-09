# Python_Random_Citizen_ID
สุ่มเลขบัตรประชาชน 13 หลัก Code สุ่มหมายเลขบัตรประจำตัวประชาชนคนไทย 13 หลัก
Thai Citizen ID generate
Thailand 


```python 
# (c)2022 Aniwat Ruttanaudom

import random

#----------------------

## สุ่มหมายเลขบัตรประชาชน

def randomCitizenID():
    i = 0
    firstNumber = ""
    numberCalc = 0
    k=0
    m=0
    while (i < 12):
        k = abs(i + (-13))
        m = random.randint(1, 9)
        firstNumber += str(m)
        # ตัวเลขชุดแรก (12 หลัก)
        numberCalc += k * m
        print("k=" + str(k) + ", m=" + str(m) + ", firstname=" + firstNumber + ", numberCalc=" + str(numberCalc))
        i += 1

    lastNumber = 11 - numberCalc % 11
    print("lastNumber="+str(lastNumber))
    # ตัวเลขหลักสุดท้าย
    return str(firstNumber) + str(lastNumber)

print(randomCitizenID(), end="")
```

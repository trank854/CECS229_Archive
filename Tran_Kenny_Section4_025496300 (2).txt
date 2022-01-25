#Kenny Tran 025496300
#CECS229 Lab 1
#2/8/21
def to_decimal(num, base):
        final = 0
        intlist = []
        for x in num:
                if x == 'A':
                        x = 10
                if x == 'B':
                        x = 11
                if x == 'C':
                        x = 12
                if x == 'D':
                        x = 13
                if x == 'E':
                        x = 14
                if x == 'F':
                        x = 15
                else:
                        int(x)
                intlist.append(x)
        exponent = len(intlist) - 1
        for z in intlist:
                if int(z) >= 1:
                        ans = int(z) * base**exponent
                        final = final + ans
                        exponent -= 1
                elif int(z) == 0:
                        exponent -= 1
        return final
			
def to_base(dec_num, base):
        hexdict = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
        remlist = []
        str1 = ''
        while dec_num != 0:
                remain = dec_num % base
                remlist.append(remain)
                dec_num = dec_num // base
        remlist.reverse()
        for x in remlist:
                if x < 10:
                        str1 = str1 + str(x)
                else:
                        str1 = str1 + hexdict[str(x)]
        return str1




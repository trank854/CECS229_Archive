#Kenny Tran
#CECS229 Lab 2
#2/15/21
def shift_cipher_encode(string, n):
        sent = ''
        for char in string:
                if char.isalpha() == True:
                        ascnum = ord(char)
                        ascnum = ascnum + n
                        if char.isupper() == True:
                                while ascnum > 90:
                                        ascnum = ascnum - 90
                                        ascnum = ascnum + 64
                        if char.islower() == True:
                                while ascnum > 122:
                                        ascnum = ascnum - 122
                                        ascnum = ascnum + 96
                else:
                        ascnum = ord(char)
                sent = sent + chr(ascnum)
        return sent

def shift_cipher_decode(string, n):
        sent = ''
        for char in string:
                if char.isalpha() == True:
                        ascnum = ord(char)
                        ascnum = ascnum - n
                        if char.isupper() == True:
                                while ascnum < 65:
                                        ascnum = 64 - ascnum
                                        ascnum = 90 - ascnum
                        if char.islower() == True:
                                while ascnum < 97:
                                        ascnum = 96 - ascnum
                                        ascnum = 122 - ascnum
                else:
                        ascnum = ord(char)
                sent = sent + chr(ascnum)
        return sent






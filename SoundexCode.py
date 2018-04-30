import math
import numpy as np
import hashlib
def SoundexCode(name):
        """Get the soundex code for the string"""
        name = name.upper()
        soundex = ""
        soundex += name[0]
        dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}
        for char in name[1:]:
                if (char in list(dictionary.keys())[0]):
                        code = dictionary[list(dictionary.keys())[0]]
                elif (char in list(dictionary.keys())[1]):
                        code = dictionary[list(dictionary.keys())[1]]
                elif (char in list(dictionary.keys())[2]):
                        code = dictionary[list(dictionary.keys())[2]]
                elif (char in list(dictionary.keys())[3]):
                        code = dictionary[list(dictionary.keys())[3]]
                elif (char in list(dictionary.keys())[4]):
                        code = dictionary[list(dictionary.keys())[4]]
                elif (char in list(dictionary.keys())[5]):
                        code = dictionary[list(dictionary.keys())[5]]
                else:
                        code = dictionary[list(dictionary.keys())[6]]
                if code != soundex[-1]:
                        soundex += code
        soundex = soundex.replace(".", "")
        soundex = soundex[:4].ljust(4, "0")
        return soundex

def binHash(word1):
        a=hashlib.md5(word1).hexdigest()[:4]
        a=int(a,16)
        return "{0:b}".format(a)

def intHash(word1):
        a=hashlib.md5(word1).hexdigest()[:4]
        a=int(a,16)
        return a

def SoundexSimilarity(w1,w2):
        s1 = SoundexCode(w1)
        s2 = SoundexCode(w2)
        N=abs(ord(s1[0])-ord(s2[0]))+np.log2(abs(int(s1[1:],16)-int(s2[1:],16))+1)
        D = 24+np.log2(int('ffffffff',16))
        return 1-N/D



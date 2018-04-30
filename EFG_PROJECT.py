import nltk
from nltk import word_tokenize
import sys
#read a file that contains greeklish 
#output a string on console that contains translated greeklish to Greek
exec(open('edit_distance.py').read())
exec(open('SoundexCode.py').read())

greeklish_file = open(sys.argv[1])
lex = open(sys.argv[2])

lexikon = word_tokenize(lex.read())

def FindPossibleWords(word):
    LexikonWords = []
    EditDistance = []
    Words = {}
    temp = ord(word[0])
    for w in lexikon:
        temp2 = ord(w[0])
        #print(temp2)
        if temp == temp2:
            LexikonWords.append(w)
        else:
            if (temp == 945 and temp2 == 940) or (temp == 949 and temp2 == 941) or (temp == 951 and temp2 == 942) or (temp == 953 and (temp2 == 943 or temp2 == 970)) or (temp == 965 and (temp2 == 971 or temp2 == 973)) or (temp == 959 and temp2 == 972) or (temp == 969 and temp2 == 974):
                LexikonWords.append(w)
    PossibleWrds = []
    for w in LexikonWords:
        ed = edit_distance(word,w) 
        if ed <=4:
            PossibleWrds.append(w)
            EditDistance.append(ed)
            try:
                Words.update({ed:Words[ed]+','+w})  
            except:
                Words[ed] = w
    #print(Words)
    return Words
tokens = []
greeklish_text = greeklish_file.read()[:-1]

print(greeklish_text)

greeklish_words = word_tokenize(greeklish_text)

print(greeklish_words)
lex.close()
greeklish_file.close()

NumOfWords = 0

Mapping = {"a":"α","b":"β","v":"β","g":"γ"
            ,"d":"δ","e":"ε","z":"ζ","h":"η"
            ,"8":"θ","i":"ι","k":"κ","l":"λ"
            ,"m":"μ","n":"ν","3":"ξ","o":"ο"
            ,"p":"π","r":"ρ","s":"σ","t":"τ"
            ,"u":"υ","f":"φ","x":"χ","4":"ψ"
            ,"w":"ω","j":"ξ","c":"σ"
            ,".":".",",":",","?":"?","!":"!"}

#Here we translate letter by letter the words
greek_text = []
PossibleWords = []
for word in greeklish_words:
    word = word.lower()
    greek_word = ""
    i = 0
    while i < len(word):
        if i == len(word)-1 and word[i] == 's':
            greek_word += 'ς'
            i+=1
        elif word[i] == 'c' and word[i+1] == 'h':
            greek_word += 'χ'
            i+=2
        elif word[i] == 'u':
            if word[i-1] == 'a' or word[i-1] == 'e':
                greek_word += Mapping[word[i]]
                i+=1
            elif word[i-1] != 'o':
                greek_word += 'ου'
                i+=1
            else:
                greek_word += Mapping[word[i]]
                i+=1
        else:
            greek_word += Mapping[word[i]]
            i+=1
    greek_text.append(greek_word)
    print(greek_word)
    PossibleWords.append(FindPossibleWords(greek_word))
    NumOfWords+=1

#This word works as a dictionary
#
finalPossibleWords = []
for i in range(0,NumOfWords):
    Ed0 = ''
    Ed1 = ''
    Ed2 = ''
    Ed3 = ''
    Ed4 = ''
    if greek_text[i] == ',' or greek_text[i] == '!' or greek_text[i] == '?' or greek_text[i] == '.':
        Ed0 = greek_text[i]
        Ed1 = 0
        Ed2 = 0
        Ed3 = 0
        Ed4 = 0
    else:
        try:
            Ed0 = PossibleWords[i][0]
        except:
            Ed0 = 0

        try:
            Ed1 = PossibleWords[i][1]
        except:
            Ed1 = 0
        
        try:
            Ed2 = PossibleWords[i][2]
        except:
            Ed2 = 0
        
        try:
            Ed3 = PossibleWords[i][3]
        except:
            Ed3 = 0
        
        try:
            Ed4 = PossibleWords[i][4]
        except:
            Ed4 = 0
    if Ed0 != 0:
        finalPossibleWords.append(Ed0)
    else:
        if Ed1 != 0:
            finalPossibleWords.append(Ed1)
        else:
            if Ed2 != 0:
                finalPossibleWords.append(Ed2)
            else:
                if Ed3 != 0:
                    finalPossibleWords.append(Ed3)
                else:
                    if Ed4 != 0:
                        finalPossibleWords.append(Ed4)
                    else:
                        finalPossibleWords.append(0)
fpw = []
fpwl = []
for i in range(0,NumOfWords):
    try:
        for r in word_tokenize(finalPossibleWords[i]):
            if r == 0:
                fpw.append(0)
            else:    
                fpw.append(r)
        fpwl.append(fpw)
        fpw = []
    except:
        fpw.append(0)
        fpwl.append(fpw)
text = ''

for i in range(0,NumOfWords):
    max = 0
    wrd = ''
    index = i
    try:
        for w in fpwl[i]:
            if w != 0 :
                temp = SoundexSimilarity(greek_text[i],w)
                if temp > max:
                    max = temp
                    wrd = w
    except:
        max = 0
        wrd = greeklish_words[index]
    text += ' ' + str(wrd)
print(text)
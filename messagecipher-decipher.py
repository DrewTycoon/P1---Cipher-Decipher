"""
Message Cipherer
"""
gate = input("Would you like to Cipher or Decipher?: ")
if gate == "Cipher":
        txt = input("Enter the message you would like to cipher: ")
        newNum = txt.maketrans({"1" : "3",
                        "2" : "4",
                        "3" : "5",
                        "4" : "6",
                        "5" : "7",
                        "6" : "8",
                        "7" : "9",
                        "8" : "0",
                        "9" : "1",
                        "0" : "2"
                        })
        newDic = txt.maketrans({"A" : "D", "a" : "d",
                        "B" : "E", "b" : "e",
                        "C" : "F", "c" : "f",
                        "D" : "G", "d" : "g",
                        "E" : "H", "e" : "h",
                        "F" : "I", "f" : "i",
                        "G" : "J", "g" : "j",
                        "H" : "K", "h" : "k",
                        "I" : "L", "i" : "l",
                        "J" : "M", "j" : "m",
                        "K" : "N", "k" : "n",
                        "L" : "O", "l" : "o",
                        "M" : "P", "m" : "p",
                        "N" : "Q", "n" : "q",
                        "O" : "R", "o" : "r",
                        "P" : "S", "p" : "s",
                        "Q" : "T", "q" : "t",
                        "R" : "U", "r" : "u",
                        "S" : "V", "s" : "v",
                        "T" : "W", "t" : "w",
                        "U" : "X", "u" : "x",
                        "V" : "Y", "v" : "y",
                        "W" : "Z", "w" : "z",
                        "X" : "A", "x" : "a",
                        "Y" : "B", "y" : "b",
                        "Z" : "C", "z" : "c"
                        })
        
        transTxt = txt.translate(newDic)
        transNum = transTxt.translate(newNum)
        transFin = transNum
        print(transFin)
elif gate == "Decipher":
        txt = input("Enter the message you would like to decipher: ")
        oldNum =txt.maketrans({'3': '1', '4': '2',
                               '5': '3', '6': '4',
                               '7': '5', '8': '6',
                               '9': '7', '0': '8',
                               '1': '9', '2': '0'})
        oldDic =txt.maketrans({'D': 'A', 'd': 'a',
                               'E': 'B', 'e': 'b',
                               'F': 'C', 'f': 'c',
                               'G': 'D', 'g': 'd',
                               'H': 'E', 'h': 'e',
                               'I': 'F', 'i': 'f',
                               'J': 'G', 'j': 'g',
                               'K': 'H', 'k': 'h',
                               'L': 'I', 'l': 'i',
                               'M': 'J', 'm': 'j',
                               'N': 'K', 'n': 'k',
                               'O': 'L', 'o': 'l',
                               'P': 'M', 'p': 'm',
                               'Q': 'N', 'q': 'n',
                               'R': 'O', 'r': 'o',
                               'S': 'P', 's': 'p',
                               'T': 'Q', 't': 'q',
                               'U': 'R', 'u': 'r',
                               'V': 'S', 'v': 's',
                               'W': 'T', 'w': 't',
                               'X': 'U', 'x': 'u',
                               'Y': 'V', 'y': 'v',
                               'Z': 'W', 'z': 'w',
                               'A': 'X', 'a': 'x',
                               'B': 'Y', 'b': 'y',
                               'C': 'Z', 'c': 'z'})
        

        transTxt = txt.translate(oldDic)
        transNum = transTxt.translate(oldNum)
        transFin = transNum
        print(transFin)
else:
    print(oldDic)
    print(newDic)

"""RESULTS
Would you like to Cipher or Decipher?: Cipher
Enter the message you would like to cipher: Hello mothafucka
Khoor prwkdixfnd
>>> 
================ RESTART: /home/amreynolds0396/messagescrambler.py ===============
Would you like to Cipher or Decipher?: Decipher
Enter the message you would like to decipher: Khoor prwkdixfnd
Hello mothafucka
"""
"""COMMENTS
Tried utilizing :
inv_map = {v: k for k, v in my_map.items()}
to duplicate dictionary and reverse the 'key' for the decipher.
Ended up calling the dictionary using stated code and
copying the printed dictionary into the code.
"""





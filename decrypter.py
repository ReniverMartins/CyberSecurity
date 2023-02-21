'''
    OS - Funcionalidades System
    PYAES - Funcionalidades de Encrypt e Decrypt
    
'''
import os
import pyaes

    ##abrir o arquivo a ser criptografado
fName = 'teste.txt.Encrypted'
file = open(fName, 'rb')
fileData = file.read()
file.close()

    ##Chave de Descriptografia
key = b"testeransonwares"
aes = pyaes.AESModeOfOperationCTR(key)
decryptData = aes.decrypt(fileData)

    ##RemoveArquivoCryptografado
os.remove(fName)

    ##SalvarArquivoCriptografado
nwFile = 'teste.txt'
nwFile = open(f'{nwFile}', 'wb')
nwFile.write(decryptData)
nwFile.close()
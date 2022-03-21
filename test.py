from random import randint

def GetRandChar(CHAR, NUM):
    char2ascii = ord(CHAR)
    sum = char2ascii + NUM
    n = sum // 255
    rand_ascii = sum - (n*255)  #for the value to rotate
    return chr(rand_ascii)

def get_seed():
    seed_array = list()
    for i in range(0, 15):
        seed_array.append(randint(0, 256))
    return seed_array

def encrypt(FILE, SEED):
    encryptedMsg = str()
    for char, num in zip(FILE, SEED):
        encryptedMsg += GetRandChar(char, num)
    return encryptedMsg

msg = 'dsfaaaaaaaaaaaaaaaaaaaaaaaaasdfasd afasdfadsf'
seed = get_seed()

print(encrypt(msg, seed))


from random import randint

def GetRandChar(CHAR, NUM):
    char2ascii = ord(CHAR)
    sum = char2ascii + NUM
    n = sum // 126
    rand_ascii = sum - (n*126)              #for the value to rotate
    return chr(rand_ascii)

def get_seed():
    seed_array = list()
    for i in range(0, 31):                  #5bit integer limit. Don't want the seed to be big
        seed_array.append(randint(10, 99))
    return seed_array

def encrypt(FILE, SEED):
    encryptedMsg = str()
    n = (len(FILE) // len(SEED)) + 1        #Wen u zip it, SEED wil alwez B bigger
    seedCopy = SEED.copy()
    for i in range(0, n+1):
        SEED.extend(seedCopy)
    for char, num in zip(FILE, SEED):
        encryptedMsg += GetRandChar(char, num)
    return encryptedMsg

def show_seed(SEED):
    STR = str()
    for i in SEED:
        STR += str(i)
    return STR

def decrypt(FILE, SEED):
    decryptedMsg = str()
    


msg = 'Daiyaan Muhammad Fardeen And Fardeen Kamal er sommilito project 1'
seed = get_seed()

encFile = open("secret.txt", "w")
encFile.write(encrypt(msg, seed))
encFile.close()

seedFile = open("seed.txt", 'w')
seedFile.write(show_seed(seed))
seedFile.close()

encFile = open("secret.txt", 'r')
seedFile = open("seed.txt", 'r')

print(encFile.read(), seedFile.read())
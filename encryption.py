from random import randint

def GetRandChar(CHAR, NUM):
    char2ascii = ord(CHAR)      #getting the ASCII value
    sum = char2ascii + NUM      #adding the random number
    n = sum // 126              #if sum is greater than 126 (largest ASCII value), n > 1. Otherwise, n == 0
    rand_ascii = sum - (n*126)  # the random ASCII value we get can be greater than 126. [-(n*126)] part is going to solve that. If n == 0, nothing will get substracted. If n == 1, then sum is also greater than 1. Tahole sum theke n*126 othoba 1*126 minus hobe
    return chr(rand_ascii)      #Return the character from the ASCII value

def get_seed():
    seed_array = list()     #A list to store the seed
    for i in range(0, 16):  # 2^4 or 4 bit integer. Why? Because it sounds cool. It can be anything.
        seed_array.append(randint(10, 99)) #Dui digit er number nitasi. Jate decrypt korar somoy seed theke value extract kora easy hoy.
    return seed_array

def encrypt(FILE, SEED):
    encryptedMsg = str()
    n = (len(FILE) // len(SEED)) + 1        #Wen u zip it, SEED wil alwez B bigger. Bcuz if SEED is smaller, massage will bottleneck
    seedCopy = SEED.copy()                  #Copy kortasi karon list ta extend korle Double add hoye jabe tokhon
    for i in range(0, n+1):
        SEED.extend(seedCopy)               #Extending the seed to reach the value of the msg. Otherwise, only a partial of the msg will get encrypted
    for char, num in zip(FILE, SEED):
        encryptedMsg += GetRandChar(char, num) #STRING CONCATANATION!!! Eita ke emneo porte paros [encryptedMsg = encryptedMsg + GetRandChar(char, num)]
    return encryptedMsg

def show_seed(SEED):  #This is a way to format the seed to a string. Jate sob jaygay sohoje fit kora jay.
    STR = str()
    for i in SEED:
        STR += str(i)
    return STR

def decrypt(FILE, SEED):
    decryptedMsg = str()
    

##########################################
#  The whole thing below is for testing  #
##########################################


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
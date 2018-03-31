#List
def applyToEach(L, f):
    """Assumes L is a list, f a function
Mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])
L = [1, -2, 3.33]
print ('L =', L )
print ('Apply abs to each element of L.' )
applyToEach(L, abs)
print ('L =', L)
print ('Apply int to each element of', L )
applyToEach(L, int)
print ('L =', L)
print ('Apply factorial to each element of', L )



#Tuple
def findDivisors (n1, n2):
    """Assumes that n1 and n2 are positive ints
    Returns a tuple containing all common divisors of n1 & n2"""
    divisors = () #the empty tuple
    for i in range(1, min (n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,)
    return divisors
divisors = findDivisors(20, 100)
print (divisors)
total = 0
for d in divisors:
    total += d
print (total)


#Dictionary

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je', 'eat':'mange', 'drink':'bois', 'John':'Jean', 'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I', 'mange':'eat', 'bois':'drink', 'Jean':'John', 'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}
def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word
def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation + translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)
print (translate('I drink good red wine, and eat bread.', dicts,'English to French'))
print (translate('Je bois du vin rouge.', dicts, 'French to English'))

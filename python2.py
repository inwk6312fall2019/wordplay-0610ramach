*****9.1 Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).


def search_words():
	file=open("words.txt")
	for word in item:
		word=word.strip()
		if len(word)>=20
			print(word)
search_words()


*****9.2 Write a program that reads words.txt and prints only the words that have no “e”. Compute the percentage of words in the list that have no “e”.


y=open('file.txt', 'r')
item_list = y.read().split()
def no_e(word):
    return word.find('e') == -1
total = len(item_list)
no_e = [word for word in item_list if no_e(word)]
percentage = float(len(no_e)) / total
print'{:.2%}'.format(percentage)


*****9.3 Write a function named avoids that takes a word and a string of forbidden letters,and that returns True if the word doesn’t use any of the forbidden letters.

def items_entered(word,forbidden_string):
    for char in word:
        if char.lower() in forbidden_string.lower():
            return False
    return True
def avoid(string, forbidden_string):
    words = string.split()
    correct_words = []
    for word in words:
        if items_entered(word, forbidden_string):
            right_words.append(word)
    print('\n'," ".join(right_words))
avoid()


*****9.4 Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?

goal = 'acefhlo'
y=open('words.txt', 'r')
word_list = y.read().splitlines()
def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True
words = [word for word in word_list if uses_only(word, goal)]
print(There are {} words that use only '{}', here's a sample: {}".format(len(words), target, words[:10]))

*****9.5 Write a function named uses_all that takes a word and a string of required letters,and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?

x=open('file.txt', 'r')
my_list = x.read().split()
def user_all(word, string):
    count = 0
    for letter in string:
        if letter in word:
            count += 1
    if count == len(string):
        return True
    return False
def find_all_vowels(list):
    count = 0
    string = 'aeiou'
    for word in list:
        if user_all(word, string):
            count += 1
    return count

print(find_all_vowels(word_list))

*****9.6 Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?

my_file= open('words.txt')
for line in my_file: 
    sentence=my_file.readline()
word=sentence.strip()
a=0
index=0
for letter in word:
    if ord(letter)<ord(word[index+1]):
        a=a+1
        index=index+1
if a==len(word):
    print(word)

*****9.7  This question is based on a Puzzler that was broadcast on the radio program Car
Talk (http: // www. cartalk. com/ content/ puzzlers ):
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?

def do_some(word):
    for i in range(len(word) - 5):
            if word[i] == word[i + 1]:
                if word[i + 2] == word[i + 3]:
                    if word[i + 4] == word[i + 5]:
                        return True
    return False
y = open("item.txt")
def find_do_some():
    for line in wordlist:
        word = line.strip()
        if do_some(word):
            print(word)
find_do_some()

*****9.8  Here’s another Car Talk Puzzler (http: // www. cartalk. com/ content/puzzlers ):

def palindrome(num):
    return str(num) == str(num)[::-1]
def puzzler_8():
    for num in range(100000, 1000000):
        if palindrome(str(num)[2:6]):
            if palindrome(str(num + 1)[1:6]):
                if palindrome(str(num + 2)[1:5]):
                    if palindrome(str(num +3)):
                        print(num)
    return False
puzzler_8()

*****9.9 Here’s another Car Talk Puzzler you can solve with a search (http: // www.cartalk. com/ content/ puzzlers ):
def palidrome_age(motherAge, daughterAge):
    Age_mother = str(motherAge)
    Age_daughter = str(daughterAge)
    diff= len(Age_mother) - len(Age_daughter)
    Age_daughter = Age_daughter.zfill(len(motherAge))
    age_mother = age_mother[::-1]
    if Age_mother == Age_daughter:
        return True
    else:
        return False
count = 0
previousDiffAge = 0
for Age_mother in range (15, 120):
    for Age_daughtert in range(1, 100):
        diffAge = Age_mother - Age_daughter
        if palidrome(Age_mother, Age_daughter) and diffAge == previousDiffAge:
            count = count + 1
            if count == 6:
                print(Age_mother)
                print(Age_daughter)
    previousDiffAge = diffAge



******13.1

book='file.txt'
x=open(book, 'r') 
    items = x.read().split()
def empty(word):
    empties = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print("{} has {} 'words'".format(book, len([clean(word) for word in words])))




******13.3

def my_list(file):
    file = open(file)
    x = open('items.txt')
    dictionary = [line.rstrip('\r\n') for line in allWords] 
    for line in file.readlines():
        line = line.strip()
        words = line.split()
        for word in items:
            word = word[0:word.find(",")]
            found = False
            index = 0
            for element in dictionary:
                if found:
                    break
                if word == element:
                    found = True
                    break
                elif word != element and index < len(dictionary)-1:
                    index = index + 1
                else:
                    print("The word " + word + " is not in the dictionary"break)

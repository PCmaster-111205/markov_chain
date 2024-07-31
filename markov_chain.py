import random
SEED = 8 #this seed is mainly for testing
random.seed(SEED)
def create(file):
    '''
    Purpose: This function takes a text file, and return 
    a list with only the word appear in the text file without
    the '\n' character or spaces.
    Parameter: file is a string representing the name of the file
    Return: a list containing all the word in the text file.'''
    file = open(file).read().split('\n')
    result = []
    for i in file:
        for k in i.split():
            result.append(k)
    return result

def create_dict(database, prefix):
    '''
    Purpose: this list take in a list containing words from a text
    and a prefix size, return an dictionary where the key is a tuple
    containing an n amount of word in the list (n is prefix size), and
    the value is the list containing the word that came right after n 
    consecutive word in the list
    Paramter: database is a list
    prefix is an integer
    Return: a dictionary'''
    dict = {}
    for i in range(len(database) - prefix ):
        if not tuple(database[i: i + prefix]) in dict.keys():
            # creating the key with the given prefix size
            dict[tuple(database[i:i + prefix])] = []
        # adding the suffix into the list for each prefix
        dict[tuple(database[i:i + prefix])].append(database[prefix + i])
    return dict

def paragraph(word_length, tlist):
    '''
    Purpose: this function takes in a list containing words, and 
    an integer stop. The function return a paragraph containing n number
    of word in the list with every line in the paragraph contains a
    maximum amount of 10 words. 
    Parameter: stop is an integer, tlist is a list
    Return: a string'''
    counter = 1
    string = ''
    # adding until reached the desired length
    while counter <= word_length:
        string += tlist[counter - 1] + ' '
        counter += 1
        # new line every 10 word
        if (counter - 1) % 10 == 0:
            string += '\n'
    print(string.strip())

def main():
    '''
    Purpose: This file execute the main purpose that was described at the top
    of this file.
    Parameter: None
    Return: None'''
    file = input()
    prefix = int(input())
    word_length = int(input())
    database = create(file)
    dict = create_dict(database, prefix)
    tlist = []
    if tlist == []:
        # set the first n word in the generated text
        tlist += list(list(dict.keys())[0])
    while len(tlist) <= word_length:
        # take the two last elemetnt w2 w3 in the current list
        # tuple(w2, w3) is the prefix
        # use the dictionary to get the suffix
        key = tuple(tlist[-(prefix):])
        # handling the case where there are more than 1 suffix
        # which is choose a random suffix from a list
        if len(dict[key]) > 1:
            index = random.randint(0, len(dict[key]) - 1)
            tlist += [dict[key][index]]
        else:
            tlist += dict[key]
    paragraph(word_length, tlist)    

main()

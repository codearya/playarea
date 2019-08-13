'''1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay."

Example: Happy = appyh + ay = appyhay


2. If a word starts with two consonants move the two consonants to the end of the word and add "ay."

Example: Child = Ildch + ay = Ildchay


3. If a word starts with a vowel add the word "way" at the end of the word.

Example: Awesome = Awesome +way = Awesomeway

'''

def conv_platin(myword):
    myword_list =list(myword)
    print("list version of input word is {}".format(myword_list))
    if myword_list[0] not in ['a','e','i','o','u'] and myword_list[1] in ['a','e','i','o','u']:
        pver = ''.join(myword_list[1:])+myword_list[0]+'ay'
        print('pig latin version of current word is: {}'.format(pver))
    elif myword_list[0] in ['a','e','i','o','u']:
        pver = ''.join(myword)+"way"
        print(pver)
    elif myword_list[0] not in ['a','e','i','o','u'] and myword_list[1] not in ['a','e','i','o','u']:
        pver = ''.join(myword_list[2:])+myword_list[0]+myword_list[1]+'ay'
    else:
        print('The end is near')


conv_platin('happy')

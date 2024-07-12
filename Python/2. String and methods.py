'''Strings: introduction, string operations (concatenation, repetition, membership and ), 
traversing a string using loops, built-in functions/methods–len(), capitalize(), title(), lower(), 
upper(), count(), find(), index(), endswith(), startswith(), isalnum(), isalpha(), isdigit(), 
islower(), isupper(), isspace(),lstrip(), rstrip(), strip(), replace(), join(), partition(), split()'''


first_name = "Raj Rishi"
last_name = "Rana"


print("|||| STRING OPERATIONS||||")
print("==============================================")

# concatenation
print(first_name+last_name)

# repetition
print(first_name*5)

# membership
print("a" in first_name)

# slicing
print(last_name[2:4])
print(last_name[1:-1]) 
print("==============================================")

print("TRAVERSING A STRING USING LOOPS")
for char in first_name:
    print(char)

index = 0
while index < len(first_name):
    print(first_name[index] + " is at index " + str(index))
    index+= 1
print("==============================================")


print('|||| STRING METHODS||||')

print('len        : ', len(first_name))
print('capitalize : ', first_name.capitalize())
print('title      : ', first_name.title())
print('lower      : ', first_name.lower())
print('upper      : ', first_name.upper())
print('count(i)   : ', first_name.count('i'))
print('find(Rishi): ', first_name.find('Rishi'))
print('index(i)   : ', first_name.index('i'))
print('endswith(d): ', first_name.endswith('d'))
print('startswith(R): ', first_name.startswith('R'))
print('isalnum    : ', first_name.isalnum())   # have only alphabets and numbers, not even white spaces
print('isalpha    : ', first_name.isalpha())   # only aphabet
print('isdigit    : ', first_name.isdigit())   # only digits
print('isupper    : ', first_name.isupper())
print('islower    : ', first_name.islower())
print('isspace    : ', first_name.isspace())   # only whtiespace?
print('lstrip     : ', first_name.lstrip())    # remove whitespace of left side and will remove specific alphabets if entered as argument
print('rstrip     : ', first_name.rstrip('i'))    # of right side and will remove specific alphabets if entered as argument
print('strip      : ', first_name.strip('i'))     # remove space from l as well as right and will remove specific alphabets if entered as argument, dont remove from middle of string
print("'   raj rishiii   '.strip(i) :", "   raj rishiiii    ".strip('i'))        # won't remove from middle
print('replace(R,n): ', first_name.replace('R','n'))
print("'Raj Rishi'.join(Hello)  :", 'Raj Rishi'.join('Hello'))      # given argument will iterate and the main sting will be repeated after it
print('partition(a): ', first_name.partition('a'))    # split at the argument given and store in tuple
print('split      : ', first_name.split())      # split and words and store in list
print("'Raj Rishi Rana'.split('i') : ", 'Raj Rishi Rana'.split('i'))      # splits at the given arg

print("==============================================")

print('\n\n\n\n\n')



#_______________________________________________________________________________


print('CLASS 12th')
print('\n\n')



from string import *
# this module conatains some important variable, such as :
print(ascii_letters)
print(ascii_lowercase)
print(ascii_uppercase)
print(digits)
print(hexdigits)
print(octdigits)
print(punctuation)

myname = '   raj      rishi     rana'
print(capwords(myname))
print(capwords.__doc__)


"Creat a function my_capwords which will do the same job as the capwords function"
def my_capwords(sentence, seperator=' '):
    #step 1: spliting
    thelist = sentence.split(seperator)

    #step 2: capitalizing
    for i in range(len(thelist)):
        thelist[i] = thelist[i].capitalize()

    #step 3: join
    final = seperator.join(thelist)


    return final

print(my_capwords('heLLow, my   nAme is  raj'))




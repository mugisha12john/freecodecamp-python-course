# yes yes yes please", return "yes(3) please"
def compress_string(sentence):

    li =  sentence.split()
    return li.count('yes')

print(compress_string("yes yes yes please"))
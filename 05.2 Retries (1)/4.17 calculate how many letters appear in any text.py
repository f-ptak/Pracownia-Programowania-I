def calc_letters():
    sentence = input("Enter a sentence: ")
    letter = input("Enter a letter: ")
    sentence_list = list(sentence)
    amount = sentence_list.count(letter)
    return amount


print(calc_letters())
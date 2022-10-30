def get_count_char (input_str):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    dictionary = {}
    text = input_str.lower()
    text = list(text)
    count = 0
    for symbol in text:
        if symbol.isalpha():
            dictionary[symbol] = dictionary.get(symbol, count) + 1
    return dictionary

def share_of_text (input_str):
    dictionary = {}
    text = input_str.lower()
    text = list(text)
    count = 0
    for symbol in text:
        if symbol.isalpha():
            dictionary[symbol] = dictionary.get(symbol, count) + 1 / 257 * 100
    return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(share_of_text(main_str))

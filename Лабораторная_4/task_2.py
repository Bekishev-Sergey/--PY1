def get_count_char(text, index=0):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_ = {}
    text = text.lower()
    text = list(text)
    copy_text = text.copy()
    count = 0
    for i in text:
        for j in copy_text:
            if i == j and i.isalpha():
                count += 1
        if count > 0:
            dict_[i] = count
        count = 0
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

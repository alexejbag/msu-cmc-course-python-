import re

line = input()
while line:
    new_str = ''
    copy = line + ' '
    for split in re.split(r'[^a-zA-Z\']', line):
        print(split)
        if re.search(r'[^a-zA-Z\'].*', copy):
            copy = re.search(r'[^a-zA-Z\'].*', copy).group()
        else:
            copy = ''
        word = re.search(r'([a-zA-Z\'].*[a-zA-Z\']*)', split)
        if word is None:
            word = ''
        else:
           flag = False
           word = word.group()
           if word[0].isupper():
               word = word.lower()
               flag = True
           first_s = re.search(r'^[^aouie]+', word)
           first_g = re.search(r'^[aouie][^aouie]*', word)
           if first_s:
               remain_word = re.search(r'([aouie].*)', word)
               if remain_word:
                   word = remain_word.group() + first_s.group() + 'ay'
               else:
                   word = first_s.group()
           elif first_g:
                another_part = re.search(r'[aouie].*', word[1:])
                if another_part:
                   word = another_part.group() + first_g.group() + 'ay'
                else:
                   word = first_g.group() + 'yay'
           if flag:
                word = word[0].upper() + word[1:]
        new_str += word
        if copy:
            new_str += copy[0]
            copy = copy[1:]
    print(new_str)
    line = input()

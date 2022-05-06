text = raw_input("Type the text you want to L337 : ")

# 4 8 C D 3 F 6 H 1 J K 1 M N 0 P Q r 5 7 U V W V X Y Z
# A B C D E F G H I J K L M N O P Q R S T U V W V X Y Z

char_to_replace = {'a' : '4',
                   'A' : '4',
                   'b' : '8',
                   'B' : '8',
                   'e' : '3',
                   'E' : '3',
                   'g' : '6',
                   'G' : '6',
                   'i' : '1',
                   'I' : '1',
                   'o' : '0',
                   'O' : '0',
                   's' : '5',
                   'S' : '5',
                   't' : '7',
                   'T' : '7'}

for key, value in char_to_replace.items():
    text = text.replace(key,value)
print(text)
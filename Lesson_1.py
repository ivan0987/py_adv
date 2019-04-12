from chardet.universaldetector import UniversalDetector


'''1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.'''


a = 'разработка'
b = 'сокет'
c = 'декоратор'
print(type(a), type(b), type(c))  # тип
print(a, b, c)  # содержание
# Переводим в Unicode
print(a.encode('Utf-8'), type(a.encode('Utf-8')))
print(b.encode('Utf-8'), type(b.encode('Utf-8')))
print(c.encode('Utf-8'), type(c.encode('Utf-8')))


''' 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность 
кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.'''

a = b'class'
b = b'function'
c = b'method'
print(type(a), a, len(a))  # <class 'bytes'> b'class' 5
print(type(b), b, len(b))  # <class 'bytes'> b'function' 8
print(type(c), c, len(c))  # <class 'bytes'> b'method' 6

'''3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.'''

# Невозможно предстаить в байтовом типе только 'класс', по причине: 'bytes can only contain ASCII literal characters'


'''4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления 
в байтовое и выполнить обратное преобразование (используя методы encode и decode).'''

a = 'разработка'
b = 'администрирование'
c = 'protocol'
d = 'standard'

a = a.encode('utf-8')
b = b.encode('utf-8')
c = c.encode('utf-8')
d = d.encode('utf-8')
print(a, b, c, d)

a = a.decode()
b = b.decode()
c = c.decode()
d = d.decode()
print(a, b, c, d)

'''5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового 
в строковый тип на кириллице.'''
detector = UniversalDetector()
with open('1.txt', 'rb') as f:
    for line in f:
        a = line.decode('IBM866', 'ignore')
        print(a)

with open('2.txt', 'rb') as f:
    for line in f:
        a = line.decode('IBM866', 'ignore')
        print(a)


# Долго ж я искал эту кодировку!!!


'''6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.'''

detector = UniversalDetector()
with open('test_file.txt', 'rb') as f:
    for line in f:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
print(detector.result)
# Файл закодирован как :{'encoding': 'windows-1251', 'confidence': 0.8607358176937344, 'language': 'Bulgarian'}

import codecs

cyril = ["И", "и", "ю", "Ю", "я", "Я", "ё", "Ё", "ш", "Ш", "ч", "Ч", "ў", "Ў",
         "қ", "Қ", "ғ", "Ғ", "ц", "Ц", "й", "Й", "у", "У", "к", "К",
         "е", "Е", "н", "Н", "г", "Г", "щ", "Щ", "з", "З", "х", "Х",
         "э", "Э", "ж", "Ж", "д", "Д", "л", "Л", "о", "О", "р", "Р",
         "п", "П", "а", "А", "в", "В", "ф", "Ф", "с", "С", "м", "М",
         "ы", "Ы", "т", "Т", "б", "Б", "қ", "Қ", "ҳ", "Ҳ", "ғ", "Ғ", "ь"]
latin = ["I", "i", "yu", "Yu", "ya", "Ya", "yo", "Yo", "sh", "Sh", "ch", "Ch", "o'", "O'",
         "q", "Q", "g'", "G'", "ts", "Ts", "y", "Y", "u", "U", "k", "K", "e", "E",
         "n", "N", "g", "G", "sh", "Sh", "z", "Z", "x", "X", "e", "E", "j", "J",
         "d", "D", "l", "L", "o", "O", "r", "R", "p", "P", "a", "A", "v", "V", "f",
         "F", "s", "S", "m", "M", "i", "I", "t", "T", "b", "B", "q", "Q", "h", "H",
         "g'", "G'", "`"]


def con_to_latin(s: str) -> str:
    for i in range(len(cyril)):
        s = s.replace(cyril[i], latin[i])
    return s


def con_to_cyril(s: str) -> str:
    for i in range(len(cyril)):
        s = s.replace(latin[i], cyril[i])
    return s


async def to_cyril(path):
    f = codecs.open(path, 'r', 'utf-8')
    f.seek(0)
    s = f.read()
    f.close()
    f = codecs.open(path, 'w', 'utf-8')
    s = con_to_cyril(s)
    f.write(s)
    f.close()


async def to_latin(path):
    f = codecs.open(path, 'r', 'utf-8')
    f.seek(0)
    s = f.read()
    f.close()
    f = codecs.open(path, 'w', 'utf-8')
    s = con_to_latin(s)
    f.write(s)
    f.close()

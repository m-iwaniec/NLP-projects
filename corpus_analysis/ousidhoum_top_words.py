import collections

file = open('/home/martyna/corpus_analysis/ousidhoum_dataset.csv', encoding="utf8")
a = file.read()

stopwords = set(line.strip() for line in open('/home/martyna/corpus_analysis/word_freq/stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
# Instantiate a dictionary, and for every word in the file,
# add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}

# To eliminate duplicates, split by punctuation, and use case demiliters.
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("[","")
    word = word.replace("<","")
    word = word.replace(">","")
    word = word.replace("-", "")
    word = word.replace("&","")
    word = word.replace("*","")
    word = word.replace("0", "")
    word = word.replace("1", "")
    word = word.replace("2", "")
    word = word.replace("3", "")
    word = word.replace("4", "")
    word = word.replace("5", "")
    word = word.replace("6", "")
    word = word.replace("7", "")
    word = word.replace("8", "")
    word = word.replace("9", "")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            # Print most common word

n_print = int(input("How many most common words do you want to print: "))
print("\nOK. The {} most common words are:\n".format(n_print))

word_counter = collections.Counter(wordcount)
x = 0
for word, count in word_counter.most_common(n_print):
    print(str(x), ": ", word, ": ", count)
    x += 1

file.close()

# Top 100:
# 0 :  @user :  4381
# 1 :   :  471
# 2 :  retarded :  460
# 3 :  shithole :  453
# 4 :  retard :  405
# 5 :  faggot :  362
# 6 :  ching :  362
# 7 :  cunt :  355
# 8 :  fucking :  322
# 9 :  twat :  317
# 10 :  chong :  302
# 11 :  i'm :  253
# 12 :  country :  245
# 13 :  people :  240
# 14 :  spic :  221
# 15 :  countries :  196
# 16 :  nigger :  188
# 17 :  fuck :  173
# 18 :  called :  157
# 19 :  mongoloid :  150
# 20 :  illegal :  140
# 21 :  immigrants :  125
# 22 :  ass :  120
# 23 :  im :  115
# 24 :  shit :  111
# 25 :  negro :  106
# 26 :  dyke :  106
# 27 :  white :  105
# 28 :  call :  101
# 29 :  he's :  94
# 30 :  amp; :  92
# 31 :  look :  89
# 32 :  aliens :  88
# 33 :  mongy :  88
# 34 :  time :  88
# 35 :  can't :  87
# 36 :  trump :  86
# 37 :  refugees :  78
# 38 :  okay :  75
# 39 :  leftist :  74
# 40 :  mongol :  73
# 41 :  dont :  73
# 42 :  feminazi :  71
# 43 :  bitch :  70
# 44 :  love :  69
# 45 :  stop :  69
# 46 :  hate :  66
# 47 :  stupid :  65
# 48 :  little :  63
# 49 :  that's :  63
# 50 :  lol :  63
# 51 :  word :  60
# 52 :  shut :  60
# 53 :  saying :  58
# 54 :  dumb :  55
# 55 :  calling :  55
# 56 :  world :  54
# 57 :  i've :  54
# 58 :  guy :  53
# 59 :  yeah :  53
# 60 :  oh :  53
# 61 :  gonna :  51
# 62 :  ur :  50
# 63 :  chinaman :  50
# 64 :  getting :  50
# 65 :  tell :  49
# 66 :  racist :  48
# 67 :  raghead :  48
# 68 :  america :  46
# 69 :  mean :  46
# 70 :  gay :  44
# 71 :  wanna :  43
# 72 :  ya :  43
# 73 :  actually :  43
# 74 :  ok :  42
# 75 :  terrorist :  42
# 76 :  day :  42
# 77 :  @url :  41
# 78 :  left :  41
# 79 :  yes :  41
# 80 :  tweet :  41
# 81 :  literally :  40
# 82 :  bad :  40
# 83 :  live :  39
# 84 :  nigga :  39
# 85 :  cant :  39
# 86 :  hey :  39
# 87 :  mind :  37
# 88 :  trying :  37
# 89 :  i'll :  37
# 90 :  black :  37
# 91 :  god :  36
# 92 :  feel :  35
# 93 :  maybe :  35
# 94 :  absolute :  35
# 95 :  talking :  35
# 96 :  fat :  35
# 97 :  twitter :  35
# 98 :  looks :  35
# 99 :  fuckin :  35
# 100 :  told :  35
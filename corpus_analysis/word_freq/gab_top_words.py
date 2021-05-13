import collections

file = open('/home/martyna/masters-thesis/data/gab.csv', encoding="utf8")
a = file.read()

stopwords = set(line.strip() for line in open('/home/martyna/masters-thesis/data/stopwords.txt'))
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
# 1 :  people :  6422
# 2 :  nigger :  4510
# 3 :  language :  4064
# 4 :  using :  3934
# 5 :  don't :  3802
# 6 :  please :  3449
# 7 :  offensive :  3372
# 8 :  faggot :  3186
# 9 :  word :  3119
# 10 :  white :  2914
# 11 :  it's :  2628
# 12 :  hate :  2566
# 13 :  race :  2542
# 14 :  doesn't :  2521
# 15 :  unacceptable :  2475
# 16 :  words :  2458
# 17 :  speech :  2423
# 18 :  refrain :  2383
# 19 :  cunt :  2286
# 20 :  retarded :  2254
# 21 :  demeans :  2096
# 22 :  insults :  2080
# 23 :  derogatory :  1930
# 24 :  discourse :  1919
# 25 :  slurs :  1768
# 26 :  racist :  1709
# 27 :  i'm :  1607
# 28 :  you're :  1598
# 29 :  post :  1580
# 30 :  jews :  1561
# 31 :  hateful :  1517
# 32 :  comments :  1516
# 33 :  mean :  1497
# 34 :  'use :  1476
# 35 :  shit :  1453
# 36 :  fuck :  1437
# 37 :  fucking :  1425
# 38 :  hurtful :  1369
# 39 :  trump :  1365
# 40 :  women :  1355
# 41 :  time :  1347
# 42 :  based :  1337
# 43 :  'please :  1316
# 44 :  terms :  1306
# 45 :  calling :  1305
# 46 :  mental :  1271
# 47 :  sexual :  1265
# 48 :  person :  1252
# 49 :  jew :  1248
# 50 :  retard :  1190
# 51 :  term :  1141
# 52 :  gab :  1111
# 53 :  name :  1110
# 54 :  'the :  1097
# 55 :  lol :  1093
# 56 :  look :  1089
# 57 :  black :  1082
# 58 :  community :  1055
# 59 :  that's :  1047
# 60 :  can't :  1047
# 61 :  isn't :  1033
# 62 :  thank :  1028
# 63 :  try :  1017
# 64 :  stupid :  987
# 65 :  stop :  955
# 66 :  own :  951
# 67 :  call :  950
# 68 :  am :  950
# 69 :  attack :  919
# 70 :  racial :  902
# 71 :  little :  864
# 72 :  actually :  843
# 73 :  makes :  841
# 74 :  'your :  840
# 75 :  real :  837
# 76 :  orientation :  832
# 77 :  ]'use :  829
# 78 :  help :  824
# 79 :  understand :  821
# 80 :  believe :  820
# 81 :  woman :  815
# 82 :  slur :  801
# 83 :  'i :  794
# 84 :  insult :  775
# 85 :  world :  769
# 86 :  ]'please :  753
# 87 :  religion :  747
# 88 :  sex :  745
# 89 :  violation :  743
# 90 :  left :  741
# 91 :  bad :  731
# 92 :  trying :  730
# 93 :  homophobic :  729
# 94 :  jewish :  717
# 95 :  denigrates :  715
# 96 :  gender :  708
# 97 :  guidelines :  699
# 98 :  yourself :  696
# 99 :  'you :  695
# 100 :  disability :  686
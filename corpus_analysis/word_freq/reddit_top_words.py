import collections

file = open('/home/martyna/masters-thesis/data/reddit.csv', encoding="utf8")
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
# 1 :  people :  6137
# 2 :  it's :  4457
# 3 :  don't :  3905
# 4 :  women :  2807
# 5 :  using :  2235
# 6 :  i'm :  2230
# 7 :  you're :  2058
# 8 :  fucking :  1951
# 9 :  shit :  1815
# 10 :  time :  1676
# 11 :  word :  1664
# 12 :  that's :  1651
# 13 :  language :  1598
# 14 :  retarded :  1530
# 15 :  cunt :  1496
# 16 :  please :  1484
# 17 :  offensive :  1463
# 18 :  fuck :  1458
# 19 :  doesn't :  1447
# 20 :  refrain :  1325
# 21 :  actually :  1262
# 22 :  woman :  1236
# 23 :  n/an/a :  1173
# 24 :  can't :  1151
# 25 :  person :  1148
# 26 :  words :  1117
# 27 :  white :  1104
# 28 :  isn't :  1102
# 29 :  mean :  1093
# 30 :  gender :  1032
# 31 :  didn't :  1011
# 32 :  hate :  1010
# 33 :  saying :  961
# 34 :  bad :  942
# 35 :  they're :  917
# 36 :  trying :  893
# 37 :  own :  891
# 38 :  stupid :  865
# 39 :  wrong :  850
# 40 :  post :  849
# 41 :  am :  840
# 42 :  term :  837
# 43 :  guy :  837
# 44 :  comments :  806
# 45 :  look :  797
# 46 :  speech :  793
# 47 :  based :  787
# 48 :  life :  785
# 49 :  lot :  773
# 50 :  makes :  773
# 51 :  reason :  770
# 52 :  call :  754
# 53 :  world :  753
# 54 :  pretty :  749
# 55 :  getting :  740
# 56 :  try :  735
# 57 :  game :  722
# 58 :  yeah :  715
# 59 :  calling :  711
# 60 :  understand :  704
# 61 :  real :  703
# 62 :  probably :  699
# 63 :  feel :  691
# 64 :  doing :  683
# 65 :  sex :  674
# 66 :  there's :  671
# 67 :  black :  670
# 68 :  argument :  670
# 69 :  mental :  660
# 70 :  believe :  658
# 71 :  hateful :  656
# 72 :  left :  652
# 73 :  agree :  651
# 74 :  little :  628
# 75 :  derogatory :  622
# 76 :  it’s :  619
# 77 :  sub :  615
# 78 :  racist :  614
# 79 :  maybe :  614
# 80 :  stop :  608
# 81 :  don’t :  603
# 82 :  instead :  601
# 83 :  retard :  600
# 84 :  he's :  599
# 85 :  comment :  598
# 86 :  i've :  595
# 87 :  sexual :  593
# 88 :  literally :  589
# 89 :  rape :  589
# 90 :  disability :  588
# 91 :  % :  579
# 92 :  talking :  574
# 93 :  day :  573
# 94 :  'please :  561
# 95 :  lol :  560
# 96 :  hard :  557
# 97 :  yes :  555
# 98 :  female :  554
# 99 :  tell :  552
# 100 :  oh :  534
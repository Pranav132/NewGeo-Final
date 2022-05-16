f = open('botstuff.txt', 'r')

f2 = open('formatted.txt', 'a')


for line in f.readlines():
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    vals = line.split(' ')
    word = vals[0][:vals[0].index(',')]
    f2.write(word)
    f2.write(',')
    if word == 'NEGATIVE':
        f2.write('-')
    f2.write(vals[1])
    f2.write('\n')

def complement(sequence):
    new = ''
    for letter in sequence:
        if letter == 'G': new += 'C'
        elif letter == 'C': new += 'G'
        elif letter == 'A': new += 'T'
        else: new += 'A'
    return new

while True:
    sequence = input('Primer sequence: ')
    comp = complement(sequence)
    l = len(sequence)
    gc = 100 * (sequence.count('G') + sequence.count('C')) / l
    txt = '\tSequence: l = %d, gc = %.1f' % (l, gc)
    print(txt)
    txt = '\tInverse: %s' % sequence[::-1]
    print(txt)
    txt = '\tComplement: %s' % comp
    print(txt)
    txt = '\tI-Complement: %s' % comp[::-1]
    print(txt)
    print()


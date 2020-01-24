import pickle

# Objects themselves must be read back in the same order that they're written in
rageAgainstMachine = ('Rage Against The Machine',
                      'Evil Empire',
                      1996,
                      ( 1, 'People of the Sun',
                        2, 'Bulls on Parade',
                        3, 'Vietnow',
                        4, 'Revolver'))

even = range(0, 20, 2)
odd = range(1, 21, 2)

with open('pickleFile', 'wb') as ragePickle:
    pickle.dump(rageAgainstMachine, ragePickle)
    pickle.dump(even, ragePickle)
    pickle.dump(odd, ragePickle)
    pickle.dump(2998033, ragePickle)

with open('pickleFile', 'rb') as limpPickle:
    rage2 = pickle.load(limpPickle)
    rageeven = pickle.load(limpPickle)
    rageodd = pickle.load(limpPickle)
    rag = pickle.load(limpPickle)

artist, album, year, song = rage2
print(artist, album, year, song)

for songs in song:
    track, name = songs
    print(track, name)

for i in rageodd:
    print(i)
print("**" * 20)

for k in rageeven:
    print(k)
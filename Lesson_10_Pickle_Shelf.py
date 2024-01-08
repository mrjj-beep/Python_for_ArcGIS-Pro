import pickle
letters = ['a', 'b', 'c']
pickled_letters = pickle.dumps(letters)
print (pickled_letters)

import pickle
outfile = open('data.txt', 'wb')
letters = ['a', 'b', 'c']
pickle.dump(letters, outfile)
outfile.close( )

unpickled_letters = pickle.loads(pickled_letters)
print (unpickled_letters)

infile = open('data.txt', 'rb')
file_data = pickle.load(infile)
infile.close()
print (file_data)


import shelve
db_file = shelve.open('letters.txt', 'c')
db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file ['end'] = ['x', 'y', 'z']
db_file.close()


db_file = shelve.open('letters.txt', 'c')
print ( list( db_file.keys( ) ) )
['vowels', 'end']


print( 'vowels' in db_file )
del db_file ['vowels']


print( 'vowels' in db_file )
db_file.close()

# binary encode an input pattern, return a list of binary vectors
def encode(pattern, n_unique):
	encoded = list()
	for value in pattern:
		row = [0.0 for x in range(n_unique)]
		row[value] = 1.0
		encoded.append(row)
	return encoded

seq1 = [3, 0, 1, 2, 3]
encoded = encode(seq1, 5)
print encoded
#for vector in encoded:
#	print(vector)



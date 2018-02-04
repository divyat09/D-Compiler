# Change the filename

f=open(filename, 'r')
for line in f.readlines():
	Data= line.split(',')
	_input= []

	for param in Data:
		_input.append(param)

	IRepresentation= IRDS()
	IRDS.represent( _input )
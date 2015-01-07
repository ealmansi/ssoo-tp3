#!/usr/bin/python
from os import listdir
from os.path import join
from os.path import isfile
from bson.code import Code
from pymongo.connection import MongoClient
import argparse
from bson.son import SON
import matplotlib.pyplot as plt
import math

conn = MongoClient() 
db = conn.tp3

EJS_DIRS = ['ej1','ej2', 'ej3']
#EJS_DIRS = ['Ej1Ejemplo']

def plot(x, y):
  fig, ax1 = plt.subplots()
  ax1.plot(x, y, 'bo')
  plt.xlabel('helpfulness')
  plt.ylabel('average text length')
  plt.show()

def average(x):
	assert len(x) > 0
	return float(sum(x)) / len(x)

def pearson_def(x, y):
	assert len(x) == len(y)
	n = len(x)
	assert n > 0
	avg_x = average(x)
	avg_y = average(y)
	diffprod = 0
	xdiff2 = 0
	ydiff2 = 0
	for idx in range(n):
		xdiff = x[idx] - avg_x
		ydiff = y[idx] - avg_y
		diffprod += xdiff * ydiff
		xdiff2 += xdiff * xdiff
		ydiff2 += ydiff * ydiff
	return diffprod / math.sqrt(xdiff2 * ydiff2)



def run(code, incoll = 'reviews', outcoll = 'default'):
	print "Corriendo map_reduce sobre %s.%s" % ("amazon", incoll)
	collection = getattr(db, incoll)
	print collection
	for ej in  EJS_DIRS if code == 'all' else [ code ] :
		print
		print "Algoritmos a ejecutar en recurso %s" % ej
		with open(join(ej, 'map.js')) as mapping_func_file:
			with open(join(ej, 'reduce.js')) as reduce_func_file:
				if isfile(join(ej,'finalize.js')):
					finalize_func = Code(open(join(ej,'finalize.js')).read())
				else:
					finalize_func = None
				map_func = Code(mapping_func_file.read())
				reduce_func = Code(reduce_func_file.read())
				if args.outcoll == 'default':
					outcoll = ej 
				if finalize_func != None:
					collection.map_reduce(map_func, reduce_func, outcoll, finalize = finalize_func)
				else:
					collection.map_reduce(map_func, reduce_func, outcoll)

		print "El resultado de la operacion se encuentra almacenado en la colleccion %s." % ej
		print 

		if ej == 'ej1':
			getattr(db,outcoll).aggregate([{"$sort" : SON([("value",-1)])},{"$limit" : 12},{"$out" : outcoll}])
			coll = getattr(db,outcoll).find()
			print "Los producId de las 12 peliculas mejor rankeadas en amazon son (",
			for res in coll:
				print res['_id'],
			print ")"   

		if ej == 'ej2':
			getattr(db,outcoll).aggregate([{"$out" : outcoll}])
			for i in range(1,6):
				coll = getattr(db,outcoll).find().sort("value.s" + str(i),-1).limit(5)
				print u"Las 5 palabras mas frecuentemente usadas en las rese\xf1as con score = %s son (" % i,
				for res in coll:
					print "%s" % res['_id'],
				print ")"
	 			
		if ej == 'ej3':
			getattr(db,outcoll).aggregate([{"$out" : outcoll}])
			coll = getattr(db,outcoll).find()
			help = []
			length = []
			for res in coll:
				print "helpfulness:",
				print res['_id'],
				help.append(float(res['_id']))
				print ", average length:",
				print res['value'] 
				length.append(res['value'])
			print
			print "The Pearson correlation is: %s" % pearson_def(help,length)
			if(args.plot):
				plot(help,length)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("code", default = 'all', help = "el directorio donde se encuentran los scripts de map y reduce, default corre todo los directorios ejx") 
	parser.add_argument("--incoll",  default = 'reviews', help = "la coleccion donde se ejecutara el mapReduce")
	parser.add_argument("--outcoll",  default = 'default', help = "la coleccion de salida del mapReduce")
	parser.add_argument("--plot",  action="store_true", help = "Plot en el ej3")
	args = parser.parse_args()

	run(args.code, args.incoll, args.outcoll)


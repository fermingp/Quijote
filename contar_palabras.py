"""
Fermín González Pereiro
"""

"""
Programa de contar palabras que hay que probar con el fichero quijote_s05.txt y  copiamos
la salida y la ponemos en un fichero llamado out_quijote_s05.txt

Hay que probar también el programa con el libro completo y copiamos la salida
en un fichero llamado out_quijote.txt
"""
from pyspark import SparkContext
import sys



def main(infile, outfile):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(infile)
        words_rdd = data.map(lambda x: len(x.split()))
        nwords = words_rdd.sum()
        with open(outfile, 'w') as outfile: 
            outfile.write("El numero total de palabras en el texto es: ")
            outfile.write(str(nwords))
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
       print("Uso: python3 {0} <file>".format(sys.argv[0]))
    infile = sys.argv[1]
    outfile = sys.argv[2]
    main(infile, outfile)
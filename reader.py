import test
import json 
import codecs

fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("const myData = \n" + str(test.final) + ";")
fhand.write("export {myData};")
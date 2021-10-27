import lsystem as LS
import argsChecker as val
import sys
import getopt

numIter=4
axiom='F'
rotation=90
updateStr="FF-[-F+F+F]+[+F-F-F]"

#print ('numIter=', numIter)
#print ('axiom=', axiom)
#print ('angle=', rotation)
#print ('updateStr=', updateStr)

#print(type(numIter))
#print(type(axiom))
#print(type(rotation))
#print(type(updateStr))

#call validate functions
myChecker=val.argsChecker()
myChecker.checkAngle(rotation)
myChecker.checkAxiom(axiom)
myChecker.checkIter(numIter)
myChecker.checkUpdateStrLetters(updateStr)
myChecker.checkUpdateStrRecursion(updateStr)

#creat L-systems obj
myLS = LS.LSystem()

#for updateStr, if valid, add each char-> updateStr to Dict
for char in updateStr:
    myLS.addToDict(char, char)
myLS.addToDict(axiom, updateStr)
#build treeSeq
treeSeq=myLS.makeLSystem(numIter, axiom)

print(treeSeq)
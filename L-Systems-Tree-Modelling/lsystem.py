class LSystem:
    """
    Class to describe an L-system created from user input.
    A class to represent atributes of the main L-Systems Tree GUI window 
    ...

    Attributes
    ----------
    Methods
    ----------
        :__init__: constuctor
        :addToDict(self, myKey, myValue): adds a key,value pair to the L-Systems dictionary 
        :applyRule(self, beforeChar): applies update rule to a single character
        :processWord(self, beforeWord): constructs a new string by iterating over characters of a string and calling applyRule.
        :makeLSystem(self, nIters, axiom): generates the L-System string
    """

    rulesDict = dict()

    def __init__(self) -> None:
        pass

    def addToDict(self, myKey, myValue):
        """
        Given a validated update string (validation done in processinput.py), store updateStrings in a dictionary
        :param self: class instance, defaults to self
        :param myKey: string, required, input symbol
        :param myVal: string, required, update symbol
        :return string: string, updated value
        :raises: none
        """
        # most recent rule applied in case of duplicate keys
        LSystem.rulesDict[myKey] = myValue
        return LSystem.rulesDict[myKey]

    def applyRule(self, beforeChar):
        """
        method to apply a rule to a character, from the dictionary defined above
        :param self: class instance, defaults to self
        :param beforeChar: string, required, symbol to be looked up in dict
        :return string: string, updated value
        :raises: none
        """
        afterStr = ""
        afterStr = LSystem.rulesDict[beforeChar]
        return afterStr

    def processWord(self, beforeWord):
        """
        method to process a string by calling the applyRules method to each character
        :param self: class instance, defaults to self
        :param beforeWord: string, required, input word
        :return afterWord: string, updated word
        :raises: none
        """
        afterWord = ""
        for char in beforeWord:
            afterWord = afterWord + self.applyRule(char)
        return afterWord

    def makeLSystem(self, nIters, axiom):
        """
        method to create an L-system, given a user-defined number of iterations, start character and update rules.
        :param self: class instance, defaults to self
        :param nIters: int, required, number of iterations
        :param axiom: string, required, chosen axiom symbol
        :return endWord: string, final tree sequence
        :raises: none
        """
        startWord = axiom
        for i in range(nIters):
            endWord = self.processWord(startWord)
            startWord = endWord
        return endWord
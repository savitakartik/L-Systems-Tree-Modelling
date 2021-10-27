class LSystem:
    """
    Class to describe an L-system created from user input.
    """

    rulesDict = dict()

    def __init__(self) -> None:
        pass

    def addToDict(self, myKey, myValue):
        """
        Given a validated update string (validation done in processinput.py), store updateStrings in a dictionary
        """
        # most recent rule applied in case of duplicate keys
        LSystem.rulesDict[myKey] = myValue

    def applyRule(self, beforeChar):
        """
        method to apply a rule to a character, from the dictionary defined above
        """
        afterStr = ""
        afterStr = LSystem.rulesDict[beforeChar]
        return afterStr

    def processWord(self, beforeWord):
        """
        method to process a string by calling the applyRules method to each character
        """
        afterWord = ""
        # write as recursive function?
        for char in beforeWord:
            afterWord = afterWord + self.applyRule(char)
        return afterWord

    def makeLSystem(self, nIters, axiom):
        """
        method to create an L-system, given a user-defined number of iterations, start character and update rules.
        """
        startWord = axiom
        for i in range(nIters):
            endWord = self.processWord(startWord)
            startWord = endWord
        return endWord
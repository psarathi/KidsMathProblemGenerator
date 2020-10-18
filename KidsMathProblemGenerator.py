import random
import os
from datetime import date

operations = ['+', '-']
delimiter = '-----'
problems = []
FILENAME = 'MathProblems.txt'
FILENAME_ANSWERS = 'MathProblems_Answers.txt'
PROBLEMS_IN_A_ROW = 5
NUMBER_OF_PROBLEMS = 12
SPACER = ' '*10
numerators = []
denominators = []
operators = []
answers = []
printableLines = []
FOOTER = date.today().strftime("%m/%d/%Y")


def generateNumeratorDenomenator():
    return random.randint(100, 999), random.randint(10, 999)


def generateMathProblems(num=NUMBER_OF_PROBLEMS):
    for i in range(num):
        operation = operations[random.randint(0, 1)]
        numerator, denominator = generateNumeratorDenomenator()
        if operation == '-' and denominator > numerator:
            while denominator > numerator:
                numerator, denominator = generateNumeratorDenomenator()
        numeratorString = str(numerator)
        denominatorString = str(denominator)
        result = eval(numeratorString + operation + denominatorString)
        numerators.append(numeratorString)
        operators.append(operation)
        denominators.append(denominatorString)
        answers.append(str(result))


def generatePrintableLines(printAnswers=False):
    i = 0
    while i < len(numerators):
        printableLines.append(SPACER.join(
            [' '*(5-len(num)) + num for num in numerators[i:i+PROBLEMS_IN_A_ROW]]))
        printableLines.append('\n')
        printableLines.append(SPACER.join(
            [o + ' '*(4-len(d)) + d for o, d in zip(operators[i:i+PROBLEMS_IN_A_ROW], denominators[i:i+PROBLEMS_IN_A_ROW])]))
        printableLines.append('\n')
        printableLines.append(SPACER.join([delimiter]*5))
        printableLines.append('\n')
        printableLines.append(SPACER.join(
            [' '*(5-len(ans)) + ans for ans in answers[i:i+PROBLEMS_IN_A_ROW]])) if printAnswers else ''
        i += PROBLEMS_IN_A_ROW
        printableLines.append('\n'*5) if i < len(numerators) else ''

    # printableLines.append(FOOTER)


def printToFile(filename):
    with open(filename, 'w+') as out_file:
        for line in printableLines:
            out_file.write(line)


if __name__ == "__main__":
    generateMathProblems()
    generatePrintableLines()
    # print('\t\t'.join(numerators))
    # print('\t\t'.join(denominators))
    # print(operators)
    # print(answers)
    printToFile(FILENAME)

    printableLines.clear()
    generatePrintableLines(printAnswers=True)

    printToFile(FILENAME_ANSWERS)

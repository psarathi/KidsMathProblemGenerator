import operator
import random
from datetime import date
from math import floor

operationsDisplay = ['+', '-', 'x', '÷']
operations = {'+': operator.add, '-': operator.sub, 'x': operator.mul, '÷': operator.truediv}
delimiter = '-----'
problems = []
FILENAME = 'MathProblems.txt'
FILENAME_ANSWERS = 'MathProblems_Answers.txt'
PROBLEMS_IN_A_ROW = 5
NUMBER_OF_PROBLEMS = 35  # Use 35 for 1 page of well formatted problems on A4 size paper
SPACER = ' ' * 10
numerators = []
denominators = []
operators = []
answers = []
printableLines = []
FOOTER = date.today().strftime("%m/%d/%Y")


def generateNumeratorDenominator(operation):
    if operation not in operationsDisplay:
        raise KeyError("Operation '{op}' is not a valid operation".format(op=operation))
    if operation == '+' or operation == '-':
        return random.randint(100, 999), random.randint(10, 999)
    if operation == 'x':
        return random.randint(100, 999), random.randint(2, 9)
    if operation == '÷':
        return random.randint(10, 99), random.randint(2, 9)


def getMathProblem(numerator, denominator, operation):
    if not numerator or not denominator or not operation:
        raise ValueError("Required parameters are missing")
    if operation == '-' and denominator > numerator:
        while denominator > numerator:
            numerator, denominator = generateNumeratorDenominator(operation)
        return numerator, denominator
    if operation == '÷' and numerator / denominator > 10:
        while numerator / denominator > 10:
            numerator, denominator = generateNumeratorDenominator(operation)
    return numerator, denominator


def getAnswer(numerator, denominator, operation):
    predicate = operations.get(operation)
    if operation == '÷':
        quotient: int = floor(predicate(numerator, denominator))
        remainder = numerator % denominator
        if remainder != 0:
            return "{quo}R{rem}".format(quo=quotient, rem=remainder)
        return quotient
    return predicate(numerator, denominator)


def generateMathProblems(num=NUMBER_OF_PROBLEMS):
    for i in range(num):
        operation = operationsDisplay[random.randint(0, len(operationsDisplay) - 1)]
        numerator, denominator = generateNumeratorDenominator(operation)
        numerator, denominator = getMathProblem(numerator, denominator, operation)
        result = getAnswer(numerator, denominator, operation)
        numerators.append(str(numerator))
        operators.append(operation)
        denominators.append(str(denominator))
        answers.append(str(result))


def generatePrintableLines(printAnswers=False):
    i = 0
    while i < len(numerators):
        printableLines.append(SPACER.join(
            [' ' * (5 - len(num)) + num for num in numerators[i:i + PROBLEMS_IN_A_ROW]]))
        printableLines.append('\n')
        printableLines.append(SPACER.join(
            [o + ' ' * (4 - len(d)) + d for o, d in
             zip(operators[i:i + PROBLEMS_IN_A_ROW], denominators[i:i + PROBLEMS_IN_A_ROW])]))
        printableLines.append('\n')
        printableLines.append(SPACER.join([delimiter] * 5))
        printableLines.append('\n')
        printableLines.append(SPACER.join(
            [' ' * (5 - len(ans)) + ans for ans in answers[i:i + PROBLEMS_IN_A_ROW]])) if printAnswers else ''
        i += PROBLEMS_IN_A_ROW
        printableLines.append('\n' * 5) if i < len(numerators) else ''

    # printableLines.append(FOOTER)


def printToFile(filename):
    with open(filename, 'w+') as out_file:
        for line in printableLines:
            out_file.write(line)


if __name__ == "__main__":
    generateMathProblems()
    generatePrintableLines()
    printToFile(FILENAME)
    printableLines.clear()
    generatePrintableLines(printAnswers=True)
    printToFile(FILENAME_ANSWERS)

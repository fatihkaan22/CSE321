def bruteForcePolynomialEvaluation(x, coefficients):
    result = 0
    for i in range(len(coefficients)):
        result = result + (x ** i) * coefficients[i]
    return result


print(bruteForcePolynomialEvaluation(3, [2, 4]))

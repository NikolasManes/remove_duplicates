def main():
    variables_number = 5
    pows = [3, 4, 5, 1, 4]
    factors = [1, 3, -2, 6, 1, 5]
    mfv = multi_variable_function(variables_number, pows, factors)
    print(mfv.value_of_function([1, 1, 1, 1, 1]))
    print(mfv.partial_derivative(3, 4, 0.1))

# Multi variable poynomial function 
class multi_variable_function:
    def __init__(self, variables_number, pows, factors):
        self.variables_number = variables_number
        self.pows = pows
        self.factors = factors
        if variables_number != len(pows) and variables_number != len(factors) - 1:
            raise Exception("The number of factors - 1, powers and variables must be the same")

    def value_of_term(self, value, index):
        return self.factors[index] * value ** self.pows[index]

    def value_of_function(self, values):
        if self.variables_number != len(values):
            raise Exception("You must give a value fro every variable")
        value = 0
        for i in range(len(values)):
            value += self.value_of_term(values[i], i)
        value += self.factors[-1]
        return value

    def partial_derivative(self, value, variable_index, approx):
        return (self.value_of_term(value + approx, variable_index) - self.value_of_term(value - approx, variable_index))/(2 * approx)


main()
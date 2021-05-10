def main():
    size = 5
    pows = [3, 4, 5, 1, 4]
    factors = [1, 3, -2, 6, 1, 5]
    mfv = multi_variable_function(size, pows, factors)
    print(mfv.value_of_function([1, 1, 1, 1, 1]))


class multi_variable_function:
    def __init__(self, size, pows, factors):
        self.size = size
        self.pows = pows
        self.factors = factors
        if size != len(pows) and size != len(factors - 1):
            raise Exception("The number of factors, powers and variables must be the same")

    def value_of_function(self, values):
        if self.size != len(values):
            raise Exception("You must give a value fro every variable")
        value = 0
        for i in range(len(values)):
            value += self.factors[i] * values[i] ** self.pows[i]
        value += self.factors[-1]
        return value

    #def partial_derivative(var_i):



main()
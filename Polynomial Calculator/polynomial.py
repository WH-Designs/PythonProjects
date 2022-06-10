import random

from adts.array import Array


class Polynomial:
    def __init__(self, coefficients: list):

        self._coefficients = Array(len(coefficients))
        for i in range(len(coefficients)):
            self._coefficients[i] = coefficients[i]

    @staticmethod
    def generate():
        number_of_coefficients = random.randint(2, 8)
        coefficients = list()

        for i in range(number_of_coefficients):
            factor = 1 if random.choice([True, False]) is True else -1
            coefficients.append(random.randint(0, 10) * factor)

        return Polynomial(coefficients)

    def __str__(self) -> str:
        poly_string = str()

        for i in range(len(self._coefficients) - 1, -1, -1):
            term = f'{self._coefficients[i]:+}x^{i} ' if i != 0 else f'{self._coefficients[i]:+}'
            poly_string += term

        return poly_string

    def __eq__(self, other) -> bool:
        if not isinstance(other, Polynomial):
            return False
        return self._coefficients == other._coefficients

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError('Other is not an Polynomial')

        smaller_coefficient_list = Array.clone(self._coefficients) \
            if len(self._coefficients) < len(other._coefficients) else Array.clone(other._coefficients)

        larger_coefficient_list = Array.clone(self._coefficients) \
            if len(self._coefficients) >= len(other._coefficients) else Array.clone(other._coefficients)

        for i in range(len(smaller_coefficient_list)):
            larger_coefficient_list[i] += smaller_coefficient_list[i]

        return Polynomial(larger_coefficient_list)

    def __sub__(self, other):

        smaller_coefficient_list = Array.clone(self._coefficients) \
            if len(self._coefficients) < len(other._coefficients) else Array.clone(other._coefficients)

        larger_coefficient_list = Array.clone(self._coefficients) \
            if len(self._coefficients) >= len(other._coefficients) else Array.clone(other._coefficients)

        lower_coefficient_list = Array.clone(other._coefficients)

        for i in range(len(lower_coefficient_list)):
            lower_coefficient_list[i] *= -1

        for i in range(len(smaller_coefficient_list)):
            larger_coefficient_list[i] = self._coefficients[i] + lower_coefficient_list[i]

        return Polynomial(larger_coefficient_list)

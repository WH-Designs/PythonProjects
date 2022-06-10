from lab_polynomial_calculator.polynomial import Polynomial


def main():

    # polynomial = Polynomial([60, 50, -40, 30, -20, 10])
    #
    # print(polynomial)

    polynomial_random1 = Polynomial.generate()
    polynomial_random2 = Polynomial.generate()

    print(f'Polynomial 1: {polynomial_random1}')
    print(f'Polynomial 2: {polynomial_random2}')

    print(f'Adding the two polynomials together:  {polynomial_random1 + polynomial_random2}')

    polynomial_random3 = Polynomial.generate()
    polynomial_random4 = Polynomial.generate()

    print(f'Polynomial 3: {polynomial_random3}')
    print(f'Polynomial 4: {polynomial_random4}')

    print(f'Subtracting the two polynomials together:  {polynomial_random1 - polynomial_random2}')

if __name__ == '__main__':
    main()

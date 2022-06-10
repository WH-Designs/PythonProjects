import unittest

from lab_polynomial_calculator.polynomial import Polynomial


class PolynomialTest(unittest.TestCase):

    def test_add_same_number_coefficients(self):
        # Arrange
        poly1 = Polynomial([20, 30, 40, 50, 60])
        poly2 = Polynomial([10, 9, 8, 7, 6])
        answer = Polynomial([30, 39, 48, 57, 66])

        # Act
        my_answer = poly1 + poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_add_same_number_coefficients_negative_signs(self):
        # Arrange
        poly1 = Polynomial([-20, 30, -40, 50, 60])
        poly2 = Polynomial([10, 9, -8, 7, -6])
        answer = Polynomial([-10, 39, -48, 57, 54])

        # Act
        my_answer = poly1 + poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_add_different_number_coefficients(self):
        # Arrange
        poly1 = Polynomial([-20, 30, -40, 50, 60, 70])
        poly2 = Polynomial([10, 9, -8])
        answer = Polynomial([-20, 30, -40, 60, 69, 62])

        # Act
        my_answer = poly1 + poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_add_different_number_coefficients(self):
        # Arrange
        poly1 = Polynomial([-20, 30, -40, 50, 60, 70])
        poly2 = Polynomial([10, 9, -8])
        answer = Polynomial([-10, 39, -48, 50, 60, 70])

        # Act
        my_answer = poly1 + poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_add_different_number_coefficients_poly_2_larger(self):
        # Arrange
        poly1 = Polynomial([20, 30, 40, 50, 60])
        poly2 = Polynomial([10, 9, 8, 7, 6, 5, 4])
        answer = Polynomial([30, 39, 48, 57, 66, 5, 4])

        # Act
        my_answer = poly1 + poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_sub_same_number_coefficients(self):
        # Arrange
        poly1 = Polynomial([20, 30, 40, 50, 60])
        poly2 = Polynomial([10, 9, 8, 7, 6])
        answer = Polynomial([10, 21, 32, 43, 54])

        # Act
        my_answer = poly1 - poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_sub_same_number_coefficients_negative_signs(self):
        # Arrange
        poly1 = Polynomial([-20, 30, -40, 50, 60])
        poly2 = Polynomial([10, 9, -8, 7, -6])
        answer = Polynomial([-30, 21, -32, 43, 66])

        # Act
        my_answer = poly1 - poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_sub_different_number_coefficients(self):
        # Arrange
        poly1 = Polynomial([20, 30, -40, -20])
        poly2 = Polynomial([-10, -9, 8])
        answer = Polynomial([30, 39, -48, -20])

        # Act
        my_answer = poly1 - poly2

        # Assert
        self.assertEqual(answer, my_answer)

    def test_sub_different_number_coefficients_poly_2_larger(self):
        # Arrange
        poly1 = Polynomial([20, 30])
        poly2 = Polynomial([-10, -9, 8, -7])
        answer = Polynomial([30, 39, 8, -7])

        # Act
        my_answer = poly1 - poly2

        # Assert
        self.assertEqual(answer, my_answer)
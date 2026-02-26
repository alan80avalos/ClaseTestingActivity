# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from class_exercises import (
    divide, get_grade, is_even, is_triangle,
    check_number_status,
    validate_password,
    calculate_total_discount,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
    validate_credit_card,
    validate_date,
    check_flight_eligibility,
    validate_url,
    calculate_quantity_discount,
    check_file_size,
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
    get_weather_advisory
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

class TestWhiteBoxCheckNumberStatus(unittest.TestCase):
    def test_is_a_number_positive(self):
        """
        Checks if a given number is positive.
        """
        self.assertEqual(check_number_status(10), "Positive")
    
    def test_is_a_number_negative(self):
        """
        Checks if a given number is negative.
        """
        self.assertEqual(check_number_status(-5), "Negative")
    
    def test_is_number_zero(self):
        """
        Checks if a given number is zero.
        """
        self.assertEqual(check_number_status(0), "Zero")

class TestWhiteBoxValidatePassword(unittest.TestCase):
    def test_is_a_validate_password(self):
        """
        Checks if a given password is valid.
        """
        self.assertTrue(validate_password("Asdfgh3!"))

    def test_is_a_invalidate_password_by_length(self):
        """
        Checks if a given password is invalid by length.
        """
        self.assertFalse(validate_password("Sdfh3!"))

    def test_is_a_invalidate_password_by_uppercase(self):
        """
        Checks if a given password is invalid by uppercase letter.
        """
        self.assertFalse(validate_password("asdfgh3!"))
    
    def test_is_a_invalidate_password_by_lowercase (self):
        """
        Checks if a given password is invalid by lowercase letter.
        """
        self.assertFalse(validate_password("ASDFGHG3!"))

    def test_is_a_invalidate_password_by_digit(self):
        """
        Checks if a given password is invalid by digit.
        """
        self.assertFalse(validate_password("Asdfghj!"))

    def test_is_a_invalidate_password_by_special_digit (self):
        """
        Checks if a given password is invalid by special character.
        """
        self.assertFalse(validate_password("Asdfgh34"))

class TestWhiteBoxCalculateTotalDiscount(unittest.TestCase):
    def test_no_discount(self):
        """
        Checks if the total discount is 0 when the total amount is less than 100.
        """
        self.assertEqual(calculate_total_discount(70), 0)

    def test_10_percent_discount(self):
        """
        Checks if the total discount is 10% of the total amount when the total amount is between 100 and 500.
        """
        self.assertEqual(calculate_total_discount(250), 25)
    
    def test_20_percent_discount(self):
        """
        Checks if the total discount is 20% of the total amount when the total amount is greater than 500.
        """
        self.assertEqual(calculate_total_discount(1000), 200)

class TestWhiteBoxCalculateOrderTotal(unittest.TestCase):
    def test_no_discount(self):
        """
        Checks if the total order is the sum of the price of the items when the quantity is less than 5.
        """
        items = [{"quantity": 3, "price": 100}]
        self.assertEqual(calculate_order_total(items), 300)
    
    def test_5_discount(self):
        """
        Checks if the total order is the sum of the price of the items with a 5% discount when the quantity is between 6 and 10.
        """
        items = [{"quantity": 7, "price": 100}]
        self.assertEqual(calculate_order_total(items), 665)
    
    def test_10_discount(self):
        """
        Checks if the total order is the sum of the price of the items with a 10% discount when the quantity is greater than 10.
        """
        items = [{"quantity": 20, "price": 100}]
        self.assertEqual(calculate_order_total(items), 1800)

class TestWhiteBoxCalculate_items_ShippingCost(unittest.TestCase):
    def test_standard_10(self):
        """
        Checks if the shipping cost is 10 when the total weight is less than 5 and the shipping method is standard.
        """
        items = [{"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)
    
    def test_standard_15(self):
        """
        Checks if the shipping cost is 15 when the total weight is between 5 and 10 and the shipping method is standard.
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)
    
    def test_standard_20(self):
        """
        Checks if the shipping cost is 20 when the total weight is greater than 10 and the shipping method is standard.
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)
    
    def test_express_20(self):
        """
        Checks if the shipping cost is 20 when the total weight is less than 5 and the shipping method is express.
        """
        items = [{"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_30(self):
        """
        Checks if the shipping cost is 30 when the total weight is between 5 and 10 and the shipping method is express.
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_40(self):
        """
        Checks if the shipping cost is 40 when the total weight is greater than 10 and the shipping method is express.
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)
    

class TestWhiteBoxValidateLogin(unittest.TestCase):
    def test_valid_credentials(self):
        """
        Checks if the login is successful when the username and password are correct.
        """
        self.assertEqual(validate_login("alan123", "12345678"), "Login Successful")
    
    def test_invalid_credentials_username(self):
        """
        Checks if the login fails when the username is incorrect.
        """
        self.assertEqual(validate_login("alan", "12345678"), "Login Failed")

    def test_invalid_credentials_password(self):
        """
        Checks if the login fails when the password is incorrect.
        """
        self.assertEqual(validate_login("alan123", "123"), "Login Failed")


class TestWhiteBoxVerifyAge(unittest.TestCase):
    def test_elegible_age(self):
        """
        Checks if the age is eligible when the age is between 18 and 65.
        """
        self.assertEqual(verify_age(19), "Eligible")

    
    def test_no_elegible_less_age(self):
        """
        Checks if the age is not eligible when the age is less than 18.
        """
        self.assertEqual(verify_age(8), "Not Eligible")

    def test_no_elegible_hight_age(self):
        """
        Checks if the age is not eligible when the age is greater than 65.
        """
        self.assertEqual(verify_age(100), "Not Eligible")

class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    def test_categorize_a(self):
        """
        Checks if the product is categorized as A when the price is less than 50.
        """
        self.assertEqual(categorize_product(30), "Category A")

    def test_categorize_b(self):
        """
        Checks if the product is categorized as B when the price is between 51 and 100.
        """
        self.assertEqual(categorize_product(70), "Category B")

    def test_categorize_c(self):
        """
        Checks if the product is categorized as C when the price is between 101 and 200.
        """
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_d(self):
        """
        Checks if the product is categorized as D when the price is greater than 200.
        """
        self.assertEqual(categorize_product(300), "Category D")

class TestWhiteBoxValidateEmail(unittest.TestCase):
    def test_email_valid(self):
        """
        Checks if the email is valid when it contains an "@" and a ".".
        """
        self.assertEqual(validate_email("alanr7570@gmail.com"), "Valid Email")

    
    def test_email_without_at(self):
        """
        Checks if the email is invalid when it doesn't contain an "@".
        """
        self.assertEqual(validate_email("alanr7570gmail.com"), "Invalid Email")

    def test_email_without_point(self):
        """
        Checks if the email is invalid when it doesn't contain a ".".
        """
        self.assertEqual(validate_email("alanr7570@gmailcom"), "Invalid Email")

class TestWhiteBoxCalculateCelsiusToFahrenheit(unittest.TestCase):
    def test_valid_temperature_number(self):
        """
        Checks if the temperature is valid when the temperature is between -100 and 100.
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_invalid_less_temperature_number(self):
        """
        Checks if the temperature is invalid when the temperature is less than -100.
        """
        self.assertEqual(celsius_to_fahrenheit(-300), "Invalid Temperature")

    def test_valid_hight_temperature_number(self):
        """
        Checks if the temperature is invalid when the temperature is greater than 100.
         """
        self.assertEqual(celsius_to_fahrenheit(200),  "Invalid Temperature")

class TestWhiteBoxValidateCreditCard(unittest.TestCase):
    def test_valid_card_numbers(self):
        """
        Checks if the credit card number is valid when it contains between 13 and 16 digits.
        """
        self.assertEqual(validate_credit_card("10234567891234"), "Valid Card")
    
    def test_invalid_card_numbers_by_length(self):
        """
        Checks if the credit card number is invalid when it contains less than 13 digits or more than 16 digits.
        """
        self.assertEqual(validate_credit_card("123"), "Invalid Card")
    
    def test_invalid_card_numbers_by_no_digit(self):
        """
        Checks if the credit card number is invalid when it contains non-digit characters.
        """
        self.assertEqual(validate_credit_card("1023456781234a"), "Invalid Card")

class TestWhiteBoxValidateDate(unittest.TestCase):
    def test_valid_date(self):
        """
        Checks if the date is valid when the year is between 1900 and 2100, the month is between 1 and 12, and the day is between 1 and 31.
        """
        self.assertEqual(validate_date(2005, 10, 1), "Valid Date")

    def test_invalid_date_by_year(self):
        """
        Checks if the date is invalid when the year is less than 1900 or greater than 2100.
        """
        self.assertEqual(validate_date(3005, 10, 1), "Invalid Date")

    def test_invalid_date_by_month(self):
        """
        Checks if the date is invalid when the month is less than 1 or greater than 12.
        """
        self.assertEqual(validate_date(2005, 13, 1), "Invalid Date")

    def test_invalid_date_by_day(self):
        """
        Checks if the date is invalid when the day is less than 1 or greater than 31.
        """
        self.assertEqual(validate_date(2005, 10, 50), "Invalid Date")

class TestWhiteBoxCheckFligthEligibility(unittest.TestCase):
    def test_age_eligible(self):
        """
        Checks if the passenger is eligible to book a flight when the age is between 18 and 65 and the passenger is not a frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(20, False), "Eligible to Book")

    def test_less_age_no_eligible(self):
        """
        Checks if the passenger is not eligible to book a flight when the age is less than 18 and the passenger is not a frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(10, False), "Not Eligible to Book")
    
    def test_higth_age_eligible(self):
        """
        Checks if the passenger is not eligible to book a flight when the age is greater than 65 and the passenger is not a frequent flyer.
        """
        self.assertEqual(check_flight_eligibility(100, False), "Not Eligible to Book")

    def test_flequent_eligible(self):
        """
        Checks if the passenger is eligible to book a flight when the passenger is a frequent flyer, regardless of age.
        """
        self.assertEqual(check_flight_eligibility(5, True), "Eligible to Book")

class TestWhiteBoxValidateUrl(unittest.TestCase):
    def test_invalid_url_higth_length(self):
        """
        Checks if the URL is invalid when the length of the URL is greater than 50 characters.
        """
        self.assertEqual(validate_url("http://www.googleqwertyuiopasdfghjklñjadskfkñasdflkajslñfdkalksñdjfñlaksdjflñsadjfñlsaaslkdfjasdkfalksdfjalksdfjñlaksdfjañsldfjalsdjfañlsdjfladskjflkdsafjjdfñlasdjfñlasdjfñlkasjdfñlksajdfñlasjdflasjdfñlasjdflksajflsajfdñlsajfdlsadjfzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwjasdfjkasñlkfdlajsfdñlkjsadfñlkjsadlfñkajsdñlfjsañlfdjsaldfjasldfjsañldfjalsfdjsadljfdsafkjsadkfasertyuiopasdfghj.com"), "Invalid URL")

    def test_valid_url_with_http(self):
        """
        Checks if the URL is valid when it starts with "http://" and has a length of 255 characters or less.
        """
        self.assertEqual(validate_url("http://www.google.com"), "Valid URL")

    def test_valid_url_with_https(self):
        """
        Checks if the URL is valid when it starts with "https://" and has a length of 255 characters or less.
        """
        self.assertEqual(validate_url("https://www.google.com"), "Valid URL")

    def test_invalid_url_without_protocol(self):
        """
        Checks if the URL is invalid when it doesn't start with "http://" or "https://".
        """
        self.assertEqual(validate_url("www.google.com"), "Invalid URL")

class TestWhiteBoxCalculateQuantityDiscount(unittest.TestCase):
    def test_no_discount(self):
        """
        Checks if the quantity discount is "No Discount" when the quantity is less than 5.
        """
        self.assertEqual(calculate_quantity_discount(4), "No Discount")
        
    def test_5_percent_discount(self):
        """
        Checks if the quantity discount is "5% Discount" when the quantity is between 6 and 10.
        """
        self.assertEqual(calculate_quantity_discount(9), "5% Discount")
        
    def test_10_percent_discount(self):
        """
        Checks if the quantity discount is "10% Discount" when the quantity is greater than 10.
        """
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")

class TestWhiteBoxCheckFileSize(unittest.TestCase):
    def test_size_valid(self):
        """
        Checks if the file size is valid when the size is between 0 and 1048576 bytes (1 MB).
        """
        self.assertEqual(check_file_size(1000), "Valid File Size")
    
    def test_size_bigger_invalid(self):
        """
        Checks if the file size is invalid when the size is greater than 1048576 bytes (1 MB).
        """
        self.assertEqual(check_file_size(104857600), "Invalid File Size")
    
    def test_size_lower_invalid(self):
        """
        Checks if the file size is invalid when the size is less than 0 bytes.
        """
        self.assertEqual(check_file_size(-1), "Invalid File Size")

class TestWhiteBoxCheckLoanEligibility(unittest.TestCase):
    def test_less_income_no_elegible(self):
        """
        Checks if the loan is not eligible when the income is less than 30000, regardless of the credit score.
        """
        self.assertEqual(check_loan_eligibility(200, 720), "Not Eligible")

    def test_normal_income_and_less_score(self):
        """
        Checks if the loan is a standard loan when the income is between 30000 and 60000 and the credit score is greater than 700.
        """
        self.assertEqual(check_loan_eligibility(40020, 720), "Standard Loan")

    def test_normal_income_and_less_score(self):
        """
        Checks if the loan is a secured loan when the income is between 30000 and 60000 and the credit score is less than or equal to 700.
        """
        self.assertEqual(check_loan_eligibility(40000, 600), "Secured Loan")

    def test_higth_income_and_less_score(self):
        """
        Checks if the loan is a standard loan when the income is greater than 60000 and the credit score is less than or equal to 750.
        """
        self.assertEqual(check_loan_eligibility(50000, 620), "Secured Loan")

    def test_higth_income_and_hight_score(self):
        """
        Checks if the loan is a premium loan when the income is greater than 60000 and the credit score is greater than 750.
        """
        self.assertEqual(check_loan_eligibility(70000, 752), "Premium Loan")

    
class TestWhiteBoxCalculateShippingCost(unittest.TestCase):
    def test_cost_5(self):
        """
        Checks if the shipping cost is 5 when the weight is less than or equal to 1 and the dimensions are less than or equal to 10.
        """
        self.assertEqual(calculate_shipping_cost(1, 5, 5, 5), 5)

    def test_cost_10(self):
        """
        Checks if the shipping cost is 10 when the weight is between 1 and 5 and the dimensions are between 11 and 30.
        """
        self.assertEqual(calculate_shipping_cost(3, 15, 15, 15), 10)

    
    def test_cost_20(self):
        """
        Checks if the shipping cost is 20 when the weight is greater than 5 or the dimensions are greater than 30.
        """
        self.assertEqual(calculate_shipping_cost(3, 40, 15, 15), 20)

class TestWhiteBoxGradeQuiz(unittest.TestCase):
    def test_pass_quiz(self):
        """
        Checks if the quiz is passed when the score is greater than or equal to 5 and the number of attempts is less than or equal to 2.
        """
        self.assertEqual(grade_quiz(8, 1), "Pass")
    
    def test_condition_pass_quiz(self):
        """
        Checks if the quiz is conditionally passed when the score is greater than or equal to 5 and the number of attempts is less than or equal to 3.
        """
        self.assertEqual(grade_quiz(8, 3), "Conditional Pass")

    def test_fail_quiz(self):
        """
        Checks if the quiz is failed when the score is less than 5 or the number of attempts is greater than 3.
        """
        self.assertEqual(grade_quiz(10, 5), "Fail")

class TestWhiteBoxAuthenticateUser(unittest.TestCase):
    def test_is_admin_user(self):
        """
        Checks if the user is an admin when the username is "admin" and the password is "admin123".
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_is_a_user(self):
        """
        Checks if the user is a regular user when the username is not "admin" and the password is not "admin123".
        """
        self.assertEqual(authenticate_user("user123", "123456789"), "User")

    def test_is_a_invalid_user_with_username_invalid(self):
        """
        Checks if the user is invalid when the username is not "admin" and the password is "admin123".
        """
        self.assertEqual(authenticate_user("user", "123456789"), "Invalid")
    
    def test_is_a_invalid_user_with_password_invalid(self):
        """
        Checks if the user is invalid when the username is "admin" and the password is not "admin123".
        """
        self.assertEqual(authenticate_user("user122112", "12"), "Invalid")

class TestWhiteBoxGetWeatherAdivisory(unittest.TestCase):
    def test_stay_hydrated(self):
        """
        Checks if the advisory is "High Temperature and Humidity. Stay Hydrated." when the temperature is greater than or equal to 30 and the humidity is greater than or equal to 80.
        """
        self.assertEqual(get_weather_advisory(35, 90), "High Temperature and Humidity. Stay Hydrated.")

    def test_bundle_up(self):
        """
        Checks if the advisory is "Low Temperature. Bundle Up!" when the temperature is less than or equal to 0 and the humidity is greater than or equal to 80.
        """
        self.assertEqual(get_weather_advisory(-10, 90), "Low Temperature. Bundle Up!")

    def test_no_advisory(self):
        """
        Checks if the advisory is "No Specific Advisory" when the temperature is between 1 and 29 and the humidity is less than 80.
        """
        self.assertEqual(get_weather_advisory(20, 90), "No Specific Advisory")
    




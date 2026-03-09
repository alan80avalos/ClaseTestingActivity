# -*- coding: utf-8 -*-

"""
White-box unit testing part 3.
"""
import unittest
from unittest.mock import patch
from io import StringIO

from class_exercises import (
    BankAccount,
    BankingSystem,
    Product,
    ShoppingCart
)

class TestWhiteBoxBankAccount(unittest.TestCase):
    """
    Banking account unit tests.
    """
    def setUp(self):
        self.account = BankAccount(123, 1000)

    def test_initialize_bank_account(self):
        """
        Checks the BankAccount class initializes correctly.
        """
        self.assertEqual(self.account.account_number, 123)
        self.assertEqual(self.account.balance, 1000)


    @patch("builtins.print")
    def test_view_account(self, mock_print):
        """
        Checks the BankAccount can view account details.
        """
        self.account.view_account()
        mock_print.assert_called_with(
            f"The account {self.account.account_number} has a balance of {self.account.balance}"
        )

class TestWhiteBoxBankingSystem(unittest.TestCase):
    """
    """
    user = "user123"
    password = "pass123"

    def setUp(self):
        self.banking_system = BankingSystem()
    
    def test_initialize_banking_system(self):
        """
        Checks the BankingSystem class initializes correctly.
        """
        self.assertEqual(self.banking_system.users, {f"{self.user}": f"{self.password}"})
        self.assertEqual(self.banking_system.logged_in_users, set())
    
    @patch("builtins.print")
    def test_authenticate_success(self, mock_print):
        """
        """
        authenticated = self.banking_system.authenticate(self.user, self.password)
        self.assertTrue(authenticated)
        self.assertIn(self.user, self.banking_system.logged_in_users)#user este en el sistema
        mock_print.assert_called_with(f"User {self.user} authenticated successfully.")
    
    @patch("builtins.print")
    def test_authenticate_failed(self, mock_print):
        """
        """
        authenticated = self.banking_system.authenticate(self.user, "wrongPass")
        self.assertFalse(authenticated)
        self.assertNotIn(self.user, self.banking_system.logged_in_users)
        mock_print.assert_called_with("Authentication failed.")

    @patch("builtins.print")
    def test_authenticate_already_login(self, mock_print):
        """
        """
        self.banking_system.logged_in_users.add(self.user)
        authenticated = self.banking_system.authenticate(self.user, self.password)
        self.assertFalse(authenticated)
        mock_print.assert_called_with("User already logged in.")

    @patch("builtins.print")
    def test_transfer_money_not_authenticated(self, mock_print):
        """
        """
        receiver = "user2"
        amount = 100
        transaction_type = "regular"
        authenticated = self.banking_system.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with("Sender not authenticated.")
        self.assertFalse(authenticated)

    @patch("builtins.print")
    def test_transfer_money_regular(self, mock_print):
        """
        """
        receiver = "user2"
        amount = 100
        transaction_type = "regular"
        self.banking_system.logged_in_users.add(self.user)
        authenticated = self.banking_system.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with(f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully.")
        self.assertTrue(authenticated)
    
    @patch("builtins.print")
    def test_transfer_money_express(self, mock_print):
        """
        """
        receiver = "user2"
        amount = 100
        transaction_type = "express"
        self.banking_system.logged_in_users.add(self.user)
        authenticated = self.banking_system.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with(f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully.")
        self.assertTrue(authenticated)

    @patch("builtins.print")
    def test_transfer_money_scheduled(self, mock_print):
        """
        """
        receiver = "user2"
        amount = 100
        transaction_type = "scheduled"
        self.banking_system.logged_in_users.add(self.user)
        authenticated = self.banking_system.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with(f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {self.user} to {receiver} processed successfully.")
        self.assertTrue(authenticated)

    @patch("builtins.print")
    def test_transfer_money_invalid_transaction(self, mock_print):
        """
        """
        receiver = "user2"
        amount = 100
        transaction_type = "bien"
        self.banking_system.logged_in_users.add(self.user)
        authenticated = self.banking_system.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with("Invalid transaction type.")
        self.assertFalse(authenticated)

    @patch("builtins.print")
    def test_transfer_money_insufficient_founds(self, mock_print):
        """
        """
        receiver = "user2"
        amount = 1000
        transaction_type = "regular"
        self.banking_system.logged_in_users.add(self.user)
        authenticated = self.banking_system.transfer_money(self.user, receiver, amount, transaction_type)
        mock_print.assert_called_with("Insufficient funds.")
        self.assertFalse(authenticated)

class TestWhiteBoxProduct(unittest.TestCase):
    """
    """
    def setUp(self):
        self.product = Product("potato", 7)

    def test_initialize_product(self):
        """
        """
        self.assertEqual(self.product.name, "potato")
        self.assertEqual(self.product.price, 7)

    @patch("builtins.print")
    def test_display_product_succesful(self, mock_print):
        """
        """
        msg = self.product.view_product()
        mock_print.assert_called_with(f"The product {self.product.name} has a price of {self.product.price}")
        self.assertEqual(msg, f"The product {self.product.name} has a price of {self.product.price}")

class TestWhiteBoxShoppingCart(unittest.TestCase):
    """
    """
    product = "potato"

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        self.product = Product("potato", 7)

    def test_initialize_shopping_cart(self):
        """
        """
        self.assertEqual(self.shopping_cart.items, [])
  
    def test_add_product(self):
        """
        """
        self.shopping_cart.add_product(self.product, 1)
        self.assertEqual(self.shopping_cart.items[0]["product"], self.product)
        self.assertEqual(self.shopping_cart.items[0]["quantity"], 1)

    def test_add_product_existing(self):
        """
        """
        self.shopping_cart.add_product(self.product, 1)
        self.shopping_cart.add_product(self.product, 2)
        self.assertEqual(self.shopping_cart.items[0]["quantity"], 3)

    def test_remove_product(self):
        """
        """
        self.shopping_cart.add_product(self.product, 2)
        self.shopping_cart.remove_product(self.product, 1)
        self.assertEqual(self.shopping_cart.items[0]["quantity"], 1)

    def test_remove_product_complete(self):
        """
        """
        self.shopping_cart.add_product(self.product, 2)
        self.shopping_cart.remove_product(self.product, 2)
        self.assertEqual(len(self.shopping_cart.items), 0)    

    @patch("builtins.print")
    def test_view_cart(self, mock_print):
        """
        """
        self.shopping_cart.add_product(self.product, 1)
        self.shopping_cart.view_cart()
        mock_print.assert_called_with(f"1 x {self.product.name} - ${self.product.price * 1}")

    @patch("builtins.print")
    def test_checkout(self, mock_print):

        self.shopping_cart.add_product(self.product, 2)

        self.shopping_cart.checkout()

        total = self.product.price * 2

        mock_print.assert_any_call(f"Total: ${total}")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")









    
    

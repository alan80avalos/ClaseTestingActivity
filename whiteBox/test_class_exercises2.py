# -*- coding: utf-8 -*-

"""
White-box unit testing part 2.
"""
import unittest

from class_exercises import (
    VendingMachine,
    TrafficLight,
    UserAuthentication,
    DocumentEditingSystem,
    ElevatorSystem
)

class TestWhiteBoxVendigMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")

    def test_vending_machine_select_drink_success(self):
        """

        """
        self.vending_machine.state = "Dispensing"
        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Drink Dispensed. Thank you!")
    
    def test_vending_machine_select_drink_error(self):
        """

        """
        output = self.vending_machine.select_drink()

        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(output, "Invalid operation in current state.")

class TestWhiteBoxTrafficLight(unittest.TestCase):
    """
    """
    def setUp(self):
        self.traffic_light = TrafficLight() 
        self.assertEqual(self.traffic_light.state, "Red")

    def test_change_state_green(self):
        """
        """
        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Green")
    
    def test_change_state_yellow(self):
        """
        """
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Yellow")

    def test_change_state_red(self):
        """
        """
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()

        self.assertEqual(self.traffic_light.state, "Red")
        #self.assertEqual(output, "")

class TestWhiteBoxUserAuthentication(unittest.TestCase):
    """
    """
    def setUp(self):
        self.user_authentication = UserAuthentication()
        self.assertEqual(self.user_authentication.state, "Logged Out")

    def test_login_success(self):
        """
        """
        output = self.user_authentication.login()

        self.assertEqual(self.user_authentication.state, "Logged In")
        self.assertEqual(output, "Login successful")

    def test_login_error(self):
        """
        """
        self.user_authentication.state = "Logged In"
        output = self.user_authentication.login()

        self.assertEqual(self.user_authentication.state, "Logged In")
        self.assertEqual(output, "Invalid operation in current state")
    ####
    def test_logout_success(self):
        """
        """
        self.user_authentication.state = "Logged In"
        output = self.user_authentication.logout()

        self.assertEqual(self.user_authentication.state, "Logged Out")
        self.assertEqual(output, "Logout successful")
    
    def test_logout_error(self):
        """
        """
        output = self.user_authentication.logout()

        self.assertEqual(self.user_authentication.state, "Logged Out")
        self.assertEqual(output, "Invalid operation in current state")
    
class TestWhiteBoxDocumentEditingSystem(unittest.TestCase):
    """
    """
    def setUp(self):
        self.document_editing_system = DocumentEditingSystem()
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_save_document_successfully(self):
        """
        """
        output = self.document_editing_system.save_document()
        
        self.assertEqual(self.document_editing_system.state, "Saved")
        self.assertEqual(output, "Document saved successfully")

    def test_save_document_invalid(self):
        """
        """
        self.document_editing_system.state = "Saved"
        output = self.document_editing_system.save_document()
        
        self.assertEqual(self.document_editing_system.state, "Saved")
        self.assertEqual(output, "Invalid operation in current state")

    def test_edit_document_resumed(self):
        """
        """
        self.document_editing_system.state = "Saved"
        output = self.document_editing_system.edit_document()
        
        self.assertEqual(self.document_editing_system.state, "Editing")
        self.assertEqual(output, "Editing resumed")

    def test_edit_document_invalid(self):
        """
        """
        output = self.document_editing_system.edit_document()
        
        self.assertEqual(self.document_editing_system.state, "Editing")
        self.assertEqual(output, "Invalid operation in current state")

class TestWhiteBoxElevatorSystem(unittest.TestCase):
    """
    """
    def setUp(self):
        self.elevator_system = ElevatorSystem()
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_move_up_succesful(self):
        """
        """
        output = self.elevator_system.move_up()

        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(output, "Elevator moving up")

    def test_move_up_invalid(self):
        """
        """
        self.elevator_system.state = "Moving Up"
        output = self.elevator_system.move_up()

        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_move_down_succesful(self):
        """
        """
        output = self.elevator_system.move_down()

        self.assertEqual(self.elevator_system.state, "Moving Down")
        self.assertEqual(output, "Elevator moving down")

    def test_move_down_invalid(self):
        """
        """
        self.elevator_system.state = "Moving Up"
        output = self.elevator_system.move_down()

        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(output, "Invalid operation in current state")

    def test_stop_up_succesful(self):
        """
        """
        self.elevator_system.state = "Moving Up"
        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_stop_down_succesful(self):
        """
        """
        self.elevator_system.state = "Moving Down"
        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Elevator stopped")

    def test_stop_invalid(self):
        """
        """
        output = self.elevator_system.stop()

        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(output, "Invalid operation in current state")



    


# -*- coding: utf-8 -*-

"""
White-box unit testing part 3.
"""
import unittest
import subprocess
from unittest.mock import patch, MagicMock, mock_open
from io import StringIO

from mockup_exercises import (
    fetch_data_from_api,
    read_data_from_file,
    execute_command,
    perform_action_based_on_time
)

class TestMockup(unittest.TestCase):

    @patch("requests.get")
    def test_fetch_data(self, mock_get):
        """
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"name": "Alan"}
        mock_get.return_value = mock_response

        result = fetch_data_from_api("http://alan-test-url")

        self.assertEqual(result, {"name": "Alan"})
        mock_get.assert_called_once()

    @patch("builtins.open", new_callable=mock_open, read_data="hola mundo")
    def test_read_file(self, mock_file):
        """
        """
        result = read_data_from_file("test.txt")

        self.assertEqual(result, "hola mundo")
        mock_file.assert_called_once()

    @patch("builtins.open")
    def test_file_not_found(self, mock_open):
        """
        """
        mock_open.side_effect = FileNotFoundError#hace que se lance el error 

        with self.assertRaises(FileNotFoundError):
            read_data_from_file("fake.txt")

    @patch("subprocess.run")
    def test_execute_command(self, mock_run):
        """
        """
        mock_process = MagicMock()
        mock_process.stdout = "test"
        mock_run.return_value = mock_process
        result = execute_command(["ls"])

        self.assertEqual(result, "test")
        mock_run.assert_called_once()

    @patch("subprocess.run")
    def test_execute_command_error(self, mock_run):
        """
        """
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["ls"])

    @patch("time.time")
    def test_action_A(self, mock_time):
        mock_time.return_value = 5

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")
    
    @patch("time.time")
    def test_action_B(self, mock_time):
        mock_time.return_value = 20

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")

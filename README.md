# ClaseTestingActivity

# Run the testcases python
python -m unittest discover

# Run with coverage
py -m pip install coverage
py -m coverage run -m unittest test_class_exercises.py || py -m coverage run -m unittest discover
py -m coverage html
 
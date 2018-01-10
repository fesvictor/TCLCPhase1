# How to run test?
First, make sure you have installed `pytest`
```
pip install -U pytest
```

Second, run `pytest <file_name> -s` to test a file.
For example : 
```python
# run test on the whole ./test/ directory
pytest ./tests/ -s 

# run test on a test_abc.py
pytest ./test/ -s
```

### But what is the `-s` for?
The `-s` options is to allow you to see the printed results when you run those code, if not `pytest` will surpess any printed result by default. Look [HERE](https://stackoverflow.com/questions/24617397/how-to-print-to-console-in-py-test) for more info.

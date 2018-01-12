## How to run `analysis.py`? 
First, go to the directory which is one level above `TCLCPhase1`  
 *Assume that you are in directory of TCLCPhase1*.
```
cd ..
```
Then, run the following command:
```
py -m TCLCPhase1.AnalysisLib.analysis.py
```
Of course, the same principle applies if you want to `py` other files.


## How to run unit tests?
There are 3 ways to do it:
```
# 1. Run all test in this directory
pytest
```
```
# 2. Run all test in specified directory
pytest <dir_name>
```
```
# 3. Run test of specific file
pytest <file_name>
```

## How to import module from another file in different directory?
In this project, TCLCPhase1 is the top level package, so import should looks like this :
```python
from TCLCPhase1.AnalysisLib.analysis import analysis
```
This will work no matter which directory you are in, as long as the directory is a subdirectory of `TCLCPhase1`.

### IMPORTANT NOTE
Whenever you create a new directory, please create an empty file named `__init__.py`. 
Without this file, you will have import problems.  
For example, let say I want to create a directory named `banana`.
```
mkdir banana
cd banana
touch __init__.py
```
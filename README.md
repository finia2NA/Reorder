# Reorder
Takes a list of entries from stdin, displays a window to select + reorder them, then outputs the result to stdout
![Screenshot](https://i.imgur.com/e42dfVL.png)

## Installation
Just run ```pipenv install```

You could also run ```pip install pyqt5``` if you don't feel like using pipenv

## Usage
Pipe some line seperated list into the program (eg ls -1), reorder and select the items, click confirm and the result gets piped into stdout.

Example:
```ls -1 | python reorder.py```
(provided you are in the environment shell already)

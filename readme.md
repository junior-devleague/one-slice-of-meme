---
author:
- gitten
title: 'One Slice of Meme, Please.'
type: Activity
---

Summary
=======

Activity for constructing and processing Python Lists

Objective
=========

A wild meme was found! Tame the meme by putting it back together! You
will rebuild the meme by placing the pieces in the proper order within a
list structure. Use list operators and the \`capture()\` function from
the provided library.

Prerequisites
=============

-   Basic usage of Python REPL
-   Basic usage of Python standard libs `os` and `os.path`

Requirements
============

-   Shell terminal or Python IDE
-   import the provided image building lib `wild_meme`
-   An appetite for memes

Desired Outcomes
================

-   build an intuition about structuring data as lists
-   basic understanding of destructuring and building lists
-   Increase comfort level of Utilizing REPL for development
-   Preparation for Conway's Game of Life project

Tasks
=====

Preparing the activity
----------------------

### From the terminal

1.  Clone the repository, change to project directory

``` {.bash}
git clone https://github.com/junior-devleague/one-slice-of-meme.git
cd one-slice-of-meme
```

2.  Create a virtual enviornment and install dependencies

``` {.bash}
virtualenv -p python3 env/
env/bin/pip install -r requirements.txt
```

3.  start your REPL and import provided lib
    -   From terminal, enter `env/bin/python`
    -   In your newly started REPL, enter `from assets.wild_meme
                  import LeftBeef`
        -   NOTE: don't forget about `os` and `os.path`!

Catching a Meme
---------------

-   You can observe the wild meme by calling `LeftBeef.observe_meme()`
-   Use `os~/~os.path`, list operators and expressions to build and
    manipulate lists
-   Your list should look something like `['<meme directory
          name>/<meme piece file name>']`
-   To build your meme use `LeftBeef.capture(path_to_piece_list)`
-   Any way you slice it... a meme is a meme?

Stretchy stretch goal
---------------------

-   Make your own wild meme!

Resources
---------

### Functions that might be useful

-   os.listdir()
    -   [docs](https://docs.python.org/3/library/os.html#os.listdir)
-   os.path.join()
    -   [docs](https://docs.python.org/3.5/library/os.path.html#os.path.join)

### Expressions that might be useful

1.  lambda expressions

    -   An example

    ``` {.python}
    lambda arg: some_function(some_arg, arg, another_arg)
    ```

    -   Another example

    ``` {.python}
    lambda arg0, arg1: function(arg0, arg1, arrrrg_pirate)
    ```

2.  list comprehension

    ``` {.python}
    [some_variable for some_variable in list of variables]
    ```

### List operations that might be useful

-   `len(somelist)`
-   `somelist[]`
-   `somelist[start:stop]`
-   `somelist[start:stop:step]`
-   `somelist.pop(index)`
-   `somelist.reverse()`
-   list every other list item `somelist[::2]`
-   list every other, starting with 'index' `somelist[index::2]`
-   create a copy `somelist[]`
-   additional info [here](http://effbot.org/zone/python-list.htm)

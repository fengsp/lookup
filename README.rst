lookup
======

::

      ___________________   ___________________
  .-/|  01   ~~**~~      \ /      ~~**~~   02  |\-.
  ||||                    :                    ||||
  ||||   $ lookup         :   Difficult        ||||
  ||||                    :   circumstances    ||||
  ||||                    :   serve as a       ||||
  ||||   Nothing seek,    :   textbook of      ||||
  ||||   nothing find.    :   life for people. ||||
  ||||                    :                    ||||
  ||||                    :           @fengsp  ||||
  ||||___________________ : ___________________||||
  ||/====================\:/====================\||
  `---------------------~___~--------------------''

english-chinese dictionary via the command line
-----------------------------------------------

Do you read english documentation a lot?  Do you find yourself constantly
opening a webpage or switching to dictionary application for understanding
an english word?

Suppose you want to know what does one word mean.  Why open your browser and
search when you can simply stay in the console and ask `lookup`::
    
    $ lookup
    usage: lookup [WORD]

    $ lookup hello
    iCIBA: hello
    ------------
    你好； 问好； 喂； 呼叫

    $ lookup "execuse me"
    iCIBA: execuse me
    -----------------
    借口； 原谅； 挡箭牌； 理由

    $ lookup 计算机
    iCIBA: 计算机
    -------------
    computer； computers； computer science； calculating machine

Installation
------------

::

    $ pip install lookup
    
    # Use Mac OS X brew
    $ brew install https://raw.github.com/fengsp/lookup/master/lookup.rb

    # Download the zipball and install it
    $ wget http://github.com/fengsp/lookup/zipball/master#egg=lookup
    $ python setup.py install

Better
------

If you feel anything wrong, feedbacks or pull requests are welcomed.

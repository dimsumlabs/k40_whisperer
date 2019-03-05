# Control software for the stock K40 Laser controller

This repository contains a copy of the
[upstream source](http://home.scorchworks.com/K40whisperer/k40whisperer.html)
with each version checked into version control.

It has had a small number of python unit tests added to the low-level hardware
and EGV output routines - intending to be the starting point for making
changes to improve the code, however the upstream did not accept these
patches.

Anyone interested in a properly decoupled library that supports the K40
should probably use this repository as a reference only and consider using
a different implementation - like [K40Nano](https://github.com/K40Nano/K40Nano)

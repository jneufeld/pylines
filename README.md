pylines
=======
Like [clines](https://github.com/jneufeld/clines) does for C/C++ files, pylines
looks at Python source files and spits out vaguely interesting stats, like the
number of actual code lines, comment lines, and so on.

Usage
-----
What pylines looks like running against its own code:

```
$ pylines.py *.py
File                 Code %      Comment %      Blank %      Total
DebugLogging.py      15   26.3   31      54.4   11    19.3   57
FileAnalyzer.py      74   45.4   58      35.6   31    19.0   163
FileStatistics.py    29   46.0   27      42.9   7     11.1   63
pylines.py           10   37.0   9       33.3   8     29.6   27
StatisticsPrinter.py 84   50.9   48      29.1   33    20.0   165
```

TODO
----
Percentages are calculated during analysis, but aren't printed. Error handling 
isn't robust right now. Tests, smarter printing (files that didn't analyze or
couldn't be opened, e.g.), and percentages are next.

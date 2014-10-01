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
File                 Total Code Comment Blank
FileAnalyzer.py      144   57   58      29
FileStatistics.py    52    20   25      7
pylines.py           27    10   9       8
StatisticsPrinter.py 113   52   38      23
```

TODO
----
Percentages are calculated during analysis, but aren't printed. Error handling 
isn't robust right now. Tests, smarter printing (files that didn't analyze or
couldn't be opened, e.g.), and percentages are next.

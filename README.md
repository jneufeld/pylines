pylines
=======
Like [clines](https://github.com/jneufeld/clines) does for C/C++ files, pylines
looks at Python source files and spits out vaguely interesting stats, like the
number of actual code lines, comment lines, and so on.

Usage
-----
What pylines looks like running against its own code, on one file:

```
$ pylines.py pylines.py
File       Code %      Comment %      Blank %      Total
pylines.py 10   37.0   9       33.3   8     29.6   27
```

And running against multiple files:

```
$ pylines.py *.py
File                 Code %      Comment %      Blank %      Total
FileAnalyzer.py      74   45.4   58      35.6   31    19.0   163
FileStatistics.py    30   46.2   28      43.1   7     10.8   65
pylines.py           10   37.0   9       33.3   8     29.6   27
StatisticsPrinter.py 112  53.8   55      26.4   41    19.7   208
Total                226  48.8   150     32.4   87    18.8   463
```

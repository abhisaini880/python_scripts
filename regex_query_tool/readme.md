# Regular Expressions

> A Regular expression is a sequence of characters taht define a search pattern.

_Example:_

regex = ^[0-9]$

above regular expression matches the pattern with a digit 0 to 9.

### Python comes with a library to deal with regular expressions
```
import re
```
Two function that were used in regex query tool to make it possible for finding and replacing the pattern in sequence of characters passed are:

>findall - used to find the pattern in a sequence and returns the matched sequence otherwise returns a empty list

>sub - used to find the pattern and then replace it with specified sequence.

**For finding** 
```
import re

pattern = r'[0-9]+'
sequence = "abhisaini880"
print(re.findall(pattern, sequence))

output --> "880"
```
**For Replacing**
```
import re
pattern = r'[0-9]+'
sequence = "abhisaini880"
repl = "990"
print(re.sub(pattern, repl, sequence))
```

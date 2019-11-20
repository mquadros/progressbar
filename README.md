# progressbar
It's a unicode progress bar! Who doesn't love a unicode progressbar?

Example code:


import time

from progressbar import *

bar = Bar(100)

for x in range(100):

    bar.update(x)

    time.sleep(.02)
	
bar.update(100)



Output:

[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%

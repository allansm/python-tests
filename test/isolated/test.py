import dependency

from util import showOptions as print_r
from fileHandle import ls
from fileHandle import selfLocation as where
from util import do
from custom import root
from ask import * 

print_r(ls(".","*"))

root = do(root,"../../gui",where(__file__))
root.size(200,150)

ask = Ask("name:","",root)

ask.show()

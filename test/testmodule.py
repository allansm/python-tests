import sys
sys.path.append("../functions")

from util import *


text = "a\nb\nc\nd\ne\nf\n";
print("original:\n"+text);
print("with func:"+removeBreakLine(text));

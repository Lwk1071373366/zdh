import os
import sys

BaseDir = os.path.dirname(os.path.dirname(__file__))   #路径上翻两层
sys.path.append(BaseDir)

from core import core

if __name__ == '__main__':
    core.entry_point()



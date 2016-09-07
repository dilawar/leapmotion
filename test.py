"""test.py: 

Testing leap motion thingy.

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2016, Dilawar Singh"
__credits__          = ["NCBS Bangalore"]
__license__          = "GNU GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import matplotlib.pyplot as plt
import numpy as np

sys.path.append( '/opt/LeapSDK/lib/' )
sys.path.append( '/opt/LeapSDK/lib/x64/') 

import Leap

def main( ):
    print( 'Imported leap' )

if __name__ == '__main__':
    main()

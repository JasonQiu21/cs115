# I pledge my honor that I have abided by the Stevens Honor System.
#
#
# Jason Qiu
# 2021-10-28

import sys
import importlib

Fib ="""
# Input: n
# Assume: n >= 0
# Output: first n numbers of Fibonacci Sequence
#

# register usage: r1 for input, r2 through r5 for computation

00 read r1          # Get n
01 setn r2 0        # init r2,r3,r4
02 setn r3 1        # ^
03 setn r4 1        # ^
04 jeqzn r1 11      # done if r1 is 0
05 write r2         # print r2
06 copy r4 r2       # r4 gets set to r2
07 copy r2 r3       # r2 gets set to r3
08 add r3 r2 r4     # r3 = r2 + r4
09 addn r1 -1       # r1 -= 1
10 jumpn 04         # repeat
11 halt

"""

# Set this variable to whichever program you want to execute
# when this file is loaded.
RunThis = Fib

# Choose whether to use debug mode; uncomment one of the following lines.
# Mode = ['-n'] # not debug mode, 
Mode = ['-d'] # debug mode
#Mode = []     # prompt for whether to enter debug mode


# When you press F5 in IDLE, the following code will
# load the assembler and simulator, then run them.
# You can interrupt with Ctrl-C; then re-start Python.

if __name__ == "__main__" : 
    import hmmmAssembler ; importlib.reload(hmmmAssembler)
    import hmmmSimulator ; importlib.reload(hmmmSimulator)
    hmmmAssembler.main(RunThis) # assemble input into machine code file out.b
    hmmmSimulator.main(Mode)    # run the machine code in out.b

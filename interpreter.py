#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# This is a interpreter for the very simple language ";#"
# 
# ;# has only two instruction:
# - ";" Increments the accumulator
# - "#" Takes modulo 127 from the accumulator and print the ASCII character out
# 
# # Usage:
# ./interpreter.py <script>
import sys

def interpret(script):
  """Outputs the result from the ;# script"""
  accumulator = 0
  output = ""
  for c in script:
    if c == ";":
      accumulator += 1
    elif c == "#":
      output += chr(accumulator % 127)
      accumulator = 0

  print(output)

if __name__ == "__main__":
  interpret(sys.argv[1])
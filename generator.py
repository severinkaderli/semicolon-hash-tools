#!/usr/bin/env python3
# Author: Severin Kaderli <severin.kaderli@gmail.com>
#
# This script creates a ;#-Script which outputs a wanted text.
# 
# # Usage:
# ./generator.py <string>
import sys

def generate(text):
	"""Generates a ;#-Script which outputs the given text"""
	script = ""
	for character in text:
		script += ord(character) * ";"
		script += "#"
	print(script)

if __name__ == "__main__":
  generate(sys.argv[1])
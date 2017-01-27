#!/usr/bin/env python3
""" Retrieve and print words from a URL

	Usage: python pyfund.py <url>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
	""" Fetch a list of words from URL 

	Args:
		url: URL in UTF format

	Returns:
		A list of srtings 

	"""
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words

def print_items(items):
	""" Print items of an iterable one per line

	Args: 
		items: iterable object
	"""
	for item in items:
		print(item)


def main(url):	
	""" Print each word from a URL 

	Args:
		url: the URL of a text document
	"""
	words = fetch_words(url)
	print_items(words)

if __name__ == '__main__':
	main(sys.argv[1])
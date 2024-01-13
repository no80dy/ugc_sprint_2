"""This is a testing module"""

import logging


def get_message(message: str) -> str:
	"""This is the function that..."""
	return message


if __name__ == '__main__':
	result = get_message('Hello world')
	logging.info(f'RESULT: {result}')

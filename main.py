"""Test the functionality of the module."""

import logging


def get_message(message: str) -> str:
	"""
	Returns message in string format.

    :param message: Сообщение.
    :type message: str
    :return: Сообщение.
    :rtype: str
	"""
	return message


if __name__ == '__main__':
	result = get_message('Hello world')
	logging.info(f'RESULT: {result}')

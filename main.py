"""Test the functionality of the module."""
import logging


def get_message(message: str) -> str:
    """
    This function returns the message.

    parameter:
        - message (str): The text of message.

    Returns:
        - str: The string message.
    """
    return message


if __name__ == '__main__':
    message_from_stdout = get_message('Hello world')
    logging.info(f'RESULT: {message_from_stdout}')

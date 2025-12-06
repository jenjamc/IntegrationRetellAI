from enum import StrEnum


class ErrorMessages(StrEnum):
    USER_DOES_NOT_EXIST = 'User does not exist'
    INVALID_ACCESS_TOKEN = 'Invalid access token'
    INVALID_PASSWORD = 'Invalid email or password'

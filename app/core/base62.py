import string


class Consts:
    BASE = 62
    DIGITS = list(string.digits + string.ascii_lowercase + string.ascii_uppercase)


class Base62:
    @staticmethod
    def encode_base_62(number) -> str:
        base62_result = ''
        while number > 0:
            digit_index = number % Consts.BASE
            number = number // Consts.BASE
            base62_result += Consts.DIGITS[digit_index]
        return base62_result[::-1]

    @staticmethod
    def decode_base_62(number) -> int:
        for i in number:
            number = number * Consts.BASE + Consts.DIGITS.index(i)
        return number

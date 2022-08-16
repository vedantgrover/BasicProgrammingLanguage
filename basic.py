import Lexer

DIGITS = '0123456789'


def run(fn, text):
    lexer = Lexer.Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error

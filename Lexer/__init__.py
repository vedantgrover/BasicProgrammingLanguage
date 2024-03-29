import Errors.IllegalCharError
import Position
import Tokens
import basic


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position.Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in basic.DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tokens.Token(Tokens.TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Tokens.Token(Tokens.TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Tokens.Token(Tokens.TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Tokens.Token(Tokens.TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Tokens.Token(Tokens.TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Tokens.Token(Tokens.TT_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], Errors.IllegalCharError.IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char in basic.DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Tokens.Token(Tokens.TT_INT, int(num_str))
        else:
            return Tokens.Token(Tokens.TT_FLOAT, float(num_str))

from .lexer import lex
from .parser import parse

def from_string(string):
    tokens = lex(string)
    return parse(tokens)[0]

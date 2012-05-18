import ply.lex as lex
import ply.yacc as yacc

tokens = (
  'COMMA',
  'IDENTIFIER',
  'LPAREN',
  'NUMBER',
  'RPAREN',
)

def t_NUMBER(t):
  r'-?[0-9]+(\.[0-9]*)?'
  t.value = float(t.value)
  return t

t_COMMA = r','
t_IDENTIFIER = r'[A-Za-z][A-Za-z_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_error(t):
  print "JavaScript Lexer: Illegal character " + t.value[0]
  t.lexer.skip(1)

def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("call", p[1], p[3])
    
def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])
    
def p_optargs(p):
    'optargs : args'
    p[0] = p[1]
    
def p_optargs_empty(p):
    'optargs : '
    p[0] = []

def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_last(p):
    'args : exp'
    p[0] = [p[1]]

def p_error(p):
    print "Syntax error in input!"

lexer = lex.lex()
parser = yacc.yacc()
print parser.parse("myfun(11,12)",lexer=lexer)
#--> ('call', 'myfun', [('number', 11.0), ('number', 12.0)])

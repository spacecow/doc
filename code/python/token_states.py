states = [('htmlcomment','exclusive')]

def t_htmlcomment(token):
  r'<!--'
  token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
  r'-->'
  token.lexer.lineno += token.value.count('\n')
  token.lexer.begin('INITIAL')

def t_htmlcomment_error(token):
  "Gathers up all of the text into one big value so one can count the new lines later."
  token.lexer.skip(1) 

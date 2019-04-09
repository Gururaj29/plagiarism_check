# import utils
from pycparser import c_parser, c_ast


with open('../dataset/sample_one.c','r') as f:
	text = f.readlines()
	
text = " ".join(e for e in text)

parser = c_parser.CParser()
ast = parser.parse(text, filename='<none>')

# print(ast)
a = []
def explore(ast, a):
	a.append(str(type(ast)))
	for i in ast:
		explore(i, a)


explore(ast, a)

for i in a:
	print(i)

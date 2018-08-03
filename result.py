import nltk
import PyPDF2
from collections import Counter
import pandas as pd


pdf = "JavaBasics-notes.pdf"
pdfReader = PyPDF2.PdfFileReader(open(pdf, 'rb'))

pages = pdfReader.getNumPages()

st = ""
for page in range(0,pages):
	p = pdfReader.getPage(page)
	st = st + (p.extractText())

st = st.lower()
tokens = nltk.word_tokenize(st)
counts = Counter(tokens)

pp = ["abstract","assert","boolean","break",
"byte",	"case",	"catch",	"char",
"class"	,"const"	,"continue",	"default",
"do",	"double"	,"else",	"enum",
"extends",	"final",	"finally",	"float",
"for",	"goto"	,"if",	"implements",
"import"	,"instanceof"	,"int",	"interface",
"long",	"native",	"new",	"package",
"private",	"protected",	"public",	"return",
"short",	"static",	"strictfp",	"super",
"switch",	"synchronized",	"this",	"throw",
"throws",	"transient"	,"try",	"void",
"volatile",	"while",	 "true",	 "false",
"null","inheritance", "abstraction","encapsulation","multithreading"]

results = dict()
for word in pp:
	results[word] = counts[word]
	


df = pd.DataFrame(data=results , index=[0])
df = (df.T)


df.to_excel('output.xlsx')

			

from flask import render_template
from flask import request
from flask import Blueprint
from pw_analysis import pw_analysis

password = Blueprint('password', __name__)


@password.route("/password/", methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('password/index.html')
	else:
		text = request.form['text']
		row = list(range(13))
		row[0] = text
		row[1] = 'a'
		row[2] = str(len(text))
		row[3] = str(NumberOfDigits(text))
		row[4] = str(NumberOfAlphas(text))
		row[5] = str(NumberOfLowers(text))
		row[6] = str(NumberOfUppers(text))
		row[7] = str(NumberOfSymbols(text))
		row[8] = bool(IsCharactersOnly(text))
		row[9] = bool(IsDigitsOnly(text))
		row[10] = str(IsRepeatCharacters(text))
		row[11] = str(IsSequentialCharacters(text))
		row[12] = str(RatioOfVowels(text))

		X = row[2:]
		result = pw_analysis(X)
		if result[0] == 0:
			answer = "Weak! 5분 만에 깨지는 패스워드입니다!"
		else:
			answer = "Strong! 단단한 패스워드! 발 뻗고 자도 되겠네요"
		return render_template('password/index.html', text=text, answer=answer)


def NumberOfDigits(input):
	n = 0
	for c in input:
		if c.isdigit():
			n += 1
	return n


def NumberOfAlphas(input):
	n = 0
	for c in input:
		if c.isalpha():
			n += 1
	return n


def NumberOfLowers(input):
	n = 0
	for c in input:
		if c.islower():
			n += 1
	return n


def NumberOfUppers(input):
	n = 0
	for c in input:
		if c.isupper():
			n += 1
	return n


def NumberOfSymbols(input):
	def issymbol(c):
		from itertools import chain
		return ord(c) in chain(range(33, 48), range(58, 65), range(91, 97), range(123, 127))
	n = 0
	for c in input:
		if issymbol(c):
			n += 1
	return n


def IsCharactersOnly(input):
	return len(input) == NumberOfAlphas(input)


def IsDigitsOnly(input):
	return len(input) == NumberOfDigits(input)


def IsRepeatCharacters(input):
	from itertools import groupby
	n = 0
	for l in [[k,len(list(g))] for k, g in groupby(input)]:
		if l[1] >= 4:
			n += 1
	return n


def IsSequentialCharacters(input):
	def forward(input):
		i = 0
		if len(input) == 0:
			return 0
		repeat_str = input[0]
		sq_list = []
		while i < len(input) - 1:
			if ord(input[i+1]) - ord(input[i]) == 1 :
				repeat_str += input[i+1]
			else:
				if len(repeat_str) >= 3:
					sq_list.append(repeat_str)
				repeat_str = input[i+1]
			i += 1
		if len(repeat_str) >= 3:
			sq_list.append(repeat_str)
		return len(sq_list)

	def backward(input):
		i = 0
		if len(input) == 0:
			return 0
		repeat_str = input[0]
		sq_list = []
		while i < len(input) - 1:
			if ord(input[i+1]) - ord(input[i]) == -1 :
				repeat_str += input[i+1]
			else:
				if len(repeat_str) >= 3:
					sq_list.append(repeat_str)
				repeat_str = input[i+1]
			i += 1
		if len(repeat_str) >= 3:
			sq_list.append(repeat_str)
		return len(sq_list)
	return forward(input)+ backward(input)


def RatioOfVowels(input):
	def isVowel(c):
		return ord(str.upper(c)) in (65, 69, 73, 79, 85, 89)
	n = 0
	for c in input:
		if isVowel(c):
			n += 1
	if NumberOfAlphas(input) != 0:
		return n / NumberOfAlphas(input)
	else :
		return 0.0

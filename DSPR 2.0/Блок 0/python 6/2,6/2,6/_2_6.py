#Необходимо написать функцию get_most_frequent_word(text), которая возвращает самое часто встречающееся
# слово в тексте text. Не забудьте очистить тест от знаков пунктуации и привести текст к единому регистру
#  (слова в верхнем и нижнем регистре считаются одним и тем же словом).
def get_most_frequent_word(text):
	punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
	red_txt = text
	for i in punctuation_list:
		red_txt = red_txt.replace(i, '')
	red_txt = red_txt.lower()
	red_txt = red_txt.split()
	mfword = None
	col = 0
	for a in red_txt:
		if red_txt.count(a) > col:
			mfword = a
			col = red_txt.count(a)
	return mfword

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

print(get_most_frequent_word(text_example))

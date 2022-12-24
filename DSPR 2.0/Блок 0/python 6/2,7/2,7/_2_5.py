#�������� ������� get_unique_words(text), ������� ����������� �� ������ ���������� � ������ � ����������
# ������������� ������ (����� ����������� �� ��������) �� ���������� (���������������) ����. ������, ���
#  �����, ���������� � ������ ��������� ��������� ����� � ��� �� ������.
def get_unique_words(text):
	punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
	red_txt = text
	for i in punctuation_list:
		red_txt = red_txt.replace(i, '')
	red_txt = red_txt.lower()
	red_txt = red_txt.split()
	set_txt = list(set(red_txt))
	return sorted(set_txt)
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
print(get_unique_words(text_example))

# Словари Dictionaryes
#
# К каждому элементу словоря можно обратиться по его индефикатору
# Синтаксис:
#	<Имя Словаря> = {
#		<Первый ключ>: <Первый значений>,
#		<Второй ключ>: <Второй элемент>,
#		<Третий ключ>: <Второй значений>
#	}

phrases = {
	"Данил0": "Ну что там с деньгами?",
	"Алина0": "Какими деньгами?",
	"Данил1": "Ну которые я вложил.",
	"Алина1": "Куда вложил?",
	"Данил2": "В капил.",
	"Алина2": "В какой капитал?",
	"Данил3": "В капитал прожиточного минимума",
	"Алина3": "Угу... А деньги то где?"
}

danya = "Данил"
alina = "Алина"
says = "говорит -"
for n in "0", "1", "2", "3":
	print(danya, says, phrases[danya + n])
	print(alina, says, phrases[alina + n])
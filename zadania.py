
# 1. Napisz słownik zawierający twoje imię, nazwisko, wiek, miasto, szkołe. Korzystając z for dla v i k wyświetl wszystkie k i v (key value).
 
person = {
    'imie' : 'Krzysztof',
    'nazwisko' : 'Auch',
    'wiek' : 14,
    'miasto' : 'Warszawa',
    'szkola' : 'Wyspiański'
}
 
def display():
    print('-'*30)
    for k, v in person.items():
        print(f"{k}: {v}")
    print('-'*30)
 
display()

# 2.Napisz funkcję pozwalającą zmienić wszystkie dane w twoim słowniku (aby przerwać edycje wpisz stop).
 
def edit():
    while True:
        print('Wybierz co chcesz zmienić?')
        print("{0} | update {1} | {2} | {3} | {4} | {5}".format(' stop - stop ','imie - 1','nazwisko - 2', 'wiek - 3', 'miasto - 4', 'szkola - 5'))
        inp = input()
        if inp == 'stop':
            print('task ended')
            break

        elif inp == '1':
            inp_2 = input('imie ?')
            person.update({'imie': inp_2})

        elif inp == '2':
            inp_2 = input('nazwisko ?')
            person.update({'nazwisko': inp_2})

        elif inp == '3':
            inp_2 = int(input('wiek ?'))
            person.update({'wiek': inp_2})

        elif inp == '4':
            inp_2 = input('miasto ?')
            person.update({'miasto': inp_2})

        elif inp == '5':
            inp_2 = input('szkola ?')
            person.update({'szkola': inp_2})

        else:
            print("wrong number")
    display()
print(edit())


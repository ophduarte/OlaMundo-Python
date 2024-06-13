text = input('Digite alguma coisa: ')
print('As caraceristicas do que foi digitado são: \b')
print('Tipo {}, Numérico: {}, Alfabetico {}, Alfanumérico {}. '.format((type(text)), text.isnumeric(), text.isalpha(), text.isalnum(),))

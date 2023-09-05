"""Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras Maiusculas,
# O nome com todas Minusculas
# Quantas letras ao todo( sem considerar espaços)
# quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo: ')).strip()  # Strip 'elimina os espaços'
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))  # Upper 'Maiuscula'
print('Seu nome em minúscula é {}'.format(nome.lower()))  # Lower 'Minuscula'
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print(' o seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

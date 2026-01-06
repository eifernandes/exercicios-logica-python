"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
print('Insira as notas para descobrir sua média')

nt1 = float(input('Primeira nota: '))
nt2 = float(input('Segunda nota: '))
nt3 = float(input('Terceira nota: '))
nt4 = float(input('Quarta nota: '))
media = (nt1+nt2+nt3+nt4) / 4

print(f'Somando todas as notas, sua média é... {media:.2f}')

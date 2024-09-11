#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='QCrypt decoder 😈', add_help=True)
parser.add_argument('-e', '--encoded', required='true', help='Encoded string to decode')
pars = parser.parse_args()

entrada = pars.encoded

valores_decimais = []
i = 0

while i < len(entrada):
    if entrada[i].isdigit():
        valor_decimal = int(entrada[i])
        i += 1

        while i < len(entrada) and entrada[i].isdigit():
            valor_decimal = valor_decimal * 10 + int(entrada[i])
            i += 1

        valores_decimais.append(valor_decimal)
    else:
        i += 1

texto_convertido = ""

for valor in valores_decimais:
    caractere = chr(valor)
    texto_convertido += caractere

entrada = texto_convertido[:-16]

print(f" \n[+] Decoded string: {texto_convertido}")

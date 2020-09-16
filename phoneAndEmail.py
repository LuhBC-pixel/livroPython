# ! python3
# phoneAndEmail.py - Encontra números de telefone e endereços de email no clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''( 
    (\d{3}|\(\d{3}\))?                # código de área 
    (\s|-|\.)?                        # separador 
    (\d{3})                           # primeiros 3 dígitos 
    (\s|-|\.)                         # separador 
    (\d{4})                           # últimos 4 dígitos 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extensão
    )''', re.VERBOSE)

# Cria regex para email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # nome do usuário v     
    @                      # símbolo @      
    [a-zA-Z0-9.-]+         # nome do domínio 
    (\.[a-zA-Z]{2,4})      # ponto seguido de outros caracteres 
    )''', re.VERBOSE)


# Encontra as correspondências no texto do clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copia os resultados para o clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
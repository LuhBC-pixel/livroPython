#! python3
# pw.py - Um programa para repositório de senhas que não é seguro

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHfhTxFtjVB6', 'blog': 'sdfAsFDSfnSDFFSFODJfoals15dasFE', 'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # o primeiro argumento da linha de comando é o nome da conta

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
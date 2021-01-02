"""Application to hack the transposition cipher with brute force"""

import pyperclip
import detect_english
import transposition_decrypt

def main():
    message_to_hack = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hacked_message = hack_transposition(message_to_hack)

    if hacked_message == None:
        print('Failed to hack encryption.')
        print(hacked_message)
    else:
        print('Copying hacked message to clipboard...')
        print(hacked_message)
        pyperclip.copy(hacked_message)


def hack_transposition(message):
    print('Attempting hack...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')
    
    for key in range(1, len(message)):
        # print(message)
        print('Trying key #%s...' % (key))
        decrypted_text = transposition_decrypt.decrypt_message(key, message)
        print(decrypted_text)

        if detect_english.is_english(decrypted_text):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decrypted_text[:100]))
            print()
            print('Enter D if hack appears successful. Hit any other key to continue hack attempts.')
            response = input('>')

            if response.strip().upper().startswith('D'):
                return decrypted_text

    return None

if __name__ == '__main__':
    main()
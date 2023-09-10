#Função determinando o tipo de caractere inserido
def alphanum(alfanum):
    print(alfanum.isalnum())

def main():
    #Digita o(s) caractere(s)
    alfanum = input("")

    #Mostra na tela se o caractere é alfanumérico
    alphanum(alfanum)

if __name__ == '__main__':
    main()

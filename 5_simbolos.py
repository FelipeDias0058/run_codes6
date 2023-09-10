import string

#Função determinando o tipo de caractere inserido
def f_simbolo(simbolo):
    if not (simbolo.isalnum() or simbolo.isspace()):
        return True
    return False
    
    
def main():
    #Digita o(s) caractere(s)
    simbolo = input("")

    #Mostra na tela True ou False, de acordo com o
    #tipo de caractere
    print(f_simbolo(simbolo))

if __name__ == '__main__':
    main()

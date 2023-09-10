#Função que lê o caractere, e diz se é ou não uma letra
def f_letra(letra):
    print(letra.isalpha())


def main():
    #Entrada do caractere
    letra = input("")

    #Exibe True ou False dependendo do caractere digitado
    f_letra(letra)

if __name__ == '__main__':
    main()



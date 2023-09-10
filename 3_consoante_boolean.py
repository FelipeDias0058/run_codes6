#Função que determina se o caractere é consoante ou não
def consoante(letra):
    consoantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    if letra in consoantes:
        return True
    return False

def main():
    #Entrada sde dados
    letra = input("")

    #Exibe True ou False na tela
    print(consoante(letra))

if __name__ == '__main__':
    main()

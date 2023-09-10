#Função que determina se o caractere é vogal ou não
def vogal(letra):
    vogais = "aeiouAEIOU"
    if letra not in vogais:
        return False
    return True

def main():
    #Entrada sde dados
    letra = input("")

    #Exibe True ou False na tela
    print(vogal(letra))

if __name__ == "__main__":
    main()
    

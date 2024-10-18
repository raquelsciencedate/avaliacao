#importar a bi
from deep_translator import GoogleTranslator
# Função para exibir o menu e obter a escolha do usuário
    
def exibir_menu():
    print("\nMenu de Idiomas:")
    print("1. Inglês")
    print("2. Espanhol")
    print("3. Francês")
    print("4. Alemão")
    print("5. Sair")
    opcao = input("Escolha um idioma para traduzir (ou 5 para sair): ")
    return opcao
# Dicionário de idiomas suportados
idiomas = {
    "1": "en",
    "2": "es",
    "3": "fr",
    "4": "de"
}

while True:
    opcao = exibir_menu()
    
    if opcao == "5":
        print("Saindo do programa...")
        break
    elif opcao in idiomas:
        idioma_escolhido = idiomas[opcao]
        tradutor = GoogleTranslator(source="pt", target=idioma_escolhido)
        
        texto = input("Digite o texto que você gostaria de traduzir: ")
        traducao = tradutor.translate(texto)
        print("Tradução:", traducao)
    else:
        print("Opção inválida. Tente novamente.")


# Inicializando os contadores de votos
excelente = 0
bom = 0
ruim = 0

# Mudado para 50 conforme o enunciado da atividade
# (Para testar rápido antes se quiser, pode mudar temporariamente para 3)
for i in range(50):
    print(f"\n--- Entrevistado {i + 1} ---")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE | 2 - BOM | 3 - RUIM")
    opiniao = input("Digite a opção (1, 2 ou 3): ")
    
    # Estrutura de decisão para contar os votos (movida para dentro do for)
    if opiniao == "1":
        excelente = excelente + 1
    elif opiniao == "2":
        bom = bom + 1
    elif opiniao == "3":
        ruim = ruim + 1

# Exibição do resultado final
print("\n===== RESULTADO FINAL =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas BOM: {bom}")
print(f"Quantidade de respostas RUIM: {ruim}")
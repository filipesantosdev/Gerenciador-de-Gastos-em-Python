gastos = []
categoria = None
descricao = None
valor = None


while True:
    try:
        print("""               ------ Bem-vindo -------
              1 - Adicionar gasto
              2 - Listar gastos
              3 - Relatório geral
              4 - Buscar gastos por categoria
              0 - Sair
             
              """)
        option = int(input("Digite a opção: "))
    except ValueError:
        print("Digite uma opção válida!!!")
        continue
# Add gastos
    if option == 1:
       try:
           valor = float(input("Digite o valor do gasto: "))
       except ValueError:
           print("O valor deve ser um número maior que 0")
           continue
       
       if valor <= 0:
           print("O valor deve ser maior que 0")
       else:
           categoria = str(input("Digite a categoria: ").strip())
           descricao = str(input("Digite a descrição: ").strip())
           if categoria == '' or descricao == '':
               print("Voçê deve colocar uma decrição válida, não é permitido espaço vazios!!!")
           else:
                gastos.append({"valor": valor, 
                          "categoria": categoria, 
                          "descrição": descricao})
# Lista
    elif option == 2:
        if len(gastos) == 0:
            print("Digite valores primeiro!!!")
        else:
            for i, gasto in enumerate(gastos, start= 1):
                print(f"""{i} - Valor: R${gasto["valor"]} | Categoria: {gasto["categoria"]} | Descrição: {gasto["descrição"]}
""")
# Report 
    elif option == 3:
        if len(gastos) == 0:
            print("Digite valores primeiro!!!")
        else:
            
            quantidade = 0
            soma = 0
            maior = None
            menor =None

            for gasto in gastos:
                quantidade += 1
                soma += gasto["valor"]
                if maior is None or maior <= gasto["valor"]:
                    maior = gasto["valor"]
                if menor is None or menor >= gasto["valor"]:
                    menor = gasto["valor"]

            media = soma / quantidade
            print(f"""""          -------- Relátorio: -------
                   Total gasto: {soma:.2f}
                   Maior gasto: {maior:.2f}
                   Menor gasto: {menor:.2f}
                   Quantidade de gastos: {quantidade}
                   Média de gastos: {media:.2f}
            """"")
#Filtro            
    elif option == 4:
        if len(gastos) == 0:
            print("Sem categorias existentes, adicione gastos primeiro!!!")
        else:
    
            busca = input("Digite a categoria que deseja buscar: ")
            quantidade = 0
            soma = 0
            maior = None
            menor =None

            for gasto in gastos:     
                if gasto["categoria"] == busca:       
                    quantidade += 1
                    soma += gasto["valor"]
                    if maior is None or maior <= gasto["valor"]:
                        maior = gasto["valor"]
                    if menor is None or menor >= gasto["valor"]:
                        menor = gasto["valor"]
            
            if quantidade == 0:
                print("Sem dados existentes")
            else:
                media = soma/quantidade
                print(f"""""          -------- {busca}: -------
                   Total gasto: {soma:.2f}
                   Maior gasto: {maior:.2f}
                   Menor gasto: {menor:.2f}
                   Quantidade de gastos: {quantidade}
                   Média de gastos: {(media):.2f}
            """"")
            
                
#Break
    elif option == 0:
        break

                


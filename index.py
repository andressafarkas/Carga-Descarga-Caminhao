def menu_inicial(): # Menu principal
    print("\n1 - Iniciar dia")
    print("2 - Realizar parada")
    print("3 - Consultar situação")
    print("4 - Listar pacotes")
    print("5 - Finalizar dia")
    print("6 - Gerar relatório")
    print("7 - Sair")
    escolha_menuPrincipal = input("\nDigite a opção desejada: ")
    return escolha_menuPrincipal

def menu_parada(): # Menu opção 1 - parada
    print("\n1 - Inserir pacote: ")
    print("2 - Retirar pacote: ")
    print("3 - Encerrar parada: ")
    opcao_menuParada = input("Informe a operação a ser realizada: ")
    return opcao_menuParada

volume = 0
verificador = False # Verificador para conseguir gerar relatório
peso = 0 # Peso dos pacotes somados
carga = [] # Lista da carga
maior_pacote = 0 # Maior peso de pacote
menor_pacote = 0 # Menor peso de pacote
menor_quantidade = 0 # Menor quantidade de pacote embarcado
maior_quantidade = 0 # Maior quantidade de pacote embarcado
menor_peso = 0 # Menor peso do dia
maior_peso = 0 # Maior peso do dia
valor_transportado = 0 # Valor que está transportando atualmente
numero_cargas = 0 # Váriavel do número de cargas
maior_peso_extra = [] # Maior peso excedente
maior_valor_extra = [] # Maior valor excedente

escolha_menuPrincipal = 0
while (escolha_menuPrincipal != '7'): # Caso opção for diferente de "Sair", faz os ifs
    escolha_menuPrincipal = menu_inicial() # Altera o valor da variavel de acordo com a entrada do usuário
    if escolha_menuPrincipal == '1':
        volume_max = int(input("Informe o volume máximo de carga (M³): ")) 
        peso_max = float(input("Informe o peso máximo de carga (Kg): ")) 
        print("Informações salvas com sucesso!\n")
    
    elif escolha_menuPrincipal == '2': # Realizar parada
        opcao_menuParada = menu_parada()
        if opcao_menuParada == '1': # Inserir pacote
            peso_pacote = 0
            i = int(input('Informe o número de pacotes a serem inseridos: ')) # Pra não ficar infinito e porque pode inserir mais de um pacote em uma parada DA PRA MUDAR
            if menor_quantidade == 0:
                menor_quantidade = i
                maior_quantidade = i
            if menor_quantidade > i:
                menor_quantidade = i
            if maior_quantidade < i:
                maior_quantidade = i
            if i > volume_max:
                print('Não é possível inserir mais do que o volume suportado!') # Verifica se não vai inserir mais do que o possível
            else:
                j = 1
                while j <= i:
                    peso_pacote = int(input('Informe o peso do pacote (Entre 1kg e 99kg): '))
                    if (peso_pacote < 1 or peso_pacote > 99): # Se peso for maior que 99 ou menor que 1, imprime valor inválido
                        print("O valor informado é inválido!")
                    else:
                        if menor_pacote == 0:      
                            menor_pacote = peso_pacote
                            maior_pacote = peso_pacote
                        if menor_pacote > peso_pacote:
                            menor_pacote = peso_pacote
                        if maior_pacote < peso_pacote:
                            maior_pacote = peso_pacote
                        peso += peso_pacote
                        valor_transporte = 0
                        if peso <= (volume_max * 10):
                            valor_transporte = peso_pacote * 1.5
                            valor_transportado += valor_transporte
                            carga.append(peso_pacote) # Adicionar o peso dentro do array carga
                            print('Custo do transporte: R$', valor_transporte) # Calcula o valor do transporte
                        if peso > (volume_max * 10): # Se o peso ultrapassar o limite de 10 vezes o volume max
                            tarifa_extra = input("Devido ao peso do pacote, deve ser cobrado um valor extra de R$ 0,80 por kilo excedente. Aceitar tarifa extra? (S/N) ")
                            if tarifa_extra == "S" or tarifa_extra == "s": # Calcula o valor extra e imprime
                                peso_extra = peso - (volume_max * 10)
                                carga.append(peso_pacote) # Adicionar o peso dentro do array carga
                                maior_peso_extra.append(peso_extra) # Cria uma lista com todos os pesos extras
                                valor_extra = peso_extra * 0.8 # Valor do pacote mais o adicional de 0,80 para cada kg excedente
                                valor_transporte = (peso_pacote * 1.5) + valor_extra
                                valor_transportado += valor_transporte
                                maior_valor_extra.append(valor_extra) # Cria uma lista com todos os valores extras
                                print('Custo do transporte mais o extra: R$', valor_transporte)
                            elif tarifa_extra == "N" or tarifa_extra == "n": # Se não, pacote não embarcado
                                peso -= peso_pacote
                                print("Pacote não embarcado!")
                            else:
                                print("Resposta inválida!")
                        if maior_peso == 0:
                            maior_peso = peso
                            menor_peso = peso
                        if maior_peso < peso:
                            maior_peso = peso
                        if menor_peso < peso:
                            menor_peso = peso
                    j += 1
                numero_cargas = j
        elif opcao_menuParada == '2': # Retirar pacote
            if numero_cargas == 0:
                print('Não é possível retirar pacotes, pois não existem pacotes carregados!') # Se for digitado algum valor que não está nas opções, valor inválido
            else:
                for ultima_carga in range(0, len(carga)+1):
                    if ultima_carga == len(carga):
                        print('Último pacote inserido: ', carga[ultima_carga - 1]) # Informa o último pacote que foi inserido
                        remover_pacote = input('Tem certeza de que deseja remover o pacote de peso ({})? (S/N) '.format(carga[ultima_carga - 1])) # Pergunta se o usuário tem certeza de que quer remover o pacote
                        if remover_pacote == 'S' or remover_pacote == 's':
                            peso -= carga[ultima_carga-1] # Diminui o peso do pacote do peso total
                            valor_transportado -= carga[ultima_carga-1] # Remove o valor do último pacote
                            numero_cargas -= 1 # Diminui o número de cargas
                            carga.pop(ultima_carga-1)
                            print('Pacote removido!')
                        elif remover_pacote == 'N' or remover_pacote == 'n': # Não remove o pacote
                            print('Pacote não removido!')
                        else: # Se for inserido algo diferente de S/s ou N/n, informa que o valor é inválido
                            print('Valor inválido!')
        elif opcao_menuParada == '3': # Encerrar parada
            print("Encerrando parada...\n")
        else: # Se for digitado algum valor que não está nas opções, valor inválido
            print("Valor inválido")
            break

    elif escolha_menuPrincipal == '3': # Consultar situação
        print('\nPeso carregado: ', peso)
        if peso <= (volume_max * 10):
            print('Peso restante: ', peso_max - peso)
        # print("Peso máximo: ", peso_max)
        print('\nQuantidade de pacotes carregados: ', len(carga))
        print('Quantidade de pacotes restantes: ', volume_max - len(carga))
        print('Quantidade máxima: ', volume_max)
        print('\nValor transportado: R${:.2f} '.format(valor_transportado))
        if valor_transportado < (volume_max * 1.5):
            print('Valor restante: R${:.2f} '.format((volume_max * 1.5) - valor_transportado))
        elif valor_transportado == (volume_max * 1.5):
            print('Não há valor excedente ou restante')
        else:
            print('Valor excedente: R${:.2f} '.format(valor_transportado - (volume_max * 10)))
        print('Valor padrão máximo: R$', volume_max * 10)

    elif escolha_menuPrincipal == '4': # Listar pacotes 
        contador = 0
        print("  ----")
        print("/    |", end="")
        for x in carga:
            if carga[contador] > 0:
                print("|", carga[contador], "|", end="")
            else:
                if contador > 0:
                    print('|   |', end='')
            contador += 1
        print("\n-----|", end="")
        for x in carga:
            print("------", end='')
        print("\n\-()-|   /()\   ", end='')
        roda = 0
        while roda <= len(carga):
            if roda % 3 == 0 and roda > 0:
                print("/()()\       ", end='')
                print("")
            roda+=1

    elif escolha_menuPrincipal == '5': #Finalizar dia
        verificador = True # Dia finalizado, agora pode acessar o relatório
        print("Dia finalizado! \n")
    
    elif escolha_menuPrincipal == '6': # Relatório
        if verificador == False:
            print('Finalize o dia para poder gerar o relatório!')
        else:
            print('Menor peso de pacote individual: ', menor_pacote)
            print('Maior peso de pacote individual: ', maior_pacote)
            print('Menor quantidade de pacotes embarcados em uma parada:', menor_quantidade)
            print('Maior quantidade de pacotes embarcados em uma parada:', maior_quantidade)
            print('Menor quantidade total de peso no caminhão ao encerrar parada: ', menor_peso)
            print('Maior quantidade total de peso no caminhão ao encerrar parada: ', maior_peso)
            if len(maior_peso_extra) > 0:
                print('Maior peso excedente durante todo o dia: ', max(maior_peso_extra))
            else:
                print("Não houve peso excedente durante o dia!")
            if len(maior_valor_extra) > 0:
                print('Maior valor excedente durante todo o dia: ', max(maior_valor_extra))
            else:
                print("Não houve valor excedente durante o dia!")
    elif escolha_menuPrincipal == '7': # Sair do processo
        print('Saindo...')
        break
else: # Se for digitado algum valor que não está nas opções, valor inválido
    print("Valor inválido")

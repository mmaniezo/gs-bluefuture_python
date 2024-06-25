def forca_opcao(lista_opcoes, msg):
    msg_erro = '\n'.join(lista_opcoes)
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print(f"Opção inválida! Somente essas:\n{msg_erro}")
        opcao = input(msg)
    return opcao

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return num

def meu_index(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return

def pag_dados():
    print("Bem-vindo(a) à página de Dados sobre os Oceanos!")
    opcoes = ['sim', 'não']
    continuar = forca_opcao(opcoes, "Você deseja continuar nessa página? [sim][não]\n-> ")
    if continuar == 'sim':
        cidades = ["Santos", "Vitória", "Balneário Camboriú", "Salvador"]
        cidades_num = ['1', '2', '3', '4']
        temperaturas = [27, 26, 25, 27]
        pHs = [7.6, 8.1, 7.9, 8.0]
        turbidez = [100, 49, 82, 19]
        nvls_oxigenio_dissolvido = [2.1, 5, 3.2, 6]
        salinidades = [45, 38, 40, 35]
        qntd_microplasticos = [1000, 500, 700, 200]
        while True:
            for i in range(len(cidades)):
                print(f"{cidades_num[i]} - {cidades[i]}")
            escolha_cidade = forca_opcao(cidades_num,
                                        "Sobre o mar de qual cidade você deseja saber os dados? (Digite o número)\n-> ")
            indice = meu_index(cidades_num, escolha_cidade)
            if temperaturas[indice] > 25 and temperaturas[indice] < 27:
                estado_temp = 'OK'
            else:
                estado_temp = 'RUIM'

            if pHs[indice] >= 8 and pHs[indice] <= 8.3:
                estado_ph = 'OK'
            else:
                estado_ph = 'RUIM'

            if turbidez[indice] <= 50:
                estado_turbidez = 'OK'
            else:
                estado_turbidez = 'RUIM'

            if nvls_oxigenio_dissolvido[indice] >= 5 and nvls_oxigenio_dissolvido[indice] <= 6:
                estado_oxigenio = 'OK'
            else:
                estado_oxigenio = 'RUIM'

            if salinidades[indice] >= 33 and pHs[indice] <= 37:
                estado_sal = 'OK'
            else:
                estado_sal = 'RUIM'

            if qntd_microplasticos[indice] <= 300:
                estado_microp = 'OK'
            else:
                estado_microp = 'RUIM'

            print(f"Temperatura: {temperaturas[indice]}°C - {estado_temp}\n"
                  f"pH: {pHs[indice]} - {estado_ph}\n"
                  f"Turbidez: {turbidez[indice]} NTU - {estado_turbidez}\n"
                  f"Nível de oxigênio dissolvido: {nvls_oxigenio_dissolvido[indice]} mg/L - {estado_oxigenio}\n"
                  f"Salinidade: {salinidades[indice]}% - {estado_sal}\n"
                  f"Quantidade de micropláticos: {qntd_microplasticos[indice]} g - {estado_microp}\n")

            ver_mais = forca_opcao(opcoes, "Deseja ver dados de outra cidade? [sim][não]\n-> ")
            if ver_mais == 'não':
                break

def pag_solucionar_reports(agente):
    print("Bem-vindo(a) à página de Solucionar Reports")
    opcoes = ['sim', 'não']
    continuar = forca_opcao(opcoes, "Você deseja continuar nessa página? [sim][não]\n-> ")
    if continuar == 'sim':
        titulos_reports_pendentes = ["Lixo na praia em Peruíbe",
                                     "Esgoto sendo derramado no mar em Santos",
                                     "Garrafas pet na areia da Prainha, em Caraguá"]
        locais_reports_pendentes = ["Praia do Guaraú, em Peruíbe, em frente ao quiosque Mar Azul",
                                    "Santos, Praia do Gonzaga, na ponta direita da praia",
                                    "Caraguatatuba, Prainha, próximo ao estacionamento"]
        descricoes_reports_pendentes = ["Muitas garrafas de vidro, cigarros e embalagens plásticas jogadas na areia",
                                        "A água do mar na ponta direita da praia está com uma coloração marrom e com um odor insuportável",
                                        "Aparentemente houve uma festa aqui, e deixaram na areia muitas garrafas pet"]
        reports_pendentes_num = ['1', '2', '3']
        for i in range(len(reports_pendentes_num)):
            print(f"\nReport {reports_pendentes_num[i]}\n"
                  f"Título: {titulos_reports_pendentes[i]}\n"
                  f"Local: {locais_reports_pendentes[i]}\n"
                  f"Descrição: {descricoes_reports_pendentes[i]}\n")
        escolha_report = forca_opcao(reports_pendentes_num, "Digite o número do report que deseja solucionar:\n-> ")
        data = input("Em qual data você pretende resolver esse report?\n-> ")
        qntd_colaboradores = verifica_numero("Quantos colaboradores estarão presentes?\n-> ")

        print(f"Você irá resolver o Report {escolha_report}, na data {data}, com {qntd_colaboradores} colaboradores!\n"
              f"Obrigado por ajudar os oceanos, {agente}!")

print("====== Seja bem-vindo(a) ao Sea Connect! ======")
tipos_cadastro = ["Pessoa Física", "Empresa"]
tipos_cadastro_num = ['1', '2']
print(f"Tipos de cadastro:\n"
      f"{tipos_cadastro_num[0]} - {tipos_cadastro[0]}\n"
      f"{tipos_cadastro_num[1]} - {tipos_cadastro[1]}")
tipo_cadastro = forca_opcao(tipos_cadastro_num, "Digite o número referente ao seu tipo de cadastro:\n-> ")

if tipo_cadastro == '1':
    nome = input("Qual seu nome completo?\n-> ")
    username = input("Qual nome de usuário você quer usar na plataforma?\n-> ")
    while len(username) < 5:    # Testando se o nome de usuário tem no mínimo 5 caracteres
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        username = input("Qual nome de usuário você quer usar na plataforma?\n-> ")

    email = input("Qual o seu email?\n-> ")
    tem_arroba = False
    for i in range(len(email)):     # Verificando se o email possui um '@'
        if email[i] == '@':
            tem_arroba = True
            break
    while not tem_arroba:
        print("Email inválido! Tente novamente.")
        email = input("Qual o seu email?\n-> ")

    telefone = verifica_numero("Qual seu número de telefone?\n-> ")
    while not (len(telefone) == 11):
        print("Número de telefone inválido! Tente novamente.")
        telefone = verifica_numero("Qual seu número de telefone?\n-> ")

    senha = input("Crie sua senha de acesso:\n-> ")
    while len(senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres.")
        senha = input("Crie sua senha de acesso:\n-> ")

    confirma_senha = input("Para confirmar, digite a senha novamente:\n-> ")
    while confirma_senha != senha:
        print("As senhas informadas são distintas!")
        confirma_senha = input("Para confirmar, digite a senha novamente:\n-> ")

    print("Cadastro realizado com sucesso! :)\n"
          "Mergulhando no Sea Connect...")

    while True:
        paginas = ["Criar Report", "Solucionar Report", "Acessar dados sobre os oceanos"]
        paginas_num = ['1', '2', '3']
        for i in range(len(paginas)):
            print(f"{paginas_num[i]} - {paginas[i]}")
        pagina = forca_opcao(paginas_num, f"O que deseja fazer, {username}?\n-> ")

        if pagina == '1':       # Criando um report
            print("Bem-vindo(a) à página de Criar Reports")
            opcoes = ['sim', 'não']
            continuar = forca_opcao(opcoes, "Você deseja continuar nessa página? [sim][não]\n-> ")
            if continuar == 'sim':
                titulo_report = input("Digite um título para o seu report:\n-> ")
                local = input("Qual o local/endereço do seu report?\n-> ")
                descricao = input("Escreva uma descrição para o seu report:\n-> ")
                midia = input("Insira uma imagem ou vídeo:\n-> ")      # Apenas simbólico

                dados = ["Título", "Local", "Descrição", "Mídia"]
                dados_num = ['1', '2', '3', '4']
                while True:
                    print(f"Seu report será visto assim:\n"
                          f"Título: {titulo_report}\n"
                          f"Local: {local}\n"
                          f"Descrição: {descricao}\n"
                          f"Mídia: {midia}\n")
                    editar = forca_opcao(opcoes, "Deseja editar algum dado? [sim][não]\n-> ")
                    if editar == 'não':
                        break
                    else:
                        for i in range(len(dados)):
                            print(f"{dados_num[i]} - {dados[i]}")
                        dado = forca_opcao(dados_num, "Digite o número que corresponde ao dado que deseja editar:\n-> ")

                        if dado == '1':
                            titulo_report = input("Digite um título para o seu report:\n-> ")
                        elif dado == '2':
                            local = input("Qual o local/endereço do seu report?\n-> ")
                        elif dado == '3':
                            descricao = input("Escreva uma descrição para o seu report:\n-> ")
                        else:
                            midia = input("Insira uma imagem ou vídeo:\n-> ")  # Apenas simbólico

                print(f"Seu report:\n"
                      f"Título: {titulo_report}\n"
                      f"Local: {local}\n"
                      f"Descrição: {descricao}\n"
                      f"Mídia: {midia}\n"
                      f"\nObrigado por ajudar os oceanos, {username}!")

        elif pagina == '2':     # Solucionando um report
            pag_solucionar_reports(username)

        else:       # Acessando os dados sobre os oceanos
            pag_dados()

        opcoes_retornar = ['sim', 'não']
        retornar = forca_opcao(opcoes_retornar, "Deseja retornar para a página inicial? [sim][não]\n-> ")
        if retornar == 'não':
            break

else:
    nome_empresa = input("Qual o nome da empresa?\n-> ")

    email_empresa = input("Qual o seu email da empresa?\n-> ")
    tem_arroba = False
    for i in range(len(email_empresa)):  # Verificando se o email possui um '@'
        if email_empresa[i] == '@':
            tem_arroba = True
            break
    while not tem_arroba:
        print("Email inválido! Tente novamente.")
        email = input("Qual o seu email?\n-> ")

    cnpj = verifica_numero("Qual o CNPJ da empresa?\n-> ")
    while not (len(cnpj) == 14):
        print("CNPJ inválido! Tente novamente.")
        cnpj = verifica_numero("Qual o CNPJ da empresa?\n-> ")

    senha = input("Crie sua senha de acesso:\n-> ")
    while len(senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres.")
        senha = input("Crie sua senha de acesso:\n-> ")

    confirma_senha = input("Para confirmar, digite a senha novamente:\n-> ")
    while confirma_senha != senha:
        print("As senhas informadas são distintas!")
        confirma_senha = input("Para confirmar, digite a senha novamente:\n-> ")

    print("Cadastro realizado com sucesso! :)\n"
          "Mergulhando no Sea Connect...")

    while True:
        paginas = ["Solucionar Report", "Acessar dados sobre os oceanos"]
        paginas_num = ['1', '2']
        for i in range(len(paginas)):
            print(f"{paginas_num[i]} - {paginas[i]}")
        pagina = forca_opcao(paginas_num, f"O que deseja fazer, {nome_empresa}?\n-> ")

        if pagina == '1':
            pag_solucionar_reports(nome_empresa)

        else:
            pag_dados()

        opcoes_retornar = ['sim', 'não']
        retornar = forca_opcao(opcoes_retornar, "Deseja retornar para a página inicial? [sim][não]\n-> ")
        if retornar == 'não':
            break
# Bibliotecas importadas
import sys
import requests

# Funcao para exibir o menu principal
def exibir_menu():
    input("Pressione Enter para ir para o menu")
    print()
    print()
    print()
    print()
    print("Selecione uma opcao:")
    print("1. Montar um computador")
    print("2. Principais avarias e solucoes")
    print("3. Rede local com fios")
    print("4. Rede local sem fios")
    print("5. Caracteristicas de componentes de hardware")
    print("6. Tipos de memorias")
    print("7. Tipos de processadores")
    print("0. Sair")
    
# Funcao para montar um computador (passo a passo)
def montar_computador():
    print("Bem-vindo ao assistente de montagem de computadores!")
    print("Siga as instrucoes passo a passo e confirme cada etapa concluida.")
    print()
    print()
    print("⠀⠀⣤⣤⣤⣤⣤⣤⣤⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀")
    print("⠀⠀⣿⣤⣤⣤⣤⣤⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀")
    print("⠀⠀⣿⣤⣤⣤⣤⣤⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀")
    print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀")
    print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀")
    print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⠀⠀")
    print("⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀")
    print("⠀⠀⣿⣿⣿⣿⣏⣹⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀ ⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀")
    print()
    print("Pressione Enter para continuar o Tutorial")
    print()
    print()
    # 1. Preparacao
    input("Reuna todas as pecas necessarias em uma superficie limpa estiver preparada: ")
    input("Leia os manuais de instrucoes de todos os componentes: ")
    
    # 2. Instalar a placa-mae no gabinete
    input("Remova os parafusos necessarios do gabinete")
    input("Alinhe a placa-mae corretamente com os encaixes de montagem")
    input("Prenda a placa-mae ao gabinete usando os parafusos fornecidos")
    
    # 3. Instalar o processador
    input("Localize o soquete correto para o processador na placa-mae e abra a alavanca de liberacao.")
    input("Remova a tampa protetora do soquete e alinhe corretamente o processador.")
    input("Baixe suavemente o processador no soquete e feche a alavanca de liberacao para prende-lo.")
    
    # 4. Instalar o cooler do processador
    input("Aplique a pasta termica no processador (se necessario) e alinhe o cooler com os encaixes na placa-mae.")
    input("Prenda o cooler usando os parafusos ou clipes fornecidos")
    
    # 5. Instalar a memoria RAM
    input("Localize os slots de memoria RAM na placa-mae e abra cuidadosamente as travas.")
    input("Alinhe os encaixes da memoria RAM com o slot e insira-a firmemente. Feche as travas para prende-la.")
    
    # 6. Instalar a fonte de alimentacao
    input("Remova os parafusos necessarios do gabinete e deslize a fonte de alimentacao para dentro do gabinete.")
    input("Prenda a fonte de alimentacao ao gabinete usando os parafusos fornecidos.")
    
    # 7. Instalar as unidades de armazenamento
    input("Localize as baias para as unidades de armazenamento no gabinete e deslize-as cuidadosamente para dentro.")
    input("Prenda as unidades de armazenamento usando os parafusos fornecidos.")
    
    # 8. Instalar a placa de video (se aplicavel)
    placa_video = input("Voce precisa instalar uma placa de video? (s/n): ").lower()
    if placa_video == "s":
        input("Localize o slot de expansao PCI-Express na placa-mae e remova a tampa do slot.")
        input("Alinhe a placa de video com o slot e insira-a firmemente.")
        input("Prenda a placa de video ao gabinete usando os parafusos fornecidos.")
    else:
        input("Vamos passar a montagem da Placa de Video.")
    
    # 9. Conectar todos os cabos
    input("Conecte os cabos de alimentacao da fonte as devidas conexoes na placa-mae, unidades de armazenamento e placa de video.")
    input("Conecte os cabos de dados (SATA, IDE) as unidades de armazenamento.")
    input("Conecte os cabos de audio, USB, painel frontal e outros perifericos a placa-mae.")
    
    # 10. Verificacao final
    input("Verifique se todos os componentes estao firmemente instalados e se todos os cabos estao conectados corretamente. Feche o gabinete e prenda os parafusos.")
    
    # 11. Ligar o computador e instalar o sistema operacional
    input("Conecte o cabo de alimentacao a fonte de alimentacao e ligue o computador.")
    print("Boa! Agora voce pode instalar o sistema operacional desejado a partir de um disco de instalacao ou midia USB.")
    
    print("Montagem do computador concluida com sucesso!")

# Funcao para lidar com avarias e solucoes
def avarias_solucoes():
    # Codigo para listar avarias comuns, suas causas e solucoes
    print("Especifique qual e o seu problema")
    print("Qual das opcoes se encaixa melhor na sua situacao?")
    print("1. O computador liga?")
        # 1. O computador liga?
    liga = input("O computador liga? (s/n) ").lower() == "s"

    if liga:
        # 1.1.1. A tela acende?
        tela_acende = input("A tela acende? (s/n) ").lower() == "s"

        if tela_acende:
            # 1.1.1.1.1. Ha imagem na tela?
            tem_imagem = input("Ha imagem na tela? (s/n) ").lower() == "s"

            if tem_imagem:
                # 1.1.1.1.1.1.1. O sistema operacional inicia normalmente?
                sistema_inicia = input("O sistema operacional inicia normalmente? (s/n) ").lower() == "s"

                if sistema_inicia:
                    print("Seu computador esta funcionando corretamente.")
                else:
                    print("Possivel problema com o sistema operacional ou inicializacao.")
                    print("Solucao: Reinicie em modo de seguranca, verifique atualizacoes, faca uma restauracao do sistema.")
            else:
                print("Problema com a placa de video ou conexoes.")
                print("Solucao: Verifique as conexoes da placa de video, tente uma placa de video alternativa.")
        else:
            # 1.1.1.2. Nao
            print("Problema com o monitor ou conexoes de video.")
            print("Solucao: Verifique as conexoes do monitor, tente um monitor alternativo.")

        # 1.1.2. Ha algum som ou LED aceso?
        tem_som_led = input("Ha algum som ou LED aceso? (s/n) ").lower() == "s"

        if tem_som_led:
            print("Possivel problema com a inicializacao ou sistema operacional.")
            print("Solucao: Tente inicializar em modo de seguranca, verifique logs de erro, faca uma restauracao do sistema.")
        else:
            print("Possivel problema com a fonte de alimentacao ou placa-mae.")
            print("Solucao: Verifique as conexoes da fonte de alimentacao, teste a fonte de alimentacao, troque a placa-mae.")
    else:
        # 1.2.1. A fonte de alimentacao esta ligada corretamente?
        fonte_ligada = input("A fonte de alimentacao esta ligada corretamente? (s/n) ").lower() == "s"

        if fonte_ligada:
            print("Possivel problema com a fonte de alimentacao ou placa-mae.")
            print("Solucao: Teste a fonte de alimentacao, troque a placa-mae.")
        else:
            print("Verifique as conexoes da fonte de alimentacao.")
            print("Solucao: Conecte corretamente a fonte de alimentacao.")

    # 2. O computador esta lento ou travando?
    lento_travando = input("\nO computador esta lento ou travando? (s/n) ").lower() == "s"

    if lento_travando:
        # 2.1. Ha muito barulho vindo do cooler ou ventoinha?
        barulho_cooler = input("Ha muito barulho vindo do cooler ou ventoinha? (s/n) ").lower() == "s"

        if barulho_cooler:
            print("Possivel superaquecimento.")
            print("Solucao: Limpe o cooler e ventoinhas, aplique pasta termica nova no processador.")
        else:
            # 2.1.2.1. Ha muitos programas abertos?
            muitos_programas = input("Ha muitos programas abertos? (s/n) ").lower() == "s"

            if muitos_programas:
                print("Fechar programas desnecessarios para liberar memoria.")
                print("Solucao: Feche programas que nao estao sendo utilizados.")
            else:
                # 2.1.2.1.2.1. O disco rigido esta cheio?
                disco_cheio = input("O disco rigido esta cheio? (s/n) ").lower() == "s"

                if disco_cheio:
                    print("Libere espaco em disco removendo arquivos desnecessarios.")
                    print("Solucao: Remova arquivos e programas que nao sao mais necessarios.")
                else:
                    print("Possivel problema com software ou hardware (verificar uso de CPU, memoria, etc.)")
                    print("Solucao: Monitore o uso de recursos com o Gerenciador de Tarefas, atualize drivers, verifique aplicativos que consomem muitos recursos.")

    # 3. Ha algum erro ou mensagem especifica?
    tem_erro = input("\nHa algum erro ou mensagem especifica? (s/n) ").lower() == "s"

    if tem_erro:
        print("Coletar informacoes sobre o erro e pesquisar solucoes especificas.")
        print("Solucao: Anote o codigo de erro ou mensagem exata, pesquise em foruns e sites de suporte para solucoes.")
    else:
        print("Realizar mais perguntas de troubleshooting para identificar o problema.")
        print("Solucao: Descreva o problema com mais detalhes para obter uma solucao mais precisa.")

    print("\nObrigado por utilizar a ferramenta de diagnostico de problemas em computadores.")
    pass

# Funcao para rede local com fios
def rede_local_fios():
    # Codigo para explicar componentes, configuracao de rede local com fios
    print("Para fazermos a confiuracao de uma rede local com fios precisaremos de:")
    print("-Um Router ou um Switch")
    print("-1 ou mais cabos de Ethernet")
    print("-1 ou mais PCs com porta para o cabo ethernet")
    print("")
    print("*****Instalacao dos Equipamentes necessarios*****")
    print("Para comecar vamos conectar o Router ou o Switch a eletricidade")
    print("Vamos conectar uma das pontas do cabo Ethernet ao Router/Switch,")
    print("e a outra ponta a entrada no PC ou PCs")
    print("")
    print("*****Confiuracao da Rede Local*****")
    print("Podemos optar por 2 opcoes sendo elas:")
    print("1. Confiurar um Ip estatico manualmente")
    print("2. Deixar que o Router atribua um Ip dinamico com o protocolo (DHCP)")
    print("3. Verifique o seu ip")
    print("")
    print("Como gostaria de confiurar a sua rede local?")
    opcao1 = input("Opcao: ")
    if opcao1 == "1":
        print("Para a confiuracao de um ip estatico, sera preciso definir  um ip mascara de sub-rede")
        print("e um gateway padrao para cada dispositivo, em seguida vamos configurar o roteador")
        print()
        print("Vamos acessar a interface de configuracao do roteador,")
        print("para escolhermos o nome do rede(SSID) e a palavra-passe da rede,")
        print("e possivel ir mais alem e e configurar opcoes como o acesso dos varios dispositivos, a firewall e o DHCP.")
    if opcao1 == "2":
        print("Para configurar um ip dinamico (DCHP), vamos aceder a interface do roteador e vamos procurar por DCHP nas opcoes")
        print("configuramos o intervalo de enderecos IP que o roteador ira atribuir aos dispositivos conectados a rede")
        print()
        print("Agora nos dispositivos que queremos configurar vamos mudar a atribuicao do ip para automatico ou habilitar o DCHP,")
        print("so salvar e esta feita a configuracao do ip")
    if opcao1 == "3":
        response = requests.get('https://ifconfig.me/ip')
        ip_address = response.text.strip()

        print(f"O seu ip e: {ip_address}")        
            

# Funcao para rede local sem fios
def rede_local_wireless():
    # Codigo para explicar configuracao de rede local wireless
    print("Para ocnfigurarmos uma rede local sem fios vamos precisar de:")
    print("-Um Router sem fio")
    print("Para começar vamos conectar o router à eletricidade, vamos ligar o router a um cabo de Rede que tenha acesso à internet,")
    print("Vamos entrar na interface de configuração do router e definir o ip do router. Configuramos o nome da rede e a palavra-passe da mesma, usando o WPA2 ou o WPA3 ")
    print("Para acessar a rede desse mesmo router vamos ao dispositivo que queremos ligar ao Wifi")
    print("Vamos às definições do Wifi do dispositivo e fazemos a ligação colocando a palavra passe correspondente á do Wifi.")
    pass

# Funcao para caracteristicas de hardware
def caracteristicas_hardware():
    # Codigo para detalhar caracteristicas de componentes de hardware
    print("Vamos falar das caracteristicas dos componentes de um PC")
    print("MotherBoard          - A motherboard é responsavel por interligar os outros componentes, sendo a central do computador. É há motherboard que todos os componentes se vão ligar  ")
    print("Processador          - O processador é a unidade de processamento do computador, vai executar os comandos dados ao computador")
    print("HD/SSD               - Os HDs e SSDs são usados para guardar os dados do computador, para guardar o sistema operativo e fazer o boot do mesmo")
    print("RAM                  - A Ram é a uam memoria de acesso aleatorio, que armazena os dados e os programas que estão a ser usados")
    print("Placa Grafica        - A Placa Grafica é responsavel por renderizar imagens, videos, e graficos 3D. É a Unidade de Processamento Grafico")
    print("Fonte de Alimentação - A fonte de alimentação como o nome indica ela alimenta o PC, é responsavel pelos niveis de voltagem que são entregues ao PC.")
    print("Caixa                - A caixa abriga todos os compontentes dentro dela, protege os compontentes, facilita a organização e ajuda no fluxo do ar.")
    pass

# Funcao para tipos de memorias
def tipos_memorias():
    # Codigo para explicar diferentes tipos de memorias
    print("Existem diferentes tipos de memórias, como:")
    print("1. Memorias de armazenamento de dados")
    print("2. Memorias RAM")
    opcaotipos_de_memorias = input("Sobre quais tipos de memorias gostarias de saber mais: ")
    if opcaotipos_de_memorias == "1":
        print("As memorias de armazenamento de dados são memorias que como o nome indica armazenão dados")
        print("Dentro deste tipos de memorias podemos ver outras memorias como:")
        print("1. HD  (Hard Disk)")
        print("2. SSD (Solid-State Drive)")
        print("Nestes discos ainda podemos ir mais a fundo e ver os diferentes tipos e papeis de cada 1")
        opcaotipos_de_memorias1 = input("Qual o disco que vamos ver a seguir: ")
        if opcaotipos_de_memorias1 == "1":
            print("Os HDs têm o nome de discos rigidos podem armazenar Gigabytes, Terabytes ou até mesmo Petabytes de informação")
            print("O papel do HD é fazer o armazenamento de ficheiros de forma local, carregar o sistema operativo e podem ser usados para recuperar dados caso haja algum problema com o computador")
            print("Os HDs tem vindo a ficar para trás por conta dos SSDs que são melhores em muitos aspetos")
            print("Desde a criação do HDs tem havido muitas versões de HD, como: ")
            print("HD ATA  - Surgiram em 1980, o seu espaço chega até aos 500Gb de espaço e a sua velocidade era de 8.3MB/s")
            print("HD SATA - Estes são os HDs mais usados a nivel domestico e os HDs mais populares da atualidade. Possuem 3 configração diferentes sendo elas SATA 1, SATA 2 e o SATA 3")
            print("          A sua velocidade maxima é de 600MB/s e o seu armazenamento pode variar entre 250GB e 15TB que é o armazenamento com mais espaço no momento deste trabalho")
            print("HD SCSI - Estamos a falar de um tipo de HD que é usado mais a nível corporativo do que domestico, estes HDs possuem preços elevados, taxas de transferencia gigantes e uma extensa capacidade de compartilhamento")
            print("HD SAS  - Esta é uma evolução dos HD SCSI, para os SCSI não se tornarem obsulentos tiveram uma evolução e têm caracteristicas como: ")
            print("            -Processadores Duplos")
            print("            -Rigidez Estrutural")
            print("            -Baixa Latência")
            print("Estes são os diversos tipos de HDs, queres conhecer os SSDs, vem ver como funcionam")
            
        if opcaotipos_de_memorias1 == "2":
            print("Os SSDs são tambem memorias de armazenamento de dados que possuem capacidades de armazenamento de 120GB até 8TB de espaço")
            print("O papel dos SSD, tal como os HDs serve para armazenar ficheiros, fazer boot dos sistemas operativos, entre outros. Vamos falar das principais vantagens dos SSD")
            print("       -São mais rapidos que os SSDs por não terem partes moveis, a diferença de velocidades é significativa, tendo uma grande diferença.")
            print("       -Os SSDs consumem menos energia, o que faz com que emitam menos calor")
            print("       -A sua durabilidade é maior que a dos HDs e são mais silenciosos")
            print("")
            print("Vamos falar sobre os tipos de SSD:")
            print("   -SSD SATA         - Este é um SSD que usa o protocolo SATA para ligar à motherboard.")
            print("   -SSD SATA EXPRESS - Estes SSD tem a possibilidade de ligar diretamente o SSD atraves das portas PCIe, mas podendo ainda usar a ligação SATA. É um SSD com um conexão hibrida,  mais segura e rapida")
            print("   -SSD NVMe         - Esta opcao é mais rapida, este SSD liga-se diretamento ao CPU para terem maior autonomia para focar na gravação, leitura da informação e otimização.")
            print("   -SSD M.2          - Os M.2 são SSDs que são pequenos e leves o que é ideal para computadores leves, como por exemplo portateis ou NUCs(Mini-PC)")
    pass

# Funcao para tipos de processadores
def tipos_processadores():
    # Codigo para explicar diferentes tipos de processadores
    print("Exitem diferentes tipos de processadores, vamos falar de alguns:")
    print(" -CPU - O CPU é responsavel pelo processamento geral do computador")
    print(" -GPU - A GPU é responsavel pelo processamento grafico como imagens, videos e os 3D")
    print(" -DSP - Os DSPs são responsaveis pelo processamento de sinais digitais, como o audio e o video. Estes processadores são usados para melhorar audios ou melhorar a qualidade de uma imagem.")
    print(" -NPU - Uma NPU foram projetadas para processarem tarefas relacionadas à Inteligencia Artificial e Machine Learning, acelarando o processo de treinamento das mesmas")  
    pass

# Loop principal
while True:
    exibir_menu()
    opcao = input("Opcao: ")

    if opcao == "1":
        montar_computador()
    elif opcao == "2":
        avarias_solucoes()
    elif opcao == "3":
        rede_local_fios()
    elif opcao == "4":
        rede_local_wireless()
    elif opcao == "5":
        caracteristicas_hardware()
    elif opcao == "6":
        tipos_memorias()
    elif opcao == "7":
        tipos_processadores()
    elif opcao == "0":
        sys.exit()
    else:
        print("Opcao invalida. Tente novamente.")
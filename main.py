
#! Como foi dado o paradmiga funcional no período, as telas também foram separadas assim.
#! Porém, para uma boa organização do código, o mais viável seria por meio de classes e métodos(POO) 
import smtplib              #!biblioteca que permite o python trabalhar com o protocolo SMTP
import PySimpleGUI as tela  #!biblioteca de interface gráfica;
import pyperclip            #!biblioteca para copiar texto para área de transferência;
from telas import cripto     #!importando cripto e suas subtelas;
from telas import tela_Email#!importando tela para envio de email
from telas import descript  #!importando tela para descriptografia e suas subtelas
from telas import loading   #!importando tela de loading 
import sqlite3              #!importando o modulo que da suporte ao banco de dados sqlite
import os                   #!importando modulo para criação de uma pasta 
import platform             #!importando o modulo para pegar a plataforma em que se encontra o usuário(suporte para linux e windows) neste programa

#! a primeira coisa a se fazer é  verificar em qual sistema operacional está sendo executado a conexão com um banco
#! caso não exista banco no dispositivo, o comando sqlite3.connect('diretório) irá criar.
#! Logo em seguida, é lançado o seguinte comando no banco: crie a tabela código se não existir uma.
#! Se o comando *sem* o IF NOT EXISTS for executado duas vezes no mesmo dispositivo, ele não conseguirá conexão o banco corretamente
#! porque a mesma coluna não pode ser criada duas vezes

#!criando pasta
#!Caso a pasta ja esteja criada, ele cai na exeção e executa o "pass"
#!Pense como se fosse um 'ignore o erro'
#!Este erro acontece porque toda vez que o programa for iniciado
#! ele tentará criar uma pasta, ou seja, se a pasta ja foi criada, ele não consegue cria-la novamente com o mesmo nome

def cria_ou_le_banco(x):
    try:
        #! conectando ou criando banco
        conex = sqlite3.connect(x)
        #! Usando a função de cursor para que possa ser feita alterações no banco com o SQL
        c = conex.cursor()
        #! Criando a tabela código se a mesma não existir
        c.execute("CREATE TABLE IF NOT EXISTS código (cod text)")
        #! Salvando para que os dados não sejam perdidos
        conex.commit()
    except:
        print('não foi possivel fazer conexão! :(')
#!Pegando o Sistema_Operacional
sistema_Operacional = platform.system()
#! Caso o usuário esteja no linux
#! pega o diretório home (não importa o usuário)
home= os.path.expanduser("~")#!pegando /home com o nome do usuário(pasta pessoal)
cwd = os.getcwd() #!Pegando diretório no qual está sendo executado o programa
if sistema_Operacional == 'Linux':
    try:
        os.chdir(home) #!Entrando no diretório
        os.makedirs('Db') #!criando a pasta
    except:
        pass
    cria_ou_le_banco(home+'/Db/dados.db')
    conex = sqlite3.connect(home+'/Db/dados.db')#! conexão depois da função (questão de escopo)
    c = conex.cursor() #! cursor depois da função (questão de escopo)
    img = f'{cwd}/img/01.png'
elif sistema_Operacional == 'Windows':
    try:
        os.chdir('C:\\')
        os.makedirs('Db')
    except:
        pass
    cria_ou_le_banco('C:\\Db\\dados.db')
    conex = sqlite3.connect('C:\\Db\\dados.db')
    c = conex.cursor()
    img=f'{cwd}\\img\\01.ico'

#+/**
#+ *optou-se por criar as telas em blocos/arquivos separados para assim
#+ *se ter uma melhor organização e manutenção entre as telas;
#+ */


#!Função que recebe um texto que será copiado para área de transferência;

def le(cox):
    pyperclip.copy(cox)
c.execute("SELECT cod FROM código")
valores = c.fetchone()
#!Verificando se o Usuário salvou login
#!Se o usuário salvou, a consulta no banco irá retornar o valor 'SIM'
#!Se o login foi salvo, o programa abre direto na segunda janela
if valores==('SIM',):
    janela1, janela2,janela3,janela4,janela5,janela6,janela7 = None, cripto.segundo(''),None,None,None, None,None
else:
    #!iniciando as telas;
    #!cripto | cripto | cripto | tela4 | tela5 | tela6 | tela7|  função.cripto  |       (temporário);
    janela1, janela2,janela3,janela4,janela5,janela6,janela7= cripto.primeiro(), None,None,None,None, None,None

#!Contador que armazenará o código ou a mensagem;
contador=''.encode("utf8")

while True:
    #!Variáveis para leitura das janelas, eventos e valores dos inputs; 
    window, event, values = tela.read_all_windows()
    
    if window == janela1 and event == tela.WIN_CLOSED or \
        window == janela2 and event == tela.WIN_CLOSED:
        break
    #! primeiro acesso no programa                      #!Evento enter no linux
    elif window == janela1 and (event == 'Login' or event == 'Return:36'):
        if values['nome'].lower().strip() == 'user' and values['senha'].strip() =='778592':
            janela1.Close()
            #!tela que pergunta se o usuário deseja salvar login no banco de dados 
            janela7 = descript.pergunta()
        else:
           bot= cripto.tela.popup('''
Login incorreto! Tente novamente
           ''',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
           if bot == 'OK':
               janela1.Close()
               janela1 = cripto.primeiro()
    #!Perguntando se o usuário deseja salvar o login
    elif window == janela7 and event == 'SIM' or event=='Return:36':
        janela7.Close()
        #!Query que salva o valor 'SIM' na única tabela do banco
        c.execute("INSERT INTO código VALUES('SIM')")
        #!Salvando
        conex.commit()
        janela2 = cripto.segundo('')
    #!Caso o usuário não queira salvar o login, nada será salvo e a tela2 será aberta
    #!Porém, sempre irá solicitar usuário e senha
    elif window == janela7 and event == 'NÃO':
        janela7.Close()
        janela2 = cripto.segundo('')
    #!Caso o usuário precise sair da conta, o banco de dados é limpo
    #!Não existe informações importantes no banco, por isso o delete sem WHERE
    elif window == janela2 and event == 'Sair da conta':
        var = cripto.tela.popup('Deseja sair da conta?',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        if var == 'OK':
            c.execute('DELETE FROM código')
            conex.commit()
            janela2.Close()
            janela1 = cripto.primeiro()
    #!Passando o valor da área de transferência, caso exista um, como parâmetro
    #!E reiniciando a janela para o elemento multiline receber um valor default e mostrar o que estava na área de
    #!transferência
    elif window == janela2 and event == 'Colar2':
        var = pyperclip.paste()
        if var == ' ':
            tela.popup('Nada para Colar',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        else:
            janela2.Close()
            janela2 = cripto.segundo(pyperclip.paste())
    #!Caso o usuário deseja criptografar a mensagem
    elif window == janela2 and event == 'Criptografar':
       #! reiniciando o contador para que uma tradução seja indepentende de outra
        contador =''

       
        var = list(values['menssagem'])

        if var == ['\n']:
            cripto.tela.popup('Nada para criptografar',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        else:
            janela3 = cripto.terceiro()
            #!Lista com o alfabeto de códigos
            codigos =[
                'cxr89,','fhH52,','3fgg7,','0829g,','5jfb2,','gca7d,','z1zca,','12cc9,',
                'aa5bc,','0820t,','1137g,','5jf4c,','3fg21,','z1zbz,','08291,','2448g,',
                '12ct1,','61bgg,','g5582,','12ca9,','61bt4,','8tz0g,','244cd,','5jfa0,',
                'gcaa3,','6zc2f,','aa5d4,','12cd6,','3fg56,','om3l4,','z2pla,','cac31,',
                'bi4c0,','hig98,','77tyx,','fuh76,','0pp61,','iuio9,','it552,','tig2a,',
                '01009,','j0a32,','m009g,','nha55,','iHbH7,','gg3rs,','b2b34,','9jgyt,',
                'op5H8,','x1c47,','189hi,','omlH7,','ad087,','ll282,','00llH,','c475a,',
                'k2bbc,','a35e9,','a3528,','04f74,','04gff,','0094g,','00920,','ef7d9,',
                'ef7e0,','gc8b0,','c2c51,','c2c47,','c2c91,','0c368,','6g7gg,','m4175,',
                'cop32,','32pco,','H40i9,','ccl22,','om675,','tjk82,','ph908,','eli56,',
                '29183,','292d0,','53gd1,','53gcg,','95767,','958c2,','958g3,','e47bf,',
                'c14e3,','c1421,','c15ed,','c15g8,','g6e4b,','g7wyx,','g6e4f,','g6e90,',
                'a784c,','bag58,','ba1ba,','2f149,','2f189,','64b01,','64cg0,','64dfa,',
                '887bc,','k9k0k,','abtur,','ciub4,','enop9,','i7858,','cac67,','ff650,'
            ]
            #!lista com o alfabeto, onde cada elemento do mesmo representa um código de 5 dígitos e uma virgula na lista códigos
            alfabeto=[
                'ú','Ú','y','r','j','k',' ','f',
                'o','q','a','h','v','ç','p','b',
                'g','s','m','d','t','z','c','i',
                'l','u','n','e','x','w','A','B',
                'C','D','E','F','G','H','I','J',
                'K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z',
                'Ç',',','.',';','?',':','ã','é',
                'à','á','õ','ó','ê','ô','â','Ã',
                'É','À','Á','Õ','Ó','Ê','Ô','Â',
                '1','2','3','4','5','6','7','8',
                '9','0','+','-','/','\\','*','$',
                '!',']','[','(',')','"','{','}',
                '=',"'",'_','Ç','\n','í','Í','#'
            ]
            #! Aqui é onde tudo acontece
            #! Esse laço de repetição que irá ler todos os elementos digitados
            #! o x recebe um elemento a cada laço, pois os elementos possuem cunho individual
            #! Ou seja, mesmo que fossem digitados: "aa", ele executará o laço duas vezes, com x valendo sempre a
            for x in var[0:]:
                #! Essa verificação é muito importante...
                #! Ela irá verificar a cada laço de repeditção, se o x existe na lista alfabeto
                #! Isso significa que se o usuário digitar uma letra que não consta na lista alfabeto, a tradução não será feita.
                #! caso x exista em alfabeto, ele executará o seguinte bloco de código, individualmente para cada laço
                if x in alfabeto:
                    #! Declaramos uma variável de nome: "posicao" que retorna o index do elemento consultado na lista alfabeto
                    #! o elemento que passamos como parâmetro é o proprio x, ja que na verificação anterior, constou-se que o x existe em alfabeto
                    #! Tudo que precisamos agora é do indice, para que se possa fazer a tradução de forma correta
                    #! A função index irá buscar na lista alfabeto, o número referente ao elemento x 
                    posicao = alfabeto.index(x)

                    #! Logo após isso, é só adicionar ao contador o código da lista codigos com o indice posicao
                    #! fazendo isso, obtemos a tradução de forma ordenada e correta
                    #! Isso é de suma importância, contando que o programa de descriptografia usa da ordem dos códigos para dar sentido aos textos
                    #! isso significa que a ordem do texto inicial é preservado
                    contador += codigos[posicao]
            #! Depois, é só printar o resultudado obtido da codficação dos elementos
            #! OBS. O componente Output da biblioteca PySimpleGUI considera a função print e mostra em uma aba de output 
            print(contador[:len(contador)-6])
        #! Verifição se a variável window é == a janela2(cripto) e se o evento Limpar foi disparado pelo usuario
        #! Caso o usuário queira limpar a tela, essa condição será verdadeira
    elif window == janela2 and event == 'Limpar':
        #! o contador é reiniciado, juntamente com a janela2
        contador = ''
        janela2.Close()
        janela2 = cripto.segundo('')
    #!Colocando o evento Copiar para as janelas de Descriptografia e criptografia
    #!Aproveitando código
    elif event == 'Copiar':
        if contador == '':
            bot = cripto.tela.popup('Sem arquivos para copiar',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
            if bot == 'OK':
                #!Verificando a janela
                if window == janela3:
                    janela3.Close()
                elif window == janela6:
                    janela6.Close()
        else:
            if window == janela3:
                le(contador[:len(contador)-6])
            elif window == janela6:
                le(contador)
            bot = cripto.tela.popup('Copiado para Área de transferência',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        

    #! se a variável window receber a janela 3 e o usuário disparar o evento Salvar(cliando no botão)
    #! A condição retornará verdadeira e irá executar o bloco de código
    
    elif window == janela3 and event == 'Enviar E-mail':
        #! chamando a função responsável por abrir a tela que envia email
        janela4 = tela_Email.Email()
    #! quando o usuário quiser enviar
    elif window == janela4 and event == 'Enviar':
        if values['para'] == '':
            tela_Email.tela.popup('Digite algo',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        else:
            try:#! primeiro, precisou criar um email para trabalhar com o protocolo SMTP 
                de = 'projetop1006@gmail.com'
                #!pegando o valor digitado, referente ao destinatário
                para= values['para']
                #! Iniciando uma instância da função SMTP. Dizendo o servidor(google) e a porta(587) padrão TLS
                server = smtplib.SMTP('smtp.gmail.com', 587)
                load = loading.loading('Colhendo informações...')
                #!Iniciando o protocolo(método da classe smtplib) TLS(Transport Layer Security)
                server.starttls()
                #! Fazendo login no email do projeto(método da classe smtplib)
                server.login(de, ',,,ola,mundO,,,')
                #! enviando a mensagem estertrvs@gmail.com
                load.Close()
                load = loading.loading('Enviando a mensagem....')
                #!Esse .encode deu bastante trabalho para descobrir kkkkk
                #!Ele serve para passar todas as mensagens para a codificação utf8
                #!Antes quando copiava algum texto da internet,
                #!Ele vinha em uma codificação binária que o protocolo, ou a lib não trabalhava
                #!Tudo que precisamos fazer então, foi passar o mais usual como parâmetro: UTF-8
                #!Código do antigo erro: UnicodeEncodeError
                server.sendmail(de, para, contador[:len(contador)-6].encode("utf8"))
                #! fechando servidor no programa
                server.quit()
                load.Close()
                bot = tela_Email.tela.popup('Email enviado com sucesso!',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
                if bot == 'OK':
                    janela4.Close()


            except:
                load.Close()
                tela_Email.tela.popup('''
                        Houve algum erro no envio! 

        Passo 1: Verifique sua conexão.

        passo 2: Verifique se a mensagem excede o tamanho 
                      máximo suportado pelo protocolo SMTP.

        passo 3: Verifique o email do destinatário.
                
                ''',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
    #!Passando da janela de Criptografia para a de descriptografia
    elif window == janela2 and event == 'bot1':
        #!Escondendo a janela2 e abrindo a janela5 
        janela2.hide()
        janela5 = descript.chama('')
    #!Voltando para a janela de Criptografia
    elif window == janela5 and event == 'bot2' or window == janela5 and event== tela.WIN_CLOSED:
        #! Mostrando a janela2 e fechando a janela 5
        janela2.un_hide()
        janela5.Close()
    #!Caso o usuário aperte no botão de descriptografia
    elif window == janela5 and event == 'Descriptografia':
        contador =''
        var = values['codigo1'].split(',')
        codigos =[
            'cxr89','fhH52','3fgg7','0829g','5jfb2','gca7d','z1zca','12cc9',
            'aa5bc','0820t','1137g','5jf4c','3fg21','z1zbz','08291','2448g',
            '12ct1','61bgg','g5582','12ca9','61bt4','8tz0g','244cd','5jfa0',
            'gcaa3','6zc2f','aa5d4','12cd6','3fg56','om3l4','z2pla','cac31',
            'bi4c0','hig98','77tyx','fuh76','0pp61','iuio9','it552','tig2a',
            '01009','j0a32','m009g','nha55','iHbH7','gg3rs','b2b34','9jgyt',
            'op5H8','x1c47','189hi','omlH7','ad087','ll282','00llH','c475a',
            'k2bbc','a35e9','a3528','04f74','04gff','0094g','00920','ef7d9',
            'ef7e0','gc8b0','c2c51','c2c47','c2c91','0c368','6g7gg','m4175',
            'cop32','32pco','H40i9','ccl22','om675','tjk82','ph908','eli56',
            '29183','292d0','53gd1','53gcg','95767','958c2','958g3','e47bf',
            'c14e3','c1421','c15ed','c15g8','g6e4b','g7wyx','g6e4f','g6e90',
            'a784c','bag58','ba1ba','2f149','2f189','64b01','64cg0','64dfa',
            '887bc','k9k0k','abtur','ciub4','enop9','i7858','cac67','ff650'
        ]
        alfabeto=[
                'ú','Ú','y','r','j','k',' ','f',
                'o','q','a','h','v','ç','p','b',
                'g','s','m','d','t','z','c','i',
                'l','u','n','e','x','w','A','B',
                'C','D','E','F','G','H','I','J',
                'K','L','M','N','O','P','Q','R',
                'S','T','U','V','W','X','Y','Z',
                'Ç',',','.',';','?',':','ã','é',
                'à','á','õ','ó','ê','ô','â','Ã',
                'É','À','Á','Õ','Ó','Ê','Ô','Â',
                '1','2','3','4','5','6','7','8',
                '9','0','+','-','/','\\','*','$',
                '!',']','[','(',')','"','{','}',
                '=',"'",'_','Ç','\n','í','Í','#'
            ]
        if var == ['\n']:
            bot = descript.tela.popup('Nada para descriptografar',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        else:
            for x in var[0:]:
                if x in codigos:
                    posicao = codigos.index(x)
                    #! única diferênca da criptografia
                    #! Aqui é passado a lista de alfabetos e não dos códigos
                    contador += alfabeto[posicao]
            #!Abrindo a janela6 e mostrando o a mensagem que foi descriptografada
            #!Não foi possível usar o elemento Output porque não havia quebra de linha 
            #!Ou seja, as palavras poderiam ficar cortadas por conta da linha
            #!Para resolver isso, o output foi subistituido para o multiline, que ao contrário do Output
            #!Reconhece as plavras e faz a quebra de linha de forma correta
            #!Agora é só passar o parâmetro que é o valor default da multiline
            janela6 = descript.descript(contador)
    #!Limpando a janela de descriptografia passando nada como valor default
    elif window == janela5 and event == 'bot_limpar':
        janela5.Close()
        janela5 = descript.chama('')
    #!Colando os elementos que estavam na área de Transferência
    elif window == janela5 and event == 'Colar':
        var = pyperclip.paste()
        if var == ' ':
            tela.popup('Nada para Colar',icon=img,button_color=['#fff','#1a1a1a'],background_color='#0d0d0d',text_color='#33cc33')
        else:
            janela5.Close()
            janela5 = descript.chama(pyperclip.paste())
                    #!Linux                    #!Windows
    elif event == 'Control_L:36' or event == 'Control_L:17':
        pyperclip.copy('')
        
'''
/**
*Nota de atualização: 3.0
*/
'''
#!Email para envio anônimo(do projeto)
#email: projetop1006@gmail.com
#senha: ,,,ola,mundO,,,

#+  Bibliotecas

#!Uso da smtplib
#https://docs.python.org/3/library/smtplib.html
#https://relaxaeusouti.com.br/2020/03/07/como-enviar-e-mails-com-python-usando-o-smtp/
#https://www.google.com/settings/security/lesssecureapps

#!Informações da PYsimpleGUI
#https://pysimplegui.readthedocs.io/en/latest/

#!Informações da OS
#https://docs.python.org/3/library/os.html?highlight=os#module-os

#!Informações da Platform
#https://docs.python.org/3/library/platform.html?highlight=platform#module-platform

#!Informações do pyperclip
#https://pypi.org/project/pyperclip/

#!Informações do sqlite3
#https://docs.python.org/3/library/sqlite3.html
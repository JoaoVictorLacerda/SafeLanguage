import PySimpleGUI as tela
import os
import platform 
var =os.path.expanduser('~')
cwd = os.getcwd()
if platform.system() == 'Windows':
    img=f'{cwd}\\img\\01.ico'
elif platform.system() =='Linux':
    img = f'{cwd}/img/01.png'


def primeiro():
    #!tela de Login
    tela.change_look_and_feel('DarkTeal4')
    ini=[
        [tela.Text('Usuário', font=('Consolas, 14'),text_color='#33cc33'), tela.Input(key='nome', font=('Consolas, 15'), size=(15, 0),background_color='#1a1a1a',text_color='#33cc33')],
        [tela.Text('Senha  ', font=('Consolas, 14'),text_color='#33cc33'), tela.Input(key='senha',password_char='•', font=('Consolas, 15'), size=(15, 0),background_color='#1a1a1a',text_color='#33cc33')],
        [tela.Button('Login', font=('Consolas, 13'),button_color=['#fff','#1a1a1a'])]
    ]
    return tela.Window(
        'Login',
         return_keyboard_events=True,
          layout=ini,
           icon=img,
            finalize=True)

def segundo(valor_Pad):
    #!tela para digitar a mensagem que seŕa encriptada
    tela.change_look_and_feel('DarkTeal4')
    ini=[
        [tela.Text('Seja bem-vindo', font=('Consolas',20), text_color='#000000', justification='center', size=(53, 0))],
        [tela.Text('Digite a mensagem que será criptografada:', font=('Consolas',20), text_color='#000000', justification='center', size=(53, 0))],
        
        [tela.Text('     Para Descriptografar', font=('Consolas', 20),text_color='#33cc33'),
        tela.Text(' →', font=('Consolas', 25),text_color='#33cc33'),
        tela.Button('Clique Aqui',size=(27, 1), font=('Consolas', 20), key='bot1',button_color=['#fff','#1a1a1a'])],

        [tela.Multiline(valor_Pad,font=("Consolas", 12), size=(90, 23), key='menssagem',background_color='#1a1a1a',text_color='#33cc33')],

        [tela.Button('Criptografar', font=('Consolas',14),button_color=['#fff','#1a1a1a']),
        tela.Button('Limpar', font=('Consolas',14),button_color=['#fff','#1a1a1a']),
        tela.Button('Colar', font=('Consolas', 14), key='Colar2',button_color=['#fff','#1a1a1a']),
        tela.Text('                                             \
                                                '),
        tela.Button('Sair da conta', font=('Consolas', 14),button_color=['#fff','#1a1a1a'])]
    ]
    return tela.Window('Criptografia', 
    return_keyboard_events=True, 
    layout=ini,
    location=(250,20),
    icon=img, 
    finalize=True,)

def terceiro():
    #!tela para devolver os resuktados para os usuários
    tela.change_look_and_feel('DarkTeal4')
    ini =[
        [tela.Output(size=(60, 23),font=('Consolas, 12'), key="out",background_color='#000000',text_color='#33cc33')],
        [tela.Button('Copiar', font=('Consolas, 14'),button_color=['#fff','#1a1a1a']),
        tela.Button('Enviar E-mail',font=('Consoles',14),button_color=['#fff','#1a1a1a'])
        ]
    ] 
    return tela.Window(
        'Resultado',
        return_keyboard_events=True,
        layout=ini,
        location=(400,70),
        icon=img,
        finalize=True)
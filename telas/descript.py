import PySimpleGUI as tela
import os
import platform 
var =os.path.expanduser('~')
cwd = os.getcwd()
if platform.system() == 'Windows':
    img=f'{cwd}\\img\\01.ico'
elif platform.system() =='Linux':
    img = f'{cwd}/img/01.png'

def chama(cont):
    tela.change_look_and_feel('DarkTeal4')
    ini=[
    [tela.Text('Seja bem-vindo', font=('Consolas',20) ,text_color='#000000', justification='center', size=(53, 0))],
    [tela.Text('   Cole o código que será descriptografado:', font=('Consolas',20),text_color='#000000', justification='center', size=(53, 0))],
    [tela.Button('Clique Aqui',size=(27, 1), font=('Consolas', 20),key='bot2',button_color=['#fff','#1a1a1a']), tela.Text(' ←', font=('Consolas', 25),text_color='#33cc33'),tela.Text('Para Criptografar', font=('Consolas', 20),text_color='#33cc33')],
    [tela.Multiline(cont,font=("Consolas", 12), size=(90, 23), key='codigo1',background_color='#1a1a1a',text_color='#33cc33')],
    [tela.Button('Descriptografia', font=('Consolas',14),button_color=['#fff','#1a1a1a']), 
    tela.Button('Limpar',font=('Consolas',14), key= 'bot_limpar',button_color=['#fff','#1a1a1a']),tela.Button('Colar', font =('Consolas', 14),button_color=['#fff','#1a1a1a'])]
    ]
    
    return tela.Window(
    'Descriptografia',
    return_keyboard_events=True, 
    layout=ini,
    location=(250,20),
    icon=img,
     finalize=True)

def descript(valor):
    tela.change_look_and_feel('DarkTeal4')
    init =[
         [tela.Multiline(valor,size=(90, 23),font=("Consolas", 14),background_color='#000000',text_color='#33cc33')],
         [tela.Button('Copiar', font=('Consolas',14 ),button_color=['#fff','#1a1a1a'])]
         
    ]
    return tela.Window(
        'Resultado',
        return_keyboard_events=True,
         layout=init,
         icon=img,
         finalize=True )


def pergunta():
    tela.change_look_and_feel('DarkTeal4')
    init=[
        [tela.Text('Deseja salvar sua conta? ',text_color='#33cc33', font=('Consolas, 14'),justification='center')],
        [tela.Button('SIM', font=('Consolas, 12'),button_color=['#fff','#1a1a1a']),tela.Button('NÃO', font=('Consolas, 12'),button_color=['#fff','#1a1a1a'])]
    ]
    return tela.Window(
        'Salvar',
        return_keyboard_events=True,
         layout=init,
         icon=img,
          finalize=True)

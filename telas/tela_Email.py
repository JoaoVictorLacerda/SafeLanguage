import PySimpleGUI as tela
import os
import platform 
var =os.path.expanduser('~')
cwd = os.getcwd()
if platform.system() == 'Windows':
    img=f'{cwd}\\img\\01.ico'
elif platform.system() =='Linux':
    img = f'{cwd}/img/01.png'

def Email():
    #!tela de Login
    tela.change_look_and_feel('DarkTeal4')
    ini=[
        [tela.Text('PARA:', font=('Consolas, 14'),text_color='#fff'), tela.Input(key='para', font=('Consolas, 15'), size=(25, 0),background_color='#1a1a1a',text_color='#33cc33')],
        [tela.Button('Enviar', font=('Consolas, 12'),button_color=['#fff','#1a1a1a'])]
    ]


    return tela.Window(
        'Enviar Email',
         layout=ini,
         icon=img,
          finalize=True)





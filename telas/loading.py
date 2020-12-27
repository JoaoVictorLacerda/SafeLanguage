import PySimpleGUI as tela 
import os
import platform 
var =os.path.expanduser('~')
cwd = os.getcwd()
if platform.system() == 'Windows':
    img=f'{cwd}\\img\\01.ico'
elif platform.system() =='Linux':
    img = f'{cwd}/img/01.png'

def loading(a):
    tela.change_look_and_feel('DarkTeal4')
    layout = [  [tela.Text(a, font='Consolas 14',justification='center',text_color='#33cc33')],
                [tela. Text('               '),tela.Image(data=tela.DEFAULT_BASE64_LOADING_GIF, key='_IMAGE_')]
            ]

    window = tela.Window(
        'Carregando',
        layout=layout,
        icon=img)
    number = 0
    while True:             # Event Loop
        event,event = window.Read(timeout=25)
        if event == tela.WIN_CLOSED:
            break
        if number == 50:
            break
        window.Element('_IMAGE_').UpdateAnimation(tela.DEFAULT_BASE64_LOADING_GIF,  time_between_frames=30)
        number +=1
    
    return window





from time import *
from tkinter import *
from tkinter import ttk
#---------------- TELA 1 - TELA DE LOGIN -----------------------------
tela = Tk()
tela.title('Login')
tela.geometry('215x150')
tela['bg'] = 'lightgrey'
#tela.iconbitmap('C:/imagens/veolia.ico')
tela.resizable(width=FALSE,height=FALSE)

logins = ['Georges', '1234','Keverny','5678','Luciano','9999'] #VETOR QUE SALVA OS USUARIOS E SENHAS
veiculos = ['Caminhão', 'Trator', 'Poliguindaste'] #VETOR QUE CONTEM OS VEICULOS PARA O LISTBOX
#VETORES QUE RECEBEM AS INFORMAÇÕES DO FORMULARIO
data_relatorio = [] 
veiculo_tipo = []
ano_fabricação = []

data_relatorio2 = []
veiculo_tipo2 = []
ano_fabricação2 = []

data_relatorio3 = []
veiculo_tipo3 = []
ano_fabricação3 = []

def login(): #FUNÇÃO QUE RECEBE OS DADOS PARA FAZER LOGIN
  usu = caixa_usuario.get()
  sen = caixa_senha.get()
#------------- TELA 2 - 1° USUARIO -------------------
  if logins[0] == usu and logins[1] in sen: #SE O USUARIO E A SENHA DIGITADA FOR IGUAL AOS DADOS DA POSIÇÃO INDICADA DO VETOR, SERÁ FEITO O LOGIN E ABRIRA OUTRA JANELA
   login_mensagem['text'] = ''
   sleep(0.5) 
   tela2 = Toplevel(tela) 
   tela2.title('Sistema de Checagem de Manutenção de Veiculos - Tela Inicial')
   tela2.geometry('669x360')
   tela2['bg'] = 'lightgrey'
   #tela2.iconbitmap('C:/imagens/veolia.ico')
   tela2.resizable(width=FALSE,height=FALSE)
   def testagem(): #FUNÇÃO DO BOTÃO "NOVA TESTAGEM"
    def salvar_dados_relatorio():  #FUNÇÃO DO BOTÃO "SALVAR RELATORIO"
      datarel = caixa_data.get() #VARIAVEL QUE COLETA A INFORMAÇÃO
      data_relatorio.append(datarel) #INFORMAÇÃO DA VARIAVEL SENDO COLOCADA NO VETOR 
  
      veicurel = caixa_veiculo.get()
      veiculo_tipo.append(veicurel)
  
      anorel = caixa_ano.get()
      ano_fabricação.append(anorel)
# --------------------- TELA 3 - 1° USUARIO ---------------------
    tela3 = Toplevel(tela2)
    tela3.title('Veolia - Formulario de Checagem')
    tela3['bg'] = 'lightgrey'
    tela3.geometry('404x300')
    #tela3.iconbitmap('C:/imagens/veolia.ico')
    tela3.resizable(width=FALSE,height=FALSE)

    display_usuario = Label(tela3,text='Nome:  GEORGES', bg='#FE570E', width=28, font='bold 9',justify=LEFT)
    display_usuario.grid(row=0,column=0, sticky=W)

    display_veiculo = Label(tela3,text='Placa:  123-ABC',bg='#FE570E', width=28, font='bold 9',justify=LEFT)
    display_veiculo.grid(row=0,column=1)

    data = Label(tela3, text='Data da Nova Testagem',bg='lightgrey',font='bold 9' )
    data.grid(row=1,column=0, pady=10,padx=5, sticky=W)

    caixa_data = Entry(tela3)
    caixa_data.place(x=9,y=55, width=200,height=20)

    veiculo = Label(tela3, text='Tipo de Veiculo', bg='lightgrey',font='bold 9')
    veiculo.grid(row=3,column=0,pady=20,padx=5, sticky=W)
 
    caixa_veiculo = ttk.Combobox(tela3, values=veiculos) #LISTA QUE CONTEM OS VEICULOS QUE SÃO SELECIONAVEIS NO FORMULARIO
    caixa_veiculo.set("Caminhão")
    caixa_veiculo.place(x=9,y=165, width=200,height=20)


    ano = Label(tela3, text='Ano do Veiculo', bg='lightgrey',font='bold 9')
    ano.grid(row=2,column=0,pady=20,padx=5, sticky=W)

    caixa_ano = Entry(tela3)
    caixa_ano.place(x=9,y=110, width=200,height=20)

    enviar_relatorio = Button(tela3, text='Enviar Relatorio', command=salvar_dados_relatorio)
    enviar_relatorio.place(x=25,y=270,width=150, height=25)

    voltar_tela = Button(tela3,text='Voltar', command=tela3.destroy) #A FUNÇÃO "DESTROY" FECHA A PAGINA
    voltar_tela.place(x=220,y=270, width=100, height=25)
 
    relatorio_enviado = Label(tela3,text='',bg='lightgrey', font='bold 9')
    relatorio_enviado.place(x=270,y=40, width=100,height=25)  
#--------------------------- IF TELA 2 - 1° USUARIO -------------------------------
   def relatorio(): #FUNÇÃO DO BOTÃO "VER RELATORIO ANTERIOR"
    if len(data_relatorio) == 0 and len(veiculo_tipo) == 0 and len(ano_fabricação) == 0: #SE O VETORES QUE GUARDAM AS INFORMAÇÕES DOS FORMULARIOS ESTIVEREM VAZIOS, É MOSTRADO UM FORMULARIO VAZIO
     visualizar_relatorio = Label(tela2, text='--------- RELATORIO --------\nDATA DA REALIZAÇÃO: '+ '' +'\nFUNCIONARIO: GEORGES PEREIRA PAIVA\nPLACA DO VEICULO: 123-ABC\nTIPO DE VEICULO: '+''+'\nANO DE FABRICAÇÃO: '+'',width=42, height=12 ,bd=15, bg='#767676',fg='black', justify=CENTER)
     visualizar_relatorio.grid(row=1, column=1,padx=1,pady=63)
    else: #SE TODOS OS VETORES ESTIVEREM PREENCHIDOS, SERÁ MOSTRADO O FORMULARIO AO APERTAR O BOTÃO 
     #D1,V1 e A1 - VARIAVEL QUE TRANSFORMAR AS INFORMAÇÕES GUARDADAS NO VETOR EM TEXTO(Str)
     d1 = str(data_relatorio[0]) 
     v1 = str(veiculo_tipo[0])
     a1 = str(ano_fabricação[0])
     visualizar_relatorio = Label(tela2, text='--------- RELATORIO --------\nDATA DA REALIZAÇÃO: '+ d1 +'\nFUNCIONARIO: GEORGES PEREIRA PAIVA\nPLACA DO VEICULO: 123-ABC\nTIPO DE VEICULO: '+ v1 +'\nANO DE FABRICAÇÃO: '+ a1,width=42, height=12 ,bd=15, bg='#767676',fg='black', justify=CENTER)
     visualizar_relatorio.grid(row=1, column=1,padx=1,pady=63)

   display_usuario = Label(tela2,text='Nome:   GEORGES', bg='#FE570E', width=44, font='bold 9',justify=LEFT)
   display_usuario.grid(row=0,column=0)

   display_veiculo = Label(tela2,text='Placa:  123-ABC',bg='#FE570E', width=50, font='bold 9',justify=LEFT)
   display_veiculo.grid(row=0,column=1)

   botao_testagem = Button(tela2, text='Nova Testagem',command=testagem ,width=15)
   botao_testagem.grid(row=1,column=0, sticky=N,pady=110)

   botao_relatorio = Button(tela2, text='Ver Relatorio Anterior', width=20, command=relatorio)
   botao_relatorio.place(x=80,y=190)

   sair_usuario = Button(tela2,text='Sair',width=15, command=tela2.destroy)
   sair_usuario.place(x=540,y=25) 
#------------- TELA 2 - 2° USUARIO -------------------
  elif logins[2] == usu and logins[3] in sen:
   login_mensagem['text'] = ''
   sleep(0.5) 
   tela2 = Toplevel(tela)
   tela2.title('Sistema de Checagem de Manutenção de Veiculos - Tela Inicial')
   tela2.geometry('669x360')
   tela2['bg'] = 'lightgrey'
   #tela2.iconbitmap('C:/Users/Leandro/Documents/python/trabalhos/imagens/veolia.ico')
   tela2.resizable(width=FALSE,height=FALSE)
   def testagem():
    def salvar_dados_relatorio():  
      datarel2 = caixa_data.get()
      data_relatorio2.append(datarel2)
  
      veicurel2 = caixa_veiculo.get()
      veiculo_tipo2.append(veicurel2)
  
      anorel2 = caixa_ano.get()
      ano_fabricação2.append(anorel2)
# --------------------- TELA 3 - 2° USUARIO ---------------------
    tela3 = Toplevel(tela2)
    tela3.title('Veolia - Formulario de Checagem')
    tela3['bg'] = 'lightgrey'
    tela3.geometry('404x300')
    #tela3.iconbitmap('C:/imagens/veolia.ico')
    tela.resizable(width=FALSE,height=FALSE)

    display_usuario = Label(tela3,text='Nome:   KEVERNY', bg='#FE570E', width=28, font='bold 9',justify=LEFT)
    display_usuario.grid(row=0,column=0, sticky=W)

    display_veiculo = Label(tela3,text='Placa:  456-DEF',bg='#FE570E', width=28, font='bold 9',justify=LEFT)
    display_veiculo.grid(row=0,column=1)

    data = Label(tela3, text='Data da Nova Testagem',bg='lightgrey',font='bold 9' )
    data.grid(row=1,column=0, pady=10,padx=5, sticky=W)

    caixa_data = Entry(tela3)
    caixa_data.place(x=9,y=55, width=200,height=20)

    veiculo = Label(tela3, text='Tipo de Veiculo', bg='lightgrey',font='bold 9')
    veiculo.grid(row=3,column=0,pady=20,padx=5, sticky=W)
 
    caixa_veiculo = ttk.Combobox(tela3, values=veiculos) #LISTA QUE CONTEM OS VEICULOS QUE SÃO SELECIONAVEIS NO FORMULARIO
    caixa_veiculo.set("Caminhão")
    caixa_veiculo.place(x=9,y=165, width=200,height=20)

    ano = Label(tela3, text='Ano do Veiculo', bg='lightgrey',font='bold 9')
    ano.grid(row=2,column=0,pady=20,padx=5, sticky=W)

    caixa_ano = Entry(tela3)
    caixa_ano.place(x=9,y=110, width=200,height=20)

    enviar_relatorio = Button(tela3, text='Enviar Relatorio', command=salvar_dados_relatorio)
    enviar_relatorio.place(x=25,y=270,width=150, height=25)

    voltar_tela = Button(tela3,text='Voltar', command=tela3.destroy) 
    voltar_tela.place(x=220,y=270, width=100, height=25)
 
    relatorio_enviado = Label(tela3,text='',bg='lightgrey', font='bold 9')
    relatorio_enviado.place(x=270,y=40, width=100,height=25)   
#--------------------------- IF TELA 2 - 2° USUARIO -------------------------------
   def relatorio():
    if len(data_relatorio2) == 0 and len(veiculo_tipo2) == 0 and len(ano_fabricação2) == 0:
     visualizar_relatorio = Label(tela2, text='--------- RELATORIO --------\nDATA DA REALIZAÇÃO: '+ '' +'\nFUNCIONARIO: KEVERNY SOUSA DO NASCIMENTO\nPLACA DO VEICULO: 456-DEF\nTIPO DE VEICULO: '+''+'\nANO DE FABRICAÇÃO: '+'',width=42, height=12 ,bd=15, bg='#767676',fg='black', justify=CENTER)
     visualizar_relatorio.grid(row=1, column=1,padx=1,pady=63)
    else:
     d2 = str(data_relatorio2[0])
     v2 = str(veiculo_tipo2[0])
     a2 = str(ano_fabricação2[0])
     visualizar_relatorio = Label(tela2, text='--------- RELATORIO --------\nDATA DA REALIZAÇÃO: '+ d2 +'\nFUNCIONARIO: KEVERNY SOUSA DO NASCIMENTO\nPLACA DO VEICULO: 456-DEF\nTIPO DE VEICULO: '+ v2 +'\nANO DE FABRICAÇÃO: '+ a2,width=42, height=12 ,bd=15, bg='#767676',fg='black', justify=CENTER)
     visualizar_relatorio.grid(row=1, column=1,padx=1,pady=63)

   display_usuario = Label(tela2,text='Nome:   KEVERNY', bg='#FE570E', width=44, font='bold 9',justify=LEFT)
   display_usuario.grid(row=0,column=0)

   display_veiculo = Label(tela2,text='Placa:  456-DEF',bg='#FE570E', width=50, font='bold 9',justify=LEFT)
   display_veiculo.grid(row=0,column=1)

   botao_testagem = Button(tela2, text='Nova Testagem',command=testagem ,width=15)
   botao_testagem.grid(row=1,column=0, sticky=N,pady=110)

   botao_relatorio = Button(tela2, text='Ver Relatorio Anterior', width=20, command=relatorio)
   botao_relatorio.place(x=80,y=190)

   sair_usuario = Button(tela2,text='Sair',width=15, command=tela2.destroy)
   sair_usuario.place(x=540,y=25)
#------------- TELA 2 - 3° USUARIO -------------------
  elif logins[4] == usu and logins[5] in sen:
   login_mensagem['text'] = ''
   sleep(0.5) 
   tela2 = Toplevel(tela)
   tela2.title('Sistema de Checagem de Manutenção de Veiculos - Tela Inicial')
   tela2.geometry('669x360')
   tela2['bg'] = 'lightgrey'
   #tela2.iconbitmap('C:/imagens/veolia.ico')
   tela2.resizable(width=FALSE,height=FALSE)

   def testagem():
    def salvar_dados_relatorio():  
      datarel3 = caixa_data.get()
      data_relatorio3.append(datarel3)
  
      veicurel3 = caixa_veiculo.get()
      veiculo_tipo3.append(veicurel3)
  
      anorel3 = caixa_ano.get()
      ano_fabricação3.append(anorel3)
# --------------------- TELA 3 - 3° USUARIO ---------------------
    tela3 = Toplevel(tela2)
    tela3.title('Veolia - Formulario de Checagem')
    tela3['bg'] = 'lightgrey'
    tela3.geometry('404x300')
    #tela3.iconbitmap('C:/imagens/veolia.ico')
    tela3.resizable(width=FALSE,height=FALSE)

    display_usuario = Label(tela3,text='Nome:   LUCIANO', bg='#FE570E', width=28, font='bold 9',justify=LEFT)
    display_usuario.grid(row=0,column=0, sticky=W)

    display_veiculo = Label(tela3,text='Placa:  789-GHI',bg='#FE570E', width=28, font='bold 9',justify=LEFT)
    display_veiculo.grid(row=0,column=1)

    data = Label(tela3, text='Data da Nova Testagem',bg='lightgrey',font='bold 9' )
    data.grid(row=1,column=0, pady=10,padx=5, sticky=W)

    caixa_data = Entry(tela3)
    caixa_data.place(x=9,y=55, width=200,height=20)

    veiculo = Label(tela3, text='Tipo de Veiculo', bg='lightgrey',font='bold 9')
    veiculo.grid(row=3,column=0,pady=20,padx=5, sticky=W)
 
    caixa_veiculo = ttk.Combobox(tela3, values=veiculos) #LISTA QUE CONTEM OS VEICULOS QUE SÃO SELECIONAVEIS NO FORMULARIO
    caixa_veiculo.set("Caminhão")
    caixa_veiculo.place(x=9,y=165, width=200,height=20)

    ano = Label(tela3, text='Ano do Veiculo', bg='lightgrey',font='bold 9')
    ano.grid(row=2,column=0,pady=20,padx=5, sticky=W)

    caixa_ano = Entry(tela3)
    caixa_ano.place(x=9,y=110, width=200,height=20)

    enviar_relatorio = Button(tela3, text='Enviar Relatorio', command=salvar_dados_relatorio)
    enviar_relatorio.place(x=25,y=270,width=150, height=25)

    voltar_tela = Button(tela3,text='Voltar', command=tela3.destroy)
    voltar_tela.place(x=220,y=270, width=100, height=25)
 
    relatorio_enviado = Label(tela3,text='',bg='lightgrey', font='bold 9')
    relatorio_enviado.place(x=270,y=40, width=100,height=25)  
#--------------------------- IF TELA 2 - 3° USUARIO -------------------------------
   def relatorio():
    if len(ano_fabricação3) == 0 and len(veiculo_tipo3) == 0 and len(ano_fabricação3) == 0:
     visualizar_relatorio = Label(tela2, text='--------- RELATORIO --------\nDATA DA REALIZAÇÃO: '+ '' +'\nFUNCIONARIO: ANTONIO LUCIANO BANDEIRA\nPLACA DO VEICULO: 789-GHI\nTIPO DE VEICULO: '+''+'\nANO DE FABRICAÇÃO: '+'',width=42, height=12 ,bd=15, bg='#767676',fg='black', justify=CENTER)
     visualizar_relatorio.grid(row=1, column=1,padx=1,pady=63)
    else:
     d3 = str(ano_fabricação3[0])
     v3 = str(veiculo_tipo3[0])
     a3 = str(ano_fabricação3[0])
     visualizar_relatorio = Label(tela2, text='--------- RELATORIO --------\nDATA DA REALIZAÇÃO: '+ d3 +'\nFUNCIONARIO: ANTONIO LUCIANO BANDEIRA\nPLACA DO VEICULO: 789-GHI\nTIPO DE VEICULO: '+ v3 +'\nANO DE FABRICAÇÃO: '+ a3,width=42, height=12 ,bd=15, bg='#767676',fg='black', justify=CENTER)
     visualizar_relatorio.grid(row=1, column=1,padx=1,pady=63)

   display_usuario = Label(tela2,text='Nome:   LUCIANO', bg='#FE570E', width=44, font='bold 9',justify=LEFT)
   display_usuario.grid(row=0,column=0)

   display_veiculo = Label(tela2,text='Placa:  789-GHI',bg='#FE570E', width=50, font='bold 9',justify=LEFT)
   display_veiculo.grid(row=0,column=1)

   botao_testagem = Button(tela2, text='Nova Testagem',command=testagem ,width=15)
   botao_testagem.grid(row=1,column=0, sticky=N,pady=110)

   botao_relatorio = Button(tela2, text='Ver Relatorio Anterior', width=20, command=relatorio)
   botao_relatorio.place(x=80,y=190)

   sair_usuario = Button(tela2,text='Sair',width=15, command=tela2.destroy)
   sair_usuario.place(x=540,y=25)
  else: #SE NENHUM USUARIO E SENHA FOR DIGITADO, OU USUARIO E SENHA FOR ESCRITO ERRADO, APARECERÁ UMA MENSAGEM DE ERRO
   login_mensagem['text'] = f'''
   Usuario ou Senha Incorreto
   '''
logo = Label(tela,text='Veolia - Login de Usuario',width=30,bg='#FE570E',font='bold 9', justify=CENTER)
logo.grid(rowspan=1,column=0,pady=1,sticky=N)

usuario = Label(tela,text='Usuario:',width=0, bg='lightgrey',font='bold 9')
usuario.grid(row=2,column=0,sticky=W)
senha = Label(tela,text='Senha:',width=0, bg='lightgrey',font='bold 9')
senha.grid(row=3, column=0,sticky=W)

caixa_usuario = Entry(tela, width=26, justify=LEFT)
caixa_usuario.grid(row=2,column=0,sticky=E,padx=4,pady=2)

caixa_senha = Entry(tela,width=27,justify=LEFT,show='*')
caixa_senha.grid(row=3,column=0,sticky=E,padx=4,pady=1)

login_botao = Button(tela, text='Login', width=5, command=login)
login_botao.grid(row=4,column=0,sticky=E,padx=5,pady=2)

login_mensagem = Label(tela, text='',width=27, height=2,justify=CENTER, background='lightgrey')
login_mensagem.place(x=10,y=100)

tela.mainloop()

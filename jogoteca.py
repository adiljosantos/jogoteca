
from flask import Flask, render_template,request, redirect,session, flash, url_for

class Jogo:                 #   criamos a classe jogo
    def __init__(self, nome, categoria, console):      #    definimos os parametros
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris','Puzzi','Atari')              #    criamos o objeto jogo1 com os atributos
jogo2 = Jogo('God of War','Rack n Slash','PS2')     #    criamos o objeto jogo2 com os atributos
jogo3 = Jogo('Mortal Combat','luta','PS2')
lista = [jogo1,jogo2,jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Adilson", "adilson", "1234")
usuario2 = Usuario("Camila", "mila", "4567")
usuario3 = Usuario("Rayann", "rayann", "rayann")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }

app = Flask(__name__)       #   necesario para iniciar a aplicação
app.secret_key = 'Alura'


@app.route('/')         #   criamos uma nova rota para login do usuario
def login():
    return render_template('login.html')

@app.route('/login')             #   é necessario criar uma rota inicial para a aplicação
def index():                  #   criamos uma função
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você precisa estar logado para acessar esta página!')
        return redirect('/login')
                            #   essa função irá retornar o conteudo para ser exibido na página
                            #   o render _template envia a saida da função (variaveis) para a página de destino  

@app.route('/home')             #   é necessario criar uma rota inicial para a aplicação
def home():                  #   criamos uma função
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você precisa estar logado para acessar esta página!')
        return redirect('/login')
    return render_template('lista.html', titulo='Jogos Cadastrados')


@app.route('/novo')         #   criamos uma nova rota para abir a tela para cadastrar um novo jogo
def novoJogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Você precisa estar logado para acessar esta página!')
        return redirect('/login')

    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])       #  criamos uma nova rota para processar o cadastro de um novo jogo no servidor
                                              #  É PRECISO INFORMAR QUE O METODO É POST
                                              #  por padrão o flask considera todas as rotas como sendo do metodo GET nós precisamos
                                              #  informar que esta rota é do tipo POST
def criarJogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)       #   criamos um objeto que contém os atributos enviadas pelo formulario
    lista.append(jogo)      #   adicionamos as informações no final da lista
    return render_template('lista.html', titulo='Jogos Cadastrados', jogos=lista)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            return redirect('/home')
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')         #   criamos uma nova rota para o logout
def logout():
    session['usuario_logado'] = None
    flash(' logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)     #  ativamos o debug para não ser preciso ficar dando o comando run toda vez que fizermos uma alteração no código
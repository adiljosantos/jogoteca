from flask import Flask, render_template,request, redirect

class Jogo:                 #   criamos a classe jogo
    def __init__(self, nome, categoria, console):      #    definimos os parametros
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris','Puzzi','Atari')              #    criamos o objeto jogo1 com os atributos
jogo2 = Jogo('God of War','Rack n Slash','PS2')     #    criamos o objeto jogo2 com os atributos
jogo3 = Jogo('Mortal Combat','luta','PS2')
lista = [jogo1,jogo2,jogo3]

app = Flask(__name__)       #   necesario para iniciar a aplicação

@app.route('/')             #   é necessario criar uma rota inicial para a aplicação
def index():                  #   criamos uma função
                            #   essa função irá retornar o conteudo para ser exibido na página
                            #   o render _template envia a saida da função (variaveis) para a página de destino  
    return render_template('lista.html', titulo='Jogos', jogos=lista)   

@app.route('/novo')         #   criamos uma nova rota para abir a tela para cadastrar um novo jogo
def novoJogo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])        #   criamos uma nova rota para processar o cadastro de um novo jogo no servidor
                                              #   por padrão o flask considera todas as rotas como sendo do metodo GET nós precisamos
                                              #  informar que esta rota é do tipo POST
def criarJogo():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)       #   criamos um objeto que contém os atributos enviadas pelo formulario
    lista.append(jogo)      #   adicionamos as informações no final da lista

    return redirect('/')

app.run(debug=True)     #  ativamos o debug para não ser preciso ficar dando o comando run toda vez que fizermos uma alteração no código
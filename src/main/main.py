# -*- coding: utf-8 -*-

'''
Arquivo: main.py
Descricao: exercicio de fixação do curso de Python/PyQt
Autor: Vanessa Espíndola
Data: março de 2022
'''

# abrir e sair da aplicação
import sys
# carregar o arquivo .ui
from PyQt5 import uic
# ...
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
# manipular arquivo externo
from minhas_funcoes import abrir_exibir_arquivo
from minhas_funcoes import salvar_inserir_dados_em_arquivo


class JanelaFilha(QMainWindow):
	'''
		Janela filha, com os componentes:
			caixa de texto: lineEdit_texto
			combobox: comboBox_automoveis
			checkbox: checkBox_marcar
			botão: pushButton_abrir
			botão: pushButton_salvar
	'''

	def __init__(self, *args, **kwargs):
		super(JanelaFilha, self).__init__(*args, **kwargs)
		self.janela = uic.loadUi('resources/ui/new_window.ui', self)
		self.janela.pushButton_abrir.clicked.connect(self.abrir_arquivo)
		self.janela.pushButton_salvar.clicked.connect(self.salvar_arquivo)
		self.show()

	def abrir_arquivo(self):
		# coleta os conteudos no arquivo
		conteudo_caixa_de_texto, conteudo_combobox, conteudo_checkbox = abrir_exibir_arquivo("resources/arquivo.txt")
		# aplicando conteudo na parte de texto
		self.janela.lineEdit_texto.setText(conteudo_caixa_de_texto)
		# aplicando o conteudo no comobox
		self.janela.comboBox_automoveis.setCurrentText( conteudo_combobox.strip('\n'))
		# apicando o conteudo no checkbox
		if '0' in conteudo_checkbox:
			self.janela.checkBox_marcar.setChecked(False)
		else:
			self.janela.checkBox_marcar.setChecked(True)

	def salvar_arquivo(self):
		# coleta o conteudo da caixa de texto
		li = self.janela.lineEdit_texto.text()
	    # coleta o conteudo do comboBox
		co = self.janela.comboBox_automoveis.currentText()
		# coleta o conteudo do checkbox
		ch = self.janela.checkBox_marcar.checkState()
		dados = [li,co,str(ch)]
		# aplica os conteudos no arquivo
		salvar_inserir_dados_em_arquivo("resources/arquivo.txt", dados)


class JanelaPai(QMainWindow):
	'''
		Janela com menu superior
		com a opção no menu de abrir a janela filha
	'''
	def __init__(self):
		super(JanelaPai,self).__init__()

		# menu superior
		opt_new_window = QAction('&Nova janela', self)
		opt_new_window.triggered.connect(self.new_window)
		menu = self.menuBar().addMenu('&Menu')
		menu.addAction(opt_new_window)

		self.setWindowTitle('Exercício') 
		self.show()

	def new_window(self):
		JanelaFilha(self)


# iniciar aplicação		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = JanelaPai()
	sys.exit(app.exec())

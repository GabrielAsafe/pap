import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
import os  #para ver o caminho das imagens
import time #gera o nome para a imagem no salvamento


#definição de valores para variável global


def inicio():
	global check
	global caminho
	global TodasAsImagens
	check = 0
	caminho= "C:/PicShifter/"
	TodasAsImagens = os.listdir(caminho)
	print("HELP para mostrat a lista de funções\n\n")


def help():
	pal = ["ler 1","resize 2","toRgb 3","cinza 4", "desenhar1 (Estamos trabalhando na implementação)", "Hflip 5", "Vflip 6", "rotacao 7", "ver 8", "salvar 9","opc 10"]
	print(pal[:],"\n\n")

def ler():
	"""A função ler carrega uma imagem para o programa, permitindo que as alterações desejadas sejam feitas """
	global imagem
	global imagemComCores
	global check
	global caminho
	global TodasAsImagens
	#variáveis	
	extensao = input("introduza a extensão da imagem: \n")
	nome = input("introduza o nome da imagem(as imagens devem estar na pasta PicShifter no disco C):\n")
	nomeExtensao = nome+"."+extensao
	resultado = caminho+nome+"."+extensao		
	#checagem de imagens na pasta
	#fim das variáveis

	for file in os.listdir(caminho):
		if nomeExtensao == file:
			check = 1
	if check == 1:		
		imagem = cv.imread(resultado)#le a imagem em bgr. normalmente n�o vale a pena converter pra rgb
		imagemComCores = cv.imread(resultado)
		print("Imagem carregada com sucesso")
		
	else:
		print("A imagem não existe na pasta do programa")


def resize(x,y):
	"""A função resize, usada após a função ler, permite que altere as dimensões da imagem """
	global imagem
	global imagemComCores
	global check
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem = cv.resize(imagem,(x,y)) #transformação morfológica
		imagemComCores = cv.resize(imagem,(x,y)) #transformação morfológica
		cv.imshow("imagem",imagem)
		cv.waitKey(0)

def toRgb():
	"""A função toRgb faz a conversão de cores BGR para RGB, utilizando a/as imagem/imagens selecionadas na função ler   """
	global imagem

	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem = cv.cvtColor(imagem,cv.COLOR_BGR2RGB) #transformação morfológica
		cv.imshow("imagem",imagem)
		cv.waitKey(0)

def cinza():
	"""A função cinza faz a conversão de cores BGR para tons de cinza """
	global imagem
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY) #transformação morfológica
		cv.imshow("imagem",imagem)
		cv.waitKey(0)


def Hflip():
	"""A função Hflip gira a imagem na horizontal"""
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO

	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem= cv.flip(imagem,1)
		cv.imshow('Result', imagem)
		cv.waitKey(0)
		cv.destroyAllWindows()


def Vflip():
	"""A função Vflip gira a imagem na vertical """
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO	
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem= cv.flip(imagem,0) #transformação morfológica
		cv.imshow('Result', imagem)
		cv.waitKey(0)
		cv.destroyAllWindows()


def rotacao():
	"""A função rotacao faz a imagem dar um backflip ou front, de rotacionar pra frente """
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO
	global teste
	def x(n):
		pass

	def rodar(a,b): #pega o nome da imagem e os valores da TB
		global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
		global teste 
		h, w = a.shape[:2] #pega as dimensões da imagem para fazer a rotação pelo centro dela
		M = cv.getRotationMatrix2D((int(w/2), int(h/2)), angulo, 1)#centro da imagem em H e W, ângulo, escala da imagem
		a = cv.warpAffine(a, M, (w, h))
		teste = a 
		
		cv.imshow('imagem', a)
	cv.namedWindow("Rotação")		
	cv.createTrackbar("Ângulo","Rotação",0 ,360,x)
	while(1):			
		angulo = cv.getTrackbarPos("Ângulo","Rotação")
		rodar(imagem, angulo) 		
		if cv.waitKey(1) & 0xFF == ord('q'):
			imagem = teste
			cv.destroyAllWindows()
			break


def ver():
	""" Essa função mostra a imagem guardada em na variavel IMAGEM que o usuário escolheu com a função 'ver' """
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO
	global check
	
	if check == 1:
		while(1):
			cv.imshow("imagem",imagem)
			if cv.waitKey(1) & 0xFF == ord('q'):
				cv.destroyAllWindows()
				break
				
				
	else:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")



def desfazer():
	""" Essa função deveria pegar as alterações feitas, que foram guardadas numa lista, e restaurar a ultima delas. funciona como uma linha do tempo no paint3D"""
	a


def limpar():
	""" Essa função devera limpar a tela do CMD do meu programa mas não funciona então fds """
	os.system('cls')

def salvar():
	""" Essa função salva a imagem"""
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		extensao = input("Introduza a extensão da imagem:\n")
		segundos = time.time()
		nome = str(segundos)+"."+extensao
		caminho= "C:/PicShifter/"
		completo = caminho+nome
		cv.imwrite(completo, imagem) #salva a imagrm na pasta do projeto
		print(f"Salvamento feito com sucesso\nO nome da imagem é {nome} ")

def MostrarOpcoes():
	global caminho
	for file in os.listdir(caminho):
		print(file)
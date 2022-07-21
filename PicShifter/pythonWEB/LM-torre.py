import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import time #gera o nome para a imagem no salvamento
import pyautogui, sys #posicionamento do mouse
from PIL import Image #função de HSV

 


"""
todo o código ta fazendo as leituras de uma global imagem mas ela altera sempre essa global. acho que seria melhor ela ser da lista de imagens
mas isso vai dar um trabalho do krlh

a estrutura do programa ta assim
le a imagem
mostra a imagem com mostrar()
auxArray.insert(0,codigosDeAlteracoes[0])#aux para saber quais transformações foram feitas nas imagem como medida de controle
insere ela na linha do tempo com insercão()



"""

#----------------------------------------------------------rotinas----------------------------------------------------------------------------

def inicio():
	global check
	global caminho
	global TodasAsImagens#lista todas as imagens usando a biblioteca OS	
	global imgArray#guarda a imagem com a alteração feita
	global auxArray#guarda o código da alteração feita
	global foiCinza #isso é para checar se a imagem foi trasnformada em cinza. caso sim o 11 não funciona
	global codigosDeAlteracoes #códigos das alterações feitas


	codigosDeAlteracoes = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
	foiCinza = False
	imgArray = []
	auxArray = []
	check = 0
	novapasta()
	drawing = False # true if mouse is pressed
	ix,iy = -1,-1 #variável usada no crop
	caminho= "C:/PicShifter"
	TodasAsImagens = os.listdir(caminho)
	print("HELP para mostrat a lista de funções\n")


def novapasta():
	directory = "PicShifter/"  
	parent_dir = "C:/" 
	path = os.path.join(parent_dir, directory)
	try:
		# Create target Directory
		os.mkdir(path)
	except FileExistsError:
		pass     


def mostrar():			
		while(1):
			cv.imshow("imagem",imagem)
			if cv.waitKey(1) & 0xFF == ord('q'):
				cv.destroyAllWindows()
				break

def mostrarcustom():	#função utilizada em efeitos para mostrar as saidas das imagens		
		while(1):
			cv.imshow(nomeSaida,saida)
			if cv.waitKey(1) & 0xFF == ord('q'):
				cv.destroyAllWindows()
				break

def salvarCustom(): #função utilizada em efeitos para salvar as saidas das imagens
	global salvar
	global imagem
	global imgArray

	salvar = input("Deseja salvar a alteração na imagem ? (s/n) \n")
	if salvar == "s":
		imagem = saida
		insercao()
		print("Efeito associado a imagem")
	else:
		pass


def insercao(): 
	""" Insere as imagens em uma lista. Essa á a função que permite que possamos 'desfazer' as alteração indesejadas numa imagem"""
	global imgArray
	global imagem
	imgArray.insert(0,imagem)#colocando elemento em posição expecífica


def checkagemDealteracoes():
	""" essa função é para checar se a imagem foi transformada em cinza em algum momento. isso é para a função clarear funcionar"""
	global foiCinza
	global auxArray
	tam = len(auxArray)
	for i in range(tam):
		if auxArray[i] == codigosDeAlteracoes[3]:
			foiCinza = True
			break
		else:
			foiCinza = False
			break


def exec():
	#https://www.horadecodar.com.br/2020/04/22/como-criar-um-executavel-com-python-exe/
	#esse foi o unico link que fez um executável do programa. fica tudo no dist
	a

#funções 
#----------------------------------------------------------funções de aplicação----------------------------------------------------------------------------

def help():
	pal = [
		"ler ou 1: A função ler carrega uma imagem para o programa, permitindo que as alterações desejadas sejam feitas.",
		"resize ou 2: A função resize, usada após a função ler, permite que altere as dimensões da imagem.",
		"toRgb ou 3: A função toRgb faz a conversão de cores BGR para RGB, utilizando a imagem selecionadas na função ler.",
		"cinza ou 4: A função cinza faz a conversão de cores BGR para tons de cinza.",
		"Hflip ou 5: A função Hflip gira a imagem na horizontal.", 
		"Vflip ou 6: A função Vflip gira a imagem na Vertical.", 
		"rotacao ou 7: A função rotacao faz a imagem dar um back/ frontflip.", 
		"ver ou 8: Essa função permite ao utilizador ver a imagem que selecionou com a função 'ler'.", 
		"salvar ou 9: Essa função permite salvar as imagens após serem alteradas.",
		"MinhasImagens ou 10: Essa função mostra as imagens que estão guardadas na pasta PicShifter no disco C.",
		"hsv ou 11: Essa função serve para aumentar o brilho e a saturação da imagem(em teoria).",
		"desfazer ou 12: Essa função retira a alteração poesteriormente feitas a imagem.",
		"Vcustom ou 13:Essa função permite que o utilizador vaja em uma linha do tempo, todas as alterações que fez até o momento.", 
		"info: Mostra informações sobre a imagem carregada.",
		"x: Fecha o programa",
		"q: Quando a janela de exibição de imagem aparecer e não fechar no botão fechar, no canto superior direito, ela é fechada no 'q' "]
	
	for i in range(len(pal)):
		print("\n")
		print("+","-----------------------------------------------------------------------------------------------------------------","+")
		print("+",pal[i])
		print("+","-----------------------------------------------------------------------------------------------------------------","+")


def ler():
	"""A função ler carrega uma imagem para o programa, permitindo que as alterações desejadas sejam feitas """
	global imagem #importa isso aqui para conseguir guardar uma nova imagem 
	global check #importa isso aqui para o controle se foi ou não adicionada 
	global caminho #importa isso aqui para saber onde procurar as imagens 
	global TodasAsImagens #importa isso aqui para uma comparação de checagem de funcionamento 
	global auxArray #importa isso aqui para saber que essa função já foi usada uma vez

	global resultado
		
	tam = len(auxArray)
	if tam>0:
		for i in range(tam):
			if auxArray[i] == codigosDeAlteracoes[0]:
				pergunta=input("Uma imagem já foi adicionada. Deseja subscrever a imagem já existente ? (responda s ou n)\n")
				
				if pergunta == "s":

					nome = input("introduza o nome da imagem(as imagens devem estar na pasta PicShifter no disco C):\n")
					extensao = input("introduza a extensão da imagem sem o ponto: \n")	
					nomeExtensao = nome+"."+extensao
					resultado = caminho+"/"+nomeExtensao
					for file in os.listdir(caminho):
						if nomeExtensao == file:
							check = 1
							break
						else:
							check = 0
					if check == 1:		
			
						imagem = cv.imread(resultado)#le a imagem em bgr. normalmente n�o vale a pena converter pra rgb
						imagemComCores = cv.imread(resultado,0)
		
						auxArray.insert(0,codigosDeAlteracoes[0])#aux para saber quais transformações foram feitas nas imagem como medida de controle
						insercao()
						print("Imagem carregada com sucesso")
					else:
						print("A imagem não existe na pasta do programa")

				else:
					break
			
	else: #se o código de inserção de imagem não for achado no meu trem de inserção de imagem ele vai executar essa parte do código
		nome = input("introduza o nome da imagem(as imagens devem estar na pasta PicShifter no disco C):\n")
		extensao = input("introduza a extensão da imagem: \n")	
		nomeExtensao = nome+"."+extensao
		resultado = caminho+"/"+nomeExtensao
	
			
		for file in os.listdir(caminho):
			if nomeExtensao == file:
				check = 1
				break
			else:
				check = 0

		if check == 1:		
			imagem = cv.imread(resultado)#le a imagem em bgr. normalmente n�o vale a pena converter pra rgb
			imagemComCores = cv.imread(resultado,0)
		
			auxArray.insert(0,codigosDeAlteracoes[0])#aux para saber quais transformações foram feitas nas imagem como medida de controle
			insercao()
			print("Imagem carregada com sucesso")
		else:
			print("A imagem não existe na pasta do programa")



def resize(x,y):
	"""A função resize, usada após a função ler, permite que altere as dimensões da imagem """
	global imagem
	global check
	global auxArray
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem = cv.resize(imagem,(x,y)) #transformação morfológica
		auxArray.insert(0,codigosDeAlteracoes[1])#aux para saber quais transformações foram feitas nas imagem como medida de controle
		insercao()
		mostrar()
						

def toRgb():
	"""A função toRgb faz a conversão de cores BGR para RGB, utilizando a imagem selecionadas na função ler   """
	global imagem
	global check
	global auxArray
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem = cv.cvtColor(imagem,cv.COLOR_BGR2RGB) #transformação morfológica
		auxArray.insert(0,codigosDeAlteracoes[2])#aux para saber quais transformações foram feitas nas imagem como medida de controle
		insercao()
		mostrar()

def cinza():
	"""A função cinza faz a conversão de cores BGR para tons de cinza """
	global imagem
	global foiCinza
	global auxArray
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY) #transformação morfológica
		auxArray.insert(0,codigosDeAlteracoes[3])
		foiCinza = True
		insercao()
		mostrar()
		


def Hflip():
	"""A função Hflip gira a imagem na horizontal"""
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO
	global auxArray
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		auxArray.insert(0,codigosDeAlteracoes[4])
		imagem= cv.flip(imagem,1)
		insercao()
		mostrar()


def Vflip():
	"""A função Vflip gira a imagem na vertical """
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global auxArray
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		imagem= cv.flip(imagem,0) #transformação morfológica
		auxArray.insert(0,codigosDeAlteracoes[5])
		insercao()
		mostrar()


def rotacao():
	"""A função rotacao faz a imagem dar um backflip ou front, de rotacionar pra frente """
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:	
		global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
		global auxArray #auxArray.insert(0,codigosDeAlteracoes[6])
	
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
				insercao()
				auxArray.insert(0,codigosDeAlteracoes[6])
				cv.destroyAllWindows()
				break


def ver():
	""" Essa função permite ao utilizador ver a imagem que selecionou com a função 'ler'"""
	if check == 1:
		while(1):
			cv.imshow("imagem",imagem)
			if cv.waitKey(1) & 0xFF == ord('q'):
				cv.destroyAllWindows()
				break				
	else:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")

def salvar():
	""" Essa função permite salvar as imagens após serem alteradas"""
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		extensao = input("Introduza a extensão da imagem(png/jpg):\n")
		segundos = time.time()
		nome = str(segundos)+"."+extensao
		caminho= "C:/PicShifter/"
		completo = caminho+nome
		cv.imwrite(completo, imagem) #salva a imagrm na pasta do projeto
		print(f"Salvamento feito com sucesso\nO nome da imagem é {nome} ")


def MostrarOpcoes():
	"""Essa função mostra as imagens que estão guardadas na pasta PicShifter no disco C"""
	for file in os.listdir(caminho):
		print(file)

def clarear():
	global imgArray#guarda a imagem com a alteração feita
	global auxArray#guarda o código da alteração feita
	global imagem
	global resultado
	global imagem1,imagem2,imagem3,imagem4,imagem5
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		image = Image.open(resultado)
		# Filter
		def truncate(x):
				'''makes sure returned value is between 0 and 255'''
				return min(255, max(0, x))

		def cinza(image):
			global imagem1,imagem2,imagem3,imagem4,imagem5
			width, height = image.size
			new_image = Image.new("RGB", (width, height), "white")
			print("Estamos trabalhando nas alterações. Aguarde")
			# Grayscale filter
			for x in range(width):
				for y in range(height):
					r, g, b = image.getpixel((x, y))        
					# New pixel colors
					r_ = g_ = b_ = (r+g+b)/3
					# Change new pixel
					new_pixel = (int(r_), int(g_), int(b_))
					new_image.putpixel((x, y), new_pixel)
			imagem1 = new_image

		def brilho(image):
			global imagem1,imagem2,imagem3,imagem4,imagem5
			# Get image dimesions
			width, height = image.size
			# Create a white RGB image
			new_image = Image.new("RGB", (width, height), "white")
			# Filter magic happens here
			# Brightness filter -64 a +64
			d= input("introduza um valor entre - 64 e + 64 (brilho)\n")
			d = int(d)
			print("Estamos trabalhando nas alterações. Aguarde")
			# Brightness filter
			for x in range(width):
					for y in range(height):
						r, g, b = image.getpixel((x, y))

						# d is the brightness increase
						r_ = truncate(r + d)
						g_ = truncate(g + d)
						b_ = truncate(b + d)

						new_pixel = (int(r_), int(g_), int(b_))
						new_image.putpixel((x, y), new_pixel)
			imagem3 = new_image

		def contraste(image):
			global imagem1,imagem2,imagem3,imagem4,imagem5
			# Get image dimesions
			width, height = image.size
			# Create a white RGB image
			new_image = Image.new("RGB", (width, height), "white")
			# Filter magic happens here  
			#contraste -100 a +100
			# Converting image into a numpy array with a dimension (width, height, 3)
			data = np.array(image)
			beta= input("introduza um valor entre - 100 e + +100(contraste)\n")
			beta = int(beta)
			print("Estamos trabalhando nas alterações. Aguarde")
			# Calculate average brightness
			μ = np.mean(data, axis=2)
			μ_mean = μ.mean()

			# Calculate factor
			if beta == 255: alpha = np.infty
			else: alpha = (255+beta)/(255-beta)

			for x in range(width):
				for y in range(height):
					r, g, b = image.getpixel((x, y))
					r_ = truncate(alpha*(r - μ_mean) + μ_mean)
					g_ = truncate(alpha*(g - μ_mean) + μ_mean)
					b_ = truncate(alpha*(b - μ_mean) + μ_mean)

					new_pixel = (int(r_), int(g_), int(b_))
					new_image.putpixel((x, y), new_pixel)
			imagem2 = new_image

		def saturacao(image):
			global imagem1,imagem2,imagem3,imagem4,imagem5
			# Get image dimesions
			width, height = image.size

			# Create a white RGB image
			new_image = Image.new("RGB", (width, height), "white")

			# Filter magic happens here
			#saturação -100 a +100
			# Calculate factor
			betas= input("introduza um valor entre - 100 e + +100(saturação)\n")
			betas = int(beta)
			print("Estamos trabalhando nas alterações. Aguarde")
			if beta == 255: alpha = np.infty
			else: alpha = (255+betas)/(255-betas)

			for x in range(width):
				for y in range(height):
					r, g, b = image.getpixel((x, y))

					μ = (r+g+b)/3

					r_ = truncate(alpha*(r - μ) + μ)
					g_ = truncate(alpha*(g - μ) + μ)
					b_ = truncate(alpha*(b - μ) + μ)

					new_pixel = (int(r_), int(g_), int(b_))
					new_image.putpixel((x, y), new_pixel)
			imagem4 = new_image

		def gamma(image):
			global imagem1,imagem2,imagem3,imagem4,imagem5
			# Get image dimesions
			width, height = image.size
			# Create a white RGB image
			new_image = Image.new("RGB", (width, height), "white")
			# Filter magic happens here
			#gamma correction 0.33, 0.66, 1.00, 1.33, 1.66 and 2
			gamma= input("introduza um dos seguintes valores: 0.33, 0.66, 1.00, 1.33, 1.66 and 2(gamma)\n")
			gamma = float(gamma)
			print("Estamos trabalhando nas alterações. Aguarde")
			for x in range(width):
				for y in range(height):
					r, g, b = image.getpixel((x, y))

					r_ = 255 * (r/255)**gamma
					g_ = 255 * (g/255)**gamma
					b_ = 255 * (b/255)**gamma

					new_pixel = (int(r_), int(g_), int(b_))
					new_image.putpixel((x, y), new_pixel)
			imagem5 = new_image
			return new_image

		# Show result

		while(1):
			pergunta = input("Qual transformação quer fazer ? (gray, contraste, brilho, saturação, gamma, sair)\n")
			if pergunta=="gray":
				new_image = cinza(image)
				imagem1 = imagem1.save("C:/PicShifter/gray.jpg")
				print("Alteração feita com sucesso.")
				pergunta2=input("A imagem pode ser vizualizada pesquisando 'gray.jpg'. Deseja salvar a imagem para o programa principal ? (s/n)\n")
				if pergunta2 =="s":
					imagem = cv.imread("C:/PicShifter/gray.jpg")
					insercao()
				else:
					pass

			if pergunta=="contraste":
				new_image = contraste(image)
				imagem2 = imagem2.save("contraste.jpg")
				print("Alteração feita com sucesso.")
			if pergunta=="brilho":
				new_image = brilho(image)
				imagem3 = imagem3.save("brilho.jpg")
				print("Alteração feita com sucesso.")
			if pergunta=="saturação":
				new_image = saturacao(image)
				imagem4 = imagem4.save("saturação.jpg")
				print("Alteração feita com sucesso.")
			if pergunta=="gamma":
				new_image = gamma(image)
				imagem5 = imagem5.save("gamma.jpg")
				print("Alteração feita com sucesso.")
			if pergunta == "sair":
				break




def desfazer():
	""" Essa função retira a alteração poesteriormente feitas a imagem """
	global imgArray#guarda a imagem com a alteração feita
	global auxArray#guarda o código da alteração feita
	global imagem
	
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		if len(imgArray)  > 1:
			val = len(imgArray)
			imagem = imgArray[1]
			del imgArray[0]
			del auxArray[0]
			checkagemDealteracoes()
			print("Alteração feita com sucesso")
		else:
			print("Nenhuma alteração foi feita") 

def verCustom():
	""" Essa função permite que o utilizador vaja em uma linha do tempo, todas as alterações que fez até o momento """
	global check
	global imgArray	
	
	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:

		def x(n):
			pass

		cv.namedWindow("Linha do tempo") #cria uma janela chamada linha do tempo
		cv.createTrackbar("Posção","Linha do tempo",0 ,len(imgArray) -1,x)	#cria umtb chamada posicao, na janela linha do tempo de 0 até o total de imagens com a função que só passa
		if check == 1:
			while(1):
				pos = cv.getTrackbarPos("Posção","Linha do tempo")
				cv.imshow("imagem",imgArray[pos])
				if cv.waitKey(1) & 0xFF == ord('q'):
					cv.destroyAllWindows()
					break				
		else:
			print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")

	
def info():

	if check == 0:
		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	else:
		print("Temos ",len(imgArray), " alterações em memória")
		print("As dimensões e canais da imagem são:",imagem.shape)
		print("Os códigos das alterações feitas são: ",auxArray)
		print("Os códigos das alterações: ",codigosDeAlteracoes)
		print("O caminho da imagem é: ",caminho)
		print("A imagem já foi cinza: ",foiCinza)


def cortar():

		"""Essa função vai cortar a imagem """
		global imgArray#guarda a imagem com a alteração feita funcao insercao()
		global auxArray#guarda o código da alteração feita linha de código "auxArray.insert(0,codigosDeAlteracoes[8])"
		global imagem

		if check == 0:
			print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
		else:
			def selecionarArea(event,x,y,flags,param):
				global ix,iy,drawing			
				if event == cv.EVENT_LBUTTONDOWN:
					drawing = True
					ix,iy = x,y
					global crop
				elif event == cv.EVENT_LBUTTONUP:
					drawing = False					
					cv.rectangle(imagem,(ix,iy),(x,y),(0,1,0),0,cv.LINE_AA)
					
					if ix < x and iy < y: #esquerda » direita cima » baixo
						crop = imagem[iy:y, ix:x]
						print("E » D / C » B")  #x > ix and y > iy						
					if ix < x and iy > y: #esquerda  » direita baixo » cima		
						crop = imagem[y:iy, ix:x]   #y inicial:y final  xinicial: xfinal	
						print("E » D / B » C") 
					if ix > x and iy < y: #direita » esquerda cima » baixo		
						crop = imagem[iy:y, x:ix]   #y inicial:y final  xinicial: xfinal	
						print("D » E / C » B")
					if ix > x and iy > y: #direita » esquerda baixo » cima		
						crop = imagem[y:iy, x:ix]   #y inicial:y final  xinicial: xfinal		
						print("D » E / B » C")
					cv.imshow("crop",crop)
			
		cv.namedWindow('imagem')
		cv.setMouseCallback('imagem',selecionarArea)

		while(1):
			cv.imshow("imagem",imagem)
			
			if cv.waitKey(1) & 0xFF == ord('q'):
				imagem = crop
				auxArray.insert(0,codigosDeAlteracoes[8])
				insercao()
				cv.destroyAllWindows()
				break				
			
		
			
def efeitos():
	from scipy.interpolate import UnivariateSpline #precisa disso para funcionar a função xxt
	global saida #mostrarCustom()
	global nomeSaida#mostrarCustom()
	global imagem
	global imgArray#guarda a imagem com a alteração feita funcao insercao()
	global auxArray#guarda o código da alteração feita linha de código "auxArray.insert(0,codigosDeAlteracoes[9])"

	def Rectangular(image):
		kernel =np.array([[1, 1, 1, 1, 1],
						  [1, 1, 1, 1, 1],
						  [1, 1, 1, 1, 1],
						  [1, 1, 1, 1, 1],
						  [1, 1, 1, 1, 1]])
		return cv.filter2D(image, -1, kernel)

	def Eliptico(image):
		kernel = np.array([[0, 0, 1, 0, 0],
						   [1, 1, 1, 1, 1],
						   [1, 1, 1, 1, 1],
						   [1, 1, 1, 1, 1],
						   [0, 0, 1, 0, 0]],)
		return cv.filter2D(image, -1, kernel)

	def Cruz(image):
		kernel = np.array ([[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0],
							[1, 1, 1, 1, 1],
							[0, 0, 1, 0, 0],
							[0, 0, 1, 0, 0]],)
		return cv.filter2D(image, -1, kernel)

	#as 3 de cima fazem a mesma merda pelo que parece https://homepages.inf.ed.ac.uk/rbf/HIPR2/morops.htm
	"""Criamos manualmente elementos de estruturação nos exemplos anteriores com a ajuda de Numpy. É uma forma retangular. Mas, em alguns casos, você pode precisar de grãos de formato elíptico / circular. Portanto, para este propósito, OpenCV possui uma função, cv.getStructuringElement () . Basta passar o formato e o tamanho do kernel, você obtém o kernel desejado."""
	def sharpen(image): #significa afiar, transforma imahens borradas em umas mais nítidas
		kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
		return cv.filter2D(image, -1, kernel)

	def sepia(image):
		kernel = np.array([[0.272, 0.534, 0.131],
						   [0.349, 0.686, 0.168],
						   [0.393, 0.769, 0.189]])
		return cv.filter2D(image, -1, kernel)

	def gaussianBlur(image):
		return cv.GaussianBlur(image, (35, 35), 0)

	def emboss(image):
		kernel = np.array([[0,-1,-1],
						   [1,0,-1],
						   [1,1,0]])
		return cv.filter2D(image, -1, kernel)
	
	def brightnessControl(image, level):#aumenta com integers
		return cv.convertScaleAbs(image, beta=level)

	def spreadLookupTable(x, y):   #função xxt
	  spline = UnivariateSpline(x, y)
	  return spline(range(256))

	def coldImage(image):
		increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
		decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
		red_channel, green_channel, blue_channel = cv.split(image)
		red_channel = cv.LUT(red_channel, increaseLookupTable).astype(np.uint8)
		blue_channel = cv.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
		return cv.merge((red_channel, green_channel, blue_channel))

	def warmImage(image):
		increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
		decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
		red_channel, green_channel, blue_channel = cv.split(image)
		red_channel = cv.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
		blue_channel = cv.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
		return cv.merge((red_channel, green_channel, blue_channel))
	#kernels da wikipedia
	def Widentity(image):  #3x3
		kernel = np.array([
						[0, 0, 0],
						[0, 1, 0],
						[0, 0, 0]])
		return cv.filter2D(image, -1, kernel)

	def Wedge0(image):  #3x3
		kernel = np.array([
						[1, 0, -1],
						[0, 0, 0],
						[ -1, 0, 1]])
		return cv.filter2D(image, -1, kernel)	
	
	def Wedge1(image):  #3x3
		kernel = np.array([
						[0, 1, 0],
						[1, -4, 1],
						[0, 1, 0]])
		return cv.filter2D(image, -1, kernel)

	def Wedge2(image):  #3x3
		kernel = np.array([
						[-1, -1, -1],
						[-1, 8, -1],
						[-1, -1, -1]])
		return cv.filter2D(image, -1, kernel)
	
	def Wsharpen(image):  #3x3
		kernel = np.array([
						[0, -1, 0],
						[-1, 5, -1],
						[0, -1, 0]])
		return cv.filter2D(image, -1, kernel)

	def WboxBlure(image):  #3x3
		kernel = np.array([
						[1, 1, 1],[1, 1, 1],[1, 1, 1]])* 0.1111
		return cv.filter2D(image, -1, kernel)	
	
	def WGblur(image):  #3x3
		kernel = np.array([
						[1, 2, 1],[2, 4, 2],[1, 2, 1]])* 0.0625
		return cv.filter2D(image, -1, kernel)
	
	def Wemboss(image):  #3x3
		kernel = np.array([
						[-2, -1, 0],[-1, 1, 1],[0, 1, 2]])
		return cv.filter2D(image, -1, kernel)
	
	def sharpen2(image): #significa afiar, transforma imahens borradas em umas mais nítidas
		kernel = np.array([[0, -1, -0], [-1, 5, -1], [0, -1, 0]])
		return cv.filter2D(image, -1, kernel)

	def deblure(image):  #3x3
		kernel = np.array([
						[-2, -1, 0],[-1, 1, 1],[0, 1, 2]])
		return cv.filter2D(image, -1, kernel)

	#fim dos kernels da wikipedia
	initialImage = imagem
	saida = initialImage	
	#esse é o loop princi+al de alterações nas imagens.
	while(1):
		pergunta = input("introduza o nome de uma transofrmação (help para ver nomes)\n")

		if pergunta == "help":
			print("Rectangular,Eliptico,Cruz,sharpen,sepia,gaussianBlur,emboss,brightnessControl,coldImage,warmImage,exitWidentity,Wedge0,Wedge1,Wedge2,Wsharpen,WboxBlure,WGblur,Wemboss")
		
		if pergunta == "Rectangular":
			saida = Rectangular(initialImage)
			nomeSaida =  "Rectangular"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
	
		if pergunta == "Eliptico":
			saida = Eliptico(initialImage)
			nomeSaida =  "Eliptico"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		
		if pergunta == "Cruz":
			saida = Cruz(initialImage)
			nomeSaida =  "Cruz"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
		
		if pergunta == "sepia":
			saida = sepia(initialImage)
			nomeSaida =  "sepia"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
			
			
		if pergunta == "sharpen":
			saida = sharpen(initialImage)
			nomeSaida =  "sharpen"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
		
		if pergunta == "gaussianBlur":
			saida = gaussianBlur(initialImage)
			nomeSaida =  "gaussianBlur"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "emboss":
			saida = emboss(initialImage)
			nomeSaida =  "emboss"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "brightnessControl":
			value = input("introduza o valor do brilho")
			saida = brightnessControl(initialImage,int(value))
			nomeSaida =  "brightnessControl"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass


		if pergunta == "coldImage":
			saida = coldImage(initialImage)
			nomeSaida =  "coldImage"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass


		if pergunta == "warmImage":
			saida = warmImage(initialImage)
			nomeSaida =  "warmImage"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		#wikipediaFunctions
		if pergunta == "Widentity":
			saida = Widentity(initialImage)
			nomeSaida =  "Widentity"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "Wedge0":
			saida = Wedge0(initialImage)
			nomeSaida =  "Wedge0"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "Wedge1":
			saida = Wedge1(initialImage)
			nomeSaida =  "Wedge1"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
		
		if pergunta == "Wedge2":
			saida = Wedge2(initialImage)
			nomeSaida =  "Wedge2"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "Wsharpen":
			saida = Wsharpen(initialImage)
			nomeSaida =  "Wsharpen"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "WboxBlure":
			saida = WboxBlure(initialImage)
			nomeSaida =  "WboxBlure"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
	
		if pergunta == "WGblur":
			saida = WGblur(initialImage)
			nomeSaida =  "WGblur"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass

		if pergunta == "Wemboss":
			saida = Wemboss(initialImage)
			nomeSaida =  "Wemboss"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
		#fim kernel wilipedia
		if pergunta == "sharpen2":
			saida = sharpen2(initialImage)
			nomeSaida =  "sharpen2"
			mostrarcustom()
			salvarCustom()
			if salvar == "s":
				auxArray.insert(0,codigosDeAlteracoes[9])
				break
			else:
				pass
		

		if  pergunta == "exit":
			break



def perpectiva():
	#https://docs.opencv.org/4.5.3/da/d54/group__imgproc__transform.html
	warpPerspective



def remaping():
	a
	#https://amroamroamro.github.io/mexopencv/opencv/remap_demo.html
	#https://docs.opencv.org/4.5.3/da/d54/group__imgproc__transform.html
	#https://amroamroamro.github.io/mexopencv/
	#matlab/  esse aqui é o mais pica
	#https://amroamroamro.github.io/mexopencv/opencv_contrib.html
	#https://amroamroamro.github.io/mexopencv/opencv.html






def borderOpencv():
	a
	#BLUE = [255,0,0]
	#img1 = cv.imread("D:/xaya.jpg")
	#replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
	#reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
	#reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
	#wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
	#constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
	#plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
	#plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
	#plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
	#plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
	#plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
	#plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
	#plt.show()

	#https://docs.opencv.org/4.5.3/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5
	#border types
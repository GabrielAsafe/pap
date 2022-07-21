

def desenhar01():
	"""A função desenhar01 desenha circulos na tela """
	global imagem #PEGA AS IMAGENS COM A ALTERAÇÃO
	global imagemComCores #PEGA AS IMAGENS COM A ALTERAÇÃO
	#cria um evento que desenha circulos quando clica
	def n(o): #FUNÇÃO QUE NÃO RETORNA NADA. USADA PARA PODER SAIR DO CÍCLO
		pass
	
	def draw(evento,x,y,FlagCor,param):
		if evento == cv.EVENT_LBUTTONDBLCLK:			
			cv.circle(imagemComCores,(x,y),pos,(255,0,0),1) # INPUTIMAGE,POSIÇÃO,COR,PREENCHIMENTO/ESPESSURA (-1 PREENCHIMENTO COMPLETO)
	
	cv.namedWindow("imagem")#cria uma janela OBRIGAT�RIO POIS O EVENTO � ASSOCIADO A JANELA! 
	cv.createTrackbar("Raio","imagem",0,100,n)#NOME DA TB, NOME DA JANELA, VALOR INICIAL, VALOR FINAL, FUNÇÃO
	cv.setMouseCallback("imagem",draw)#chama a fun��o
	while(1):
		pos = cv.getTrackbarPos("Raio","imagem")
		cv.imshow("imagem",imagemComCores)
		if cv.waitKey(1) & 0xff == ord('q'):#se q for pressionado fecha a janela e termina o programa
			break
#FIM DO DESENHAR 01




#INCOMPLETO  FALTA CRIAR UMA FORMA DE DAR REWIND NAS IMAGENS 

def desenhar02():

	def desenho(evento,x,y,bandeira,outroTrecoAi):
		if evento == cv.EVENT_LBUTTONDOWN:
			desenhando = True

		if evento == cv.EVENT_MOUSEMOVE:
			if desenhando == True:
				cv.line(quadro,)
		cv.namedWindow("janel")
		quadro = np.zeros((600,600),np.uint8)
		cv.setMouseCallback("janela",quadro)
		while(1):
			cv.imshow("janela",quadro)
		
			if cv.waitKey(1) & 0xff == ord('q'):
				break



			
	global imagemComCores
	global modoDesenho
	global rewind #array que guarda as imagns
	global aux
	modoDesenho = 0
	rewind = []
	
	#if aux == 0:
	#	copia = imagemComCores.copy()
	#	rewind.append(copia)
	#	print(len(rewind))

	def n(o):
		pass


	def draw(evento,x,y,flag,parm):
		global imagemComCores
		global x0,y0,desenhando,apertado
		desenhando = False		

		if evento == cv.EVENT_LBUTTONDOWN:
			#print(evento,x,y,flag,parm)
			desenhando = True	
			x0 = x
			y0 = y
			return x0,y0
			return desenhando
		if evento == cv.EVENT_RBUTTONDBLCLK:
			cv.imshow("rewind",rweind[aux-1])
		
			
		if evento == cv.EVENT_MOUSEMOVE:			
			if desenhando == True & modoDesenho == 1:
				return
			if desenhando == True & modoDesenho == 2:						
				cv.destroyAllWindows
			if desenhando == True & modoDesenho == 3:				
				cv.destroyAllWindows
		
		
		if evento == cv.EVENT_LBUTTONUP:
			
			desenhando = False
			if modoDesenho == 1:
				cv.line(imagemComCores,(x0,y0),(x,y),(255,0,0),5)			
				rewind.append(imagemComCores)
				aux+=1
				print("rewind",len(rewind))
				print("aux",aux)
				cv.destroyAllWindows
			if modoDesenho == 2:
				cv.rectangle(imagemComCores,(x0,y0),(x,y),(0,255,0),3)			
				rewind.append(imagemComCores)
				aux+=1
				cv.destroyAllWindows
			if modoDesenho == 3:
				cv.circle(imagemComCores,(x,y),pos,(255,0,0),2)		
				rewind.append(imagemComCores)
				aux+=1
				cv.destroyAllWindows
			
				
			
		
	cv.namedWindow("imagem")#cria uma janela OBRIGAT�RIO POIS O EVENTO � ASSOCIADO A JANELA! 
	cv.createTrackbar("Raio","imagem",0,100,n)	
	cv.setMouseCallback("imagem",draw)#chama a fun��o

	while(1):
		pos = cv.getTrackbarPos("Raio","imagem")
		cv.imshow("imagem",imagemComCores)
		
		if cv.waitKey(1) & 0xff == ord('q'):#se q for pressionado fecha a janela e termina o programa
			break
		if cv.waitKey(30) == ord("1"):
			modoDesenho = 1
			print(modoDesenho)
		elif cv.waitKey(30) == ord("2"):
			modoDesenho = 2
			print(modoDesenho)
		elif cv.waitKey(30) == ord("3"):
			modoDesenho = 3
			print(modoDesenho)
		
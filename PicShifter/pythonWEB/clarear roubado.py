#""" Essa função na verdade, quando trocado a imagem Src2, faz um blend de duas imagens e com o suposto 'HSV' 
#	    Poderiamos decidir a opacidade que a segunda imagem apareceria na primeira mas quando é feita com uma Src2 
#		branca, torna-se como uma alternativa a um HSV."""
#	global auxArray
#	global imagem
#	global foiCinza #essa merda ta aqui pra controle. se foi cinza = True ela não funciona
		
#	if check == 0:
#		print("Deves carregar uma imagem antes. Use a função 'ler' ou a tecla '1' ")
	
#	elif check == 1 and foiCinza == False:
#		h, w,_ = imagem.shape
#		#PEGA AS IMAGENS COM A ALTERAÇÃO
#		#transforma a src2 no tamanho da primeira pois a função precisa de imagens de mesmo shape
#		def x(n):
#			pass
#		src2 = cv.imread("C:/PicShifter/src.png")#se não tiver essa imagem o bagulho não funciona como hsv
#		src2=cv.resize(src2,(h,w))

#		# add or blend the images
	
#		cv.namedWindow("HSV")		
#		cv.createTrackbar("Hue","HSV",1 ,360,x)
#		cv.createTrackbar("Saturation","HSV",1 ,10,x)
#		cv.createTrackbar("Value","HSV",1 ,10,x) #parece que não funciona mas isso é uma escalar somado a cada valor (alfa e beta) quando está somando as imagens

#		# save the output image
		
#		while(1):		
#			if cv.waitKey(1) & 0xFF == ord('q'):
#				imagem	= dst
#				insercao()
#				cv.destroyAllWindows()
#				break
#			else:
			
#				v1 = cv.getTrackbarPos("Hue","HSV")
#				v2 = cv.getTrackbarPos("Saturation","HSV")
#				v3 = cv.getTrackbarPos("Value","HSV")
#				dst = cv.addWeighted(imagem, v1/10, src2, v2/10, v3/10)
#				auxArray.insert(0,codigosDeAlteracoes[7])
#				cv.imshow('image.png', dst)
#				cv.waitKey(1)
	
#	else:
#		print("Devido a ter transformado a imagem em cinza essa função está desativada")


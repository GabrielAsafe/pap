import LM as lm


lm.inicio()

while (1):
    argumento=input("//BlocoPrincipal/")

    if argumento == "1" or argumento =="ler":
       lm.ler()       
    if argumento == "2" or argumento =="resize":        
        x=input("Introduza o tamanho na horizontal:\n")
        y=input("Introduza o tamanho na vertical:\n")
        lm.resize(int (x), int(y))#xy   
            
    if argumento == "3"  or argumento =="Torgb":
        lm.toRgb()    
    if argumento == "4"  or argumento =="cinza":
        lm.cinza()   
    if argumento == "5"  or argumento =="Hflip":
        lm.Hflip()
    if argumento == "6" or argumento =="Vflip":
        lm.Vflip()
    if argumento == "7" or argumento =="rotacao":
        lm.rotacao()
    if argumento == "help":
        lm.help()
    if argumento == "8"  or argumento =="ver": 
        lm.ver()                              
    if argumento == "9" or argumento =="salvar":
        lm.salvar()
    if argumento == "10" or argumento =="MinhasImagens":
        lm.MostrarOpcoes()    
    if argumento == "11" or argumento =="hsv":
        lm.hsv()                
    if argumento == "12" or argumento =="desfazer":
        lm.desfazer()
    if argumento == "13" or argumento =="LinhaDoTempo":
        lm.LinhaDoTempo()
    if argumento == "14" or argumento == "cortar":        
        lm.cortar()
    if argumento == "15" or argumento == "efeitos":
        lm.efeitos()
    if argumento == "info" :
        lm.info()
    if argumento == "16" or argumento == "pes":
        lm.perspectiva()#não funciona  

    if argumento == "desenhar1"  or argumento =="000":
        lm.desenhar01()
        #lm.desenhar02()
            
    if argumento == "sair" :
        print("Adeus")
        break
   
  

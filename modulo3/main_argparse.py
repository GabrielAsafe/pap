#!C:\Users\gabri\AppData\Local\Programs\Python\Python37\\python.exe
import argparse
import LM_argparse as lm
parser = argparse.ArgumentParser()  #criando um argument parser
# parser.add_argument("a") #adicionando argumentos
# parser.add_argument("b") #adicionando argumentos
# parser.add_argument("operacion") #adicionando argumentos
# args = parser.parse_args()  #parseando argumentos

"""
como adicionar funções:
adiciona o nome da função em add argument/choices 
cria um if
"""

parser = argparse.ArgumentParser(description='me mama')
parser.add_argument('-i', '--imagem', type=str, help='Parámetro a')
parser.add_argument('-f', '--funcao',type=str, choices=['ler','resize','toRgb','cinza','Hflip','Vflip','rotacao','salvar','contraste','saturacao','gamma','brilho','cinza2','desfazer','linha_do_tempo','info','cortar','efeitos','perspectiva','detec','canais','compress','convert','sharpen','sepia','gaussianBlur','emboss','coldImage','warmImage','preview'],
default='ler', required=False, help='Operación a realizar con a y b')
parser.add_argument('-hd', '--resizeH', type=int, help='altura da imagem', required=False)
parser.add_argument('-wd', '--resizeW', type=int, help='largura da imagem', required=False)
parser.add_argument('-vv1', '--variavel1', type=int, help='variável ocasional 1', required=False)
parser.add_argument('-vv2', '--variavel2', type=int, help='variável ocasional 2', required=False)

parser.add_argument('-vv3', '--variavel3', type=str, help='variável ocasional 3 para strings', required=False)
parser.add_argument('-vv4', '--variavel4', type=int, help='variável que le inteiros. compresao', required=False)
args = parser.parse_args()

#verificação do argumento parseado
variables = vars(args)
print(variables)



#checagens dos if's

if args.funcao == 'ler':
    lm.ler(args.imagem)
    #print("Leitura feita com sucesso")  #descomentar se testar pelo cmd


if args.funcao == 'resize': 
    imagem=lm.ler(args.imagem)
    lm.resize(imagem,args.resizeW, args.resizeH)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
        
if args.funcao == 'toRgb': 
    imagem=lm.ler(args.imagem)
    lm.Torgb(imagem)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
   
if args.funcao == 'cinza': 
    imagem=lm.ler(args.imagem)
    lm.cinza(imagem)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
   

if args.funcao == 'Hflip': 
    imagem=lm.ler(args.imagem)
    lm.Hflip(imagem)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
   
   
if args.funcao == 'Vflip': 
    imagem=lm.ler(args.imagem)
    lm.Vflip(imagem)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
   
   
if args.funcao == 'rotacao': 
    imagem=lm.ler(args.imagem)
    lm.rotacao(imagem,args.variavel1)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
  

if args.funcao == 'contraste': 
    lm.contraste(args.imagem,args.variavel2)
   # print("Alteração feita com sucesso") # descomentar se testar pelo cmd

if args.funcao == 'cinza2':
    lm.cinza2(args.imagem)
   # print("Alteração feita com sucesso") # descomentar se testar pelo cmd
    
if args.funcao == 'gamma': 

    lm.gamma(args.imagem,args.variavel2)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
 
if args.funcao == 'saturacao': 

    lm.saturacao(args.imagem,args.variavel2)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
   

if args.funcao == 'brilho': 
    lm.brilho(args.imagem,args.variavel2)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd
   
if args.funcao == 'info': 
    #imagem=lm.ler(args.imagem)
    lm.info(args.imagem)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd

if args.funcao == 'detec': 
    lm.detec(args.imagem)
    #print("Alteração feita com sucesso") # descomentar se testar pelo cmd


if args.funcao == 'canais':
    lm.canais(args.imagem)

if args.funcao == 'compress':
    lm.compress(args.imagem,args.variavel3,args.variavel4)


if args.funcao == 'convert':
    lm.convert(args.imagem,args.variavel3)



if args.funcao == 'sharpen':
    lm.sharpen(args.imagem)



if args.funcao == 'sepia':
    lm.sepia(args.imagem)



if args.funcao == 'gaussianBlur':
    lm.gaussianBlur(args.imagem)


if args.funcao == 'emboss':
    lm.emboss(args.imagem)

if args.funcao == 'coldImage':
    lm.coldImage(args.imagem)

if args.funcao == 'warmImage':
    lm.warmImage(args.imagem)
	
	
if args.funcao == 'preview':
    lm.preview(args.imagem)



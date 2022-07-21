import numpy as np
import cv2 as cv

imagem = cv.imread("C:/PicShifter/rakan.jpg")
h,w,c = imagem.shape
global horizontal,vertical
horizontal=[]
vertical=[]


def mudanca():
    global horizontal,vertical
    # All points are in format [cols, rows]
    pt_A = [int(horizontal[3]),int(vertical[3])]
    pt_B = [int(horizontal[2]),int(vertical[2])]
    pt_C = [int(horizontal[1]),int(vertical[1])]
    pt_D = [int(horizontal[0]),int(vertical[0])]
    # Here, I have used L2 norm. You can use L1 also.
    width_AD = np.sqrt(((pt_A[0] - pt_D[0]) ** 2) + ((pt_A[1] - pt_D[1]) ** 2))
    width_BC = np.sqrt(((pt_B[0] - pt_C[0]) ** 2) + ((pt_B[1] - pt_C[1]) ** 2))
    maxWidth = max(int(width_AD), int(width_BC))     
     
    height_AB = np.sqrt(((pt_A[0] - pt_B[0]) ** 2) + ((pt_A[1] - pt_B[1]) ** 2))
    height_CD = np.sqrt(((pt_C[0] - pt_D[0]) ** 2) + ((pt_C[1] - pt_D[1]) ** 2))
    maxHeight = max(int(height_AB), int(height_CD))

    input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
    output_pts = np.float32([[0, 0],
                            [0, maxHeight - 1],
                            [maxWidth - 1, maxHeight - 1],
                            [maxWidth - 1, 0]])  
    # Compute the perspective transform M
    M = cv.getPerspectiveTransform(input_pts,output_pts)
    out = cv.warpPerspective(imagem,M,(maxWidth, maxHeight),flags=cv.INTER_LINEAR)
    cv.imshow("aaaaaaaaa",out)
    
def selecionarArea(event,x,y,flags,param):
    global horizontal,vertical
    if event == cv.EVENT_LBUTTONDOWN:
            drawing = True
            horizontal.insert(0,x)
            vertical.insert(0,y)

                                    
    elif event == cv.EVENT_LBUTTONUP:
            drawing = False					
            cv.line(imagem,(horizontal[0],vertical[0]),(x,y),(255,255,255),5)#cv2.line(image, start_point, end_point, color, thickness)
            #print(horizontal[0],vertical[0])

cv.namedWindow('imagem')
cv.setMouseCallback('imagem',selecionarArea)

print("Em vista de evitar frustrações futuras, a seleção deve ser da seguinte forma:\n14\n23")
while(1):
        
        cv.imshow("imagem",imagem)        
        #print("tamanho",len(horizontal))
        if len(horizontal) == 4:
            #print(horizontal,"\n",vertical)            
            break       
        if cv.waitKey(1) & 0xFF == ord('q'):                           
            #imagem = crop
            #auxArray.insert(0,codigosDeAlteracoes[8])
            #insercao()
            cv.destroyAllWindows()
            break

mudanca()



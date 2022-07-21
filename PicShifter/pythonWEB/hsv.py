from PIL import Image
import numpy as np

# Open image
image = Image.open('C:/PicShifter/eu.jpg')

# Filter
def truncate(x):
        '''makes sure returned value is between 0 and 255'''
        return min(255, max(0, x))

def cinza(image):
    global imagem1,imagem2,imagem3,imagem4,imagem5
    # Get image dimesions
    width, height = image.size
    # Create a white RGB image
    new_image = Image.new("RGB", (width, height), "white")
    # Filter magic happens here
    # Grayscale filter
    for x in range(width):
      for y in range(height):
        # Get original pixel colors
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
    pergunta = input("Qual transformação quer fazer ? (gray,contraste,brilho,saturação,gamma)\n")
    if pergunta=="gray":
        new_image = cinza(image)
        imagem1 = imagem1.save("gray.jpg")
        print("Alteração feita com sucesso.")
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

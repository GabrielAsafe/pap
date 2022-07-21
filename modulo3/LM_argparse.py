import cv2 as cv
import numpy as np
import sys
import os
import time #gera o nome para a imagem no salvamento
import pyautogui, sys #posicionamento do mouse
from PIL import Image #função de HSV
from scipy.interpolate import UnivariateSpline #precisa disso para funcionar a função xxt
global imagem


def mostrar(x):
        while(1):
            cv.imshow("imagem",x)
            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break

def spreadLookupTable(x, y):   #função xxt
	  spline = UnivariateSpline(x, y)
	  return spline(range(256))

def salvar(imagem):
		extensao = "jpg"
		nome = "OutImage"+"."+extensao
		caminho= "..\PicShifter/"
		completo = caminho+nome
		cv.imwrite(completo, imagem) #salva a imagrm na pasta do projeto


def ler(x):
   global imagem
   imagem = cv.imread(x)#le a imagem em bgr. normalmente n�o vale a pena converter pra rgb
   #salvar(imagem)
   return imagem
   ##mostrar(imagem)


def resize(imagem,x,y):

    imagem = cv.resize(imagem,(x,y)) #transformação morfológica
    salvar(imagem)
    ##mostrar(imagem)

def Torgb(imagem):
    imagem = cv.cvtColor(imagem,cv.COLOR_BGR2RGB)
    salvar(imagem)



def cinza(imagem):
    imagem = cv.cvtColor(imagem,cv.COLOR_BGR2GRAY)
    salvar(imagem)
    


def Hflip(imagem):
    imagem= cv.flip(imagem,1)
    salvar(imagem)
    

def Vflip(imagem):
    imagem= cv.flip(imagem,0) #transformação morfológica
    salvar(imagem)
    


def rotacao(imagem,angulo): #pega o nome da imagem e os valores da TB
    h, w = imagem.shape[:2] #pega as dimensões da imagem para fazer a rotação pelo centro dela
    M = cv.getRotationMatrix2D((int(w/2), int(h/2)), angulo, 1)#centro da imagem em H e W, ângulo, escala da imagem
    imagem = cv.warpAffine(imagem, M, (w, h))
    salvar(imagem)


def contraste(imagem, tipo):
    image = Image.open(imagem)#carrega uma imagem no formato da biblioteca do pillow

    def truncate(x):#makes sure returned value is between 0 and 255
            return min(255, max(0, x))

    # Get image dimesions
    width, height = image.size
    # Create a white RGB image
    new_image = Image.new("RGB", (width, height), "white")

    #contraste -100 a +100

    data = np.array(image)#converter imagem em array numpy para possibilitar as alterações 
    beta = tipo
    beta = int(beta)
    print("Estamos trabalhando nas alterações. Aguarde")
    # Calculate average brightness
    μ = np.mean(data, axis=2)#media
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
    imagem2 = imagem2.save("..\PicShifter/hsv\ contraste.jpg")


def cinza2(imagem):
    image = Image.open(imagem)#carrega uma imagem no formato da biblioteca do pillow

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
        if x == width/2:
            print("50% do processo concluído")
        
    imagem1 = new_image
    imagem1 = imagem1.save("..\PicShifter/hsv\ gray.jpg")



def brilho(imagem, tipo):
    image = Image.open(imagem)#carrega uma imagem no formato da biblioteca do pillow
    
    def truncate(x):#makes sure returned value is between 0 and 255
        return min(255, max(0, x))
    # Get image dimesions
    width, height = image.size
    # Create a white RGB image
    new_image = Image.new("RGB", (width, height), "white")
    # Brightness filter -64 a +64
    d = tipo
    d = int(d)
    print("Estamos trabalhando nas alterações. Aguarde")
    # Brightness filter
    for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                r_ = truncate(r + d)
                g_ = truncate(g + d)
                b_ = truncate(b + d)
                new_pixel = (int(r_), int(g_), int(b_))
                new_image.putpixel((x, y), new_pixel)
    imagem3 = new_image
    imagem3 = imagem3.save("..\PicShifter/hsv\ brilho.jpg")



def gamma(imagem, tipo):
    image = Image.open(imagem)#carrega uma imagem no formato da biblioteca do pillow        
    def truncate(x):#makes sure returned value is between 0 and 255
        return min(255, max(0, x))
    # Get image dimesions
    width, height = image.size
    # Create a white RGB image
    new_image = Image.new("RGB", (width, height), "white")
    #gamma correction 33, 66, 100, 133, 166 and 200
    gamma= tipo /100

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
    imagem5 = imagem5.save("..\PicShifter/hsv\ gamma.jpg")


def saturacao(imagem, tipo):
    image = Image.open(imagem)#carrega uma imagem no formato da biblioteca do pillow
    def truncate(x):#makes sure returned value is between 0 and 255
        return min(255, max(0, x))        
    width, height = image.size
    # Create a white RGB image
    new_image = Image.new("RGB", (width, height), "white")
    #saturação -100 a +100
    betas= tipo
    print("Estamos trabalhando nas alterações. Aguarde")
    # Calculate factor
    if betas == 255: alpha = np.infty
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
    imagem4 = imagem4.save("..\PicShifter/hsv\ saturacao.jpg")


def info(imagem):
	#fonte  https://www.thepythoncode.com/article/extracting-image-metadata-in-python
    #essa função extrai os metadados da imagem

	from PIL import Image
	from PIL.ExifTags import TAGS

	# path to the image or video
	imagename = imagem

	# read the image data using PIL
	image = Image.open(imagename)

	# extract other basic metadata
	info_dict = {
		"Filename": image.filename,
		"Image Size": image.size,
		"Image Height": image.height,
		"Image Width": image.width,
		"Image Format": image.format,
		"Image Mode": image.mode,
		"Image is Animated": getattr(image, "is_animated", False),
		"Frames in Image": getattr(image, "n_frames", 1)
	}
	f = open("dimensoes.txt", "w")
    
	for label,value in info_dict.items():
		#print(f"{label:25}: {value}")
	   
		f.write(f"{label:25}: {value} \n")
	f.close()   

		# extract EXIF data
	exifdata = image.getexif()

	# iterating over all EXIF data fields
	f = open("dimensoes.txt", "a")
	for tag_id in exifdata:
		# get the tag name, instead of human unreadable tag id
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)
		# decode bytes 
		if isinstance(data, bytes):
			data = data.decode()
		#print(f"{tag:25}: {data}")
		f.write(f"{tag:25}: {data} \n")

	f.close()      



def detec(imagem):
    from PIL import Image
    import matplotlib.pyplot as plt
    import tensorflow as tf
    import numpy as np
    import os

    from object_detection.utils import label_map_util
    from object_detection.utils import config_util
    from object_detection.utils import visualization_utils as viz_utils
    from object_detection.builders import model_builder


    center_net_path = './centernet_resnet50_v1_fpn_512x512_coco17_tpu-8/'
    pipeline_config = center_net_path + 'pipeline.config'
    model_path = center_net_path + 'checkpoint/'
    label_map_path = 'mscoco_label_map.pbtxt'
    image_path = imagem

    # Load pipeline config and build a detection model
    configs = config_util.get_configs_from_pipeline_file(pipeline_config)
    model_config = configs['model']
    detection_model = model_builder.build(model_config=model_config, is_training=False)

    # Restore checkpoint
    ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
    ckpt.restore(os.path.join(model_path, 'ckpt-0')).expect_partial()

    def get_model_detection_function(model):
        @tf.function
        def detect_fn(image):
            image, shapes = model.preprocess(image)
            prediction_dict = model.predict(image, shapes)
            detections = model.postprocess(prediction_dict, shapes)

            return detections, prediction_dict, tf.reshape(shapes, [-1])
        return detect_fn

    detect_fn = get_model_detection_function(detection_model)



    label_map_path = label_map_path
    label_map = label_map_util.load_labelmap(label_map_path)
    categories = label_map_util.convert_label_map_to_categories(
        label_map,
        max_num_classes=label_map_util.get_max_label_map_index(label_map),
        use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    label_map_dict = label_map_util.get_label_map_dict(label_map, use_display_name=True)


    image = np.array(Image.open(image_path))
    input_tensor = tf.convert_to_tensor(np.expand_dims(image, 0), dtype=tf.float32)
    detections, predictions_dict, shapes = detect_fn(input_tensor)

    label_id_offset = 1
    image_np_with_detections = image.copy()

    # Use keypoints if available in detections
    keypoints, keypoint_scores = None, None
    if 'detection_keypoints' in detections:
        keypoints = detections['detection_keypoints'][0].numpy()
        keypoint_scores = detections['detection_keypoint_scores'][0].numpy()

    def get_keypoint_tuples(eval_config):
        tuple_list = []
        kp_list = eval_config.keypoint_edge
        for edge in kp_list:
            tuple_list.append((edge.start, edge.end))
        return tuple_list

    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'][0].numpy(),
        (detections['detection_classes'][0].numpy() + label_id_offset).astype(int),
        detections['detection_scores'][0].numpy(),
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.30,
        agnostic_mode=False,
        keypoints=keypoints,
        keypoint_scores=keypoint_scores,
        keypoint_edges=get_keypoint_tuples(configs['eval_config']))

    plt.figure(figsize=(12,16))
    plt.imshow(image_np_with_detections)
    plt.savefig('..\PicShifter/predict/detec.jpg')
    print("Sua imagem está salvo em 'Predictions' na pasta Picshifter.")


def compress(imagem,tipo ,qualidade):

    imagem = cv.imread(imagem)
 
    if tipo == "jpg":
        cv.imwrite("..\PicShifter/comprimida.jpg", imagem, [cv.IMWRITE_JPEG_QUALITY, qualidade])

    if tipo == "png":
        cv.imwrite("..\PicShifter/comprimida.png", imagem, [int(cv.IMWRITE_PNG_COMPRESSION),qualidade]) 



def convert(imagem, tipo):
    imagem = cv.imread(imagem)
    if tipo == "jpg":
        cv.imwrite("..\PicShifter/convertida.jpg",imagem)
        print("alteração feita com sucesso")
    if tipo == "png":
        cv.imwrite("..\PicShifter/convertida.png", imagem) 
        print("alteração feita com sucesso")
    
    if tipo == "jpeg":
        cv.imwrite("..\PicShifter/convertida.jpeg", imagem)
        print("alteração feita com sucesso") 

    if tipo == "tiff":
        cv.imwrite("..\PicShifter/convertida.tiff", imagem)
        print("alteração feita com sucesso")

    print(tipo)


#aqui começa os efeitos. Eles precisam ser lidos pela função de leitura(cv.imread) do programa para estar no formato certo.

def sharpen(imagem): #significa afiar, transforma imahens borradas em umas mais nítidas
    imagem = cv.imread(imagem)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    imagem = cv.filter2D(imagem, -1, kernel)
    salvar(imagem)

def sepia(imagem):
	imagem = cv.imread(imagem)
	imagem = cv.transform(imagem, np.matrix([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])) # multipying image with special sepia matrix
	imagem[np.where(imagem > 255)] = 255 # normalizing values greater than 255 to 255
	imagem = np.array(imagem, dtype=np.uint8) # converting back to int
	salvar(imagem)

def gaussianBlur(imagem):
	imagem = cv.imread(imagem)
	imagem = cv.GaussianBlur(imagem,(5,5),cv.BORDER_DEFAULT)
	salvar(imagem)

def emboss(imagem):
    imagem = cv.imread(imagem)
    kernel = np.array([[0,-1,-1],
                        [1,0,-1],
                        [1,1,0]])
    imagem = cv.filter2D(imagem, -1, kernel)
    salvar(imagem)

def coldImage(imagem):
    imagem = cv.imread(imagem)
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv.split(imagem)
    red_channel = cv.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    imagem = cv.merge((red_channel, green_channel, blue_channel))
    salvar(imagem)


def warmImage(imagem):
    imagem = cv.imread(imagem)
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv.split(imagem)
    red_channel = cv.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    imagem = cv.merge((red_channel, green_channel, blue_channel))
    salvar(imagem)
	
	
def preview(imagem):
	imagem = cv.resize(imagem,(200,200)) #transformação morfológica
	print("pré visualisando a imagem")
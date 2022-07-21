<?php
    $url = "/..\main/index.php/";
    $currentDirectory = getcwd();
    $uploadDirectory = "/..\Picshifter/";

    $errors = []; // Store errors here

    $fileExtensionsAllowed = ['jpeg','jpg','png','txt','pdf']; // These will be the only file extensions allowed 

    $fileName = $_FILES['the_file']['name'];
    $fileSize = $_FILES['the_file']['size'];
    $fileTmpName  = $_FILES['the_file']['tmp_name'];
    $fileType = $_FILES['the_file']['type'];
    //$fileExtension = strtolower(end(explode('.',$fileName)));
	$tmp = explode('.', $fileName);
	$fileExtension = strtolower(end($tmp));

    $uploadPath = $currentDirectory . $uploadDirectory . basename($fileName); 

    if (isset($_POST['submit'])) {

      if (! in_array($fileExtension,$fileExtensionsAllowed)) {
        $errors[] = "Essa extensão não é permitida pelo servidor. Por favor selecione imagens com a extensão JPEG ou PNG ";
      }

      if ($fileSize > 10000000) {
        $errors[] = "File exceeds maximum size (10MB)";
      }

      if (empty($errors)) {
        $didUpload = move_uploaded_file($fileTmpName, $uploadPath);

        if ($didUpload) {
          echo "O arquivo " . basename($fileName) . " Foi carregado";
          //header("Refresh:0; url=$url");
        } else {
          echo "Aconteceu um erro inesperado, por favor entre em contacto com a assistência técnica.";
        }
      } else {
        foreach ($errors as $error) {
          echo $error . "Esses são os erros: " . "\n";
        }
      }

    }

   
?>
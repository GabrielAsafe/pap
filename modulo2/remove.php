<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">

        <title>PicShifter remover</title>
        <link rel="apple-touch-icon" sizes="180x180" href="..\Picshifter/icon/apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="32x32" href="..\Picshifter/icon/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="..\Picshifter/icon/favicon-16x16.png">
        <link rel="manifest" href="..\Picshifter/icon/site.webmanifest">
        <link rel="mask-icon" href="..\Picshifter/icon/safari-pinned-tab.svg" color="#5bbad5">
        <meta name="msapplication-TileColor" content="#da532c">
        <meta name="theme-color" content="#ffffff">
    </head>



    <body>



        <?php 

            if(isset($_GET["old_name"])){ $old_name = $_GET["old_name"]; ; 

            $file_pointer = "..\PicShifter/" .$old_name;
  
            // Use unlink() function to delete a file
            if (!unlink($file_pointer)) {
                echo ("$file_pointer Um erro inesperado ocorreu");
            }
            else {
                echo ("$file_pointer Foi deletado");
            }}            
         ?>


            <!-- Nessa tab ficam as imagem -->
            <div>                               
                <?php
                    //isso é uma função para retornar os nomes dos arquivos que estão na pasta picshifter 
                    $nomes_das_imagens = array();
                    $cont = 0;
                    $fileList = glob('..\PicShifter/*.*');
                    foreach($fileList as $filename){
                        if(is_file($filename)){
                            $cont = $cont + 1;
                            $nomes_das_imagens[$cont] = $filename;
                                }   
                        }        
                        //cria um array que guarda os nomes das imagens que a função glob acho na pasta picshifter e escreve elas dento de um botão
                        for($i=1;$i<=count($nomes_das_imagens);$i++){                                

                            echo("<div class='a'><a href='remove.php?old_name=$nomes_das_imagens[$i]'> $nomes_das_imagens[$i] </a></div> <br>");
                        }
                ?>
            </div>


    </body>
</html>
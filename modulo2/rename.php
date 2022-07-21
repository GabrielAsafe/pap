<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="style.css">

        <title>PicShifter Renomear</title>
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
            if(isset($_GET["new_name"])){ $new_name = $_GET["new_name"]; ;}  

            if(isset($_GET["old_name"])){ $old_name = $_GET["old_name"];;}  

            if (isset($old_name) && isset($new_name)){
            $old_name = "..\PicShifter/" .$old_name;
            $new_name = "..\PicShifter/" .$new_name;
            rename($old_name, $new_name) ; 
            echo("Alteração feita com sucesso");
        }?>


        <div class="imagens">                               
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

                        echo("<div class='a'><a href='rename.php?old_name=$nomes_das_imagens[$i]'> $nomes_das_imagens[$i] </a></div> <br>");
                    }
            ?>
        </div>



    <?php     
        if(isset($_GET["old_name"])){ $old_name = $_GET["old_name"];?>
            <div class="formulario">
                <form action="rename.php" class="form-container">           
                        <input class="input" type="text" placeholder="Nome antigo" name="old_name" value="<?=$old_name?>" >
                        <input class="input" type="text" placeholder="Novo nome" name="new_name" >  
                        <button type="submit" class="btn">Mudar nome</button>
                </form>
            </div>
    <?php }; ?>

        
    
       

    </body>
</html>
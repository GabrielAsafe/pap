
<?php if(!isset($nome_imagem) && (!isset($funcao))){ ?>

    <img src="../PicShifter/iconesLaterais/notloaded.png ?>">

    <?php    } ?>

    <?php  if(isset($nome_imagem) && (!isset($funcao)  )){ ?>

    <img src=" <?= $_GET["nome_imagem"];  ?>">

    <?php    } ?>


<!-- se a função utilizada não for detec ele retorna as imagens contidas em hsv-->
<?php if(isset($funcao) && isset($imagem) && $funcao!= "detec"  && $funcao!= "info"  && $funcao!= "compress"  && $funcao!= "convert"){ ?>
    <?php if($funcao == "gamma" || $funcao == "saturacao" || $funcao == "brilho" || $funcao == "contraste"  ){ ?>

        <img src="../PicShifter/hsv/ <?=$funcao?>.jpg">

    <?php    }else{ ?>
        <img src="../PicShifter/OutImage.jpg ?>">
    <?php }   
} ?>


<!-- se a função utilizada for detec ele retorna a imagem que passou pela api do tensorflow-->
<?php if(isset($funcao) && isset($imagem) && $funcao== "detec" ){ ?>
    <?php if(  $funcao == "detec"  ){ ?>
        <img src="../PicShifter/predict/<?=$funcao?>.jpg">

    <?php    }else{ ?>
        <img src="../PicShifter/OutImage.jpg ?>">
    <?php }  
} ?>



<!-- se a função utilizada for detec ele retorna a imagem que passou pela api do tensorflow-->
<?php if(isset($funcao) && isset($imagem) && $funcao== "compress" ){ ?>
    <?php if($variavel3 == "jpg"  ){ ?>
        <img src="../PicShifter/comprimida.jpg ?>">

    <?php    }else{ ?>
        <img src="../PicShifter/comprimida.png ?>">
    <?php }  
} ?>


<!-- se a função utilizada for detec ele retorna a imagem que passou pela api do tensorflow-->
<?php if(isset($funcao) && isset($imagem) && $funcao== "convert" ){ ?>
    <?php if($variavel3 == "jpg"  ){ ?>
        <img src="../PicShifter/convertida.jpg?>">

    <?php    } if($variavel3 == "png"  ){ ?>
        <img src="../PicShifter/convertida.png?>">

    <?php    } if($variavel3 == "jpeg"  ){ ?>
        <img src="../PicShifter/convertida.jpeg?>">

    <?php    }if($variavel3 == "tiff"  ){ echo("A imagem está na pasta do programa. Browser não suporta abrir .tiff ") ?>
        <img src="../PicShifter/convertida.tiff?>">
       
    <?php }  
} ?>




<!-- se a função utilizada for info ele retorna a mesma imagem que foi selecionada-->
<?php  if(isset($imagem) && (isset($funcao)) && $funcao== "info"){ ?>
    <img src="<?= $_GET["imagem"];  ?>">
<?php    } ?>

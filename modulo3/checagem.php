<?php

$mostrar = FALSE;


if(isset($_GET["nome_imagem"])){ $nome_imagem = $_GET["nome_imagem"]; 
    if($mostrar == TRUE){
    echo("<br> nome da imagem ". $nome_imagem );
       };
;}  

if(isset($_GET["Função"])){ $funcao = $_GET["Função"]; 
    if($mostrar == TRUE){
        echo("<br>Função ". $funcao);
        };
};
if(isset($_GET["width"])){ $width = $_GET["width"];
    if($mostrar == TRUE){
        echo("<br>Largura ". $width);
        };
};
if(isset($_GET["height"])){ $height = $_GET["height"];
    if($mostrar == TRUE){
        echo("<br>Altura ". $height);
        };
};


if(isset($_GET["imagem"])){ $imagem = $_GET["imagem"];
    if($mostrar == TRUE){
        echo("<br>nome da imagem 2 ". $imagem);
        };
};



if(isset($_GET["variavel1"])){ $variavel1 = $_GET["variavel1"];
    if($mostrar == TRUE){
        echo("<br>Variável 1  ". $variavel1);
        };
};

if(isset($_GET["variavel2"])){ $variavel2 = $_GET["variavel2"];
    if($mostrar == TRUE){
        echo("<br>Variável 2  ".$variavel2);
        };
};

if(isset($_GET["variavel3"])){ $variavel3 = $_GET["variavel3"];
    if($mostrar == TRUE){
        echo("<br>Variável 3  ".$variavel3);
        };
};

if(isset($_GET["variavel4"])){ $variavel4 = $_GET["variavel4"];
    if($mostrar == TRUE){
        echo("<br>Variável 4  ".$variavel4);
        };
};






?>

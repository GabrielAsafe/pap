<!-- 
Checagem tem que ser importado no inicio do programa

caixa_imagem tem que ser importado depois do funções_check

Dentro do LM_argparse tem que se alterar o caminho de onde se vai salvar, dependendo da estrutura dos diretórios

dentro de funcs cada href tem que apontar para uma pg

Pensar em eventualmente fazer com que TODAS as funções tenham opção de decidir onde salvar, ou pelo menos definir todos os caminhos de salvamento por uma constante
-->

<?php include("checagem.php");?>
<!doctype html>

<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="style.css" >
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;700&display=swap" rel="stylesheet">
        <script>let aberto=0;</script>
    </head>
    
    <body>
        <section class="corpo">

            <div class="CaixaImagem">
                <?php include("funcoes_check.php"); ?>
                <?php include("caixa_img.php");?>
            </div>


            <div  class="Classeformularios">
                <?php  if(isset($nome_imagem)){ ?>
                <div>
                    <div class="">
                        <button class="bot" id="bt1" onclick="abrir()">Abrir formulário</a></button>
                        <button class="bot" id="bt2" onclick="fechar()">Fechar formulário</a></button>
                    </div>
                </div>


                <div class="">
                    <div class="form" id="form">
                        <form action="cinza.php" method="get" id="form1"><!--mudar action em cada form-->
                            <label for="fname">Nome da imagem:</label><br>
                            <input class="input" type="text" placeholder="imagem" readonly="readonly" value="<?=$nome_imagem?>" name="imagem" required><br>
                            <label for="fname">Nome da função:</label><br>
                            <input class="input" type="text" placeholder="função" readonly="readonly" value="cinza" name="Função" required><!-- alterar o value em cada função--><br>

                            <button class="bot"type="submit" form="form1" value="Submit">Transformar imagem</button><br>
                        </form>                    
                    </div> 
                </div >
                <?php }else{?>
                <button class="bot" onclick="popup()">Abrir formulário</button>

                <script>
                    function popup(){alert("Deve selecionar uma imagem antes. As imagens são selecionadas no campo Base.");} 
                </script> 
                <?php } ?>
            
            </div>


        <div class="CaixaNomeImagem">

            <div class="">

                    <button class="bot" id="bt3" onclick="abrir2()">Abrir imagens</a></button>
                    <button class="bot" id="bt4" onclick="fechar2()">Fechar imagens</a></button>
                </div>
                    <div class="lista" id="lista">                               
                        <?php
                            //isso é uma função para retornar os nomes dos arquivos que estão na pasta picshifter 
                            $nomes_das_imagens = array();
                            $cont = 0;
                            $fileList = glob('../PicShifter/*.*');
                            foreach($fileList as $filename){
                                if(is_file($filename)){
                                    $cont = $cont + 1;
                                    $nomes_das_imagens[$cont] = $filename;
                                        }   
                                } 
                                if ($cont == 0){
                                    echo("Deve adicionar imagens na pasta. Vá ao separador ");
                                }       
                                //cria um array que guarda os nomes das imagens que a função glob acho na pasta picshifter e escreve elas dento de um botão
                                for($i=1;$i<=count($nomes_das_imagens);$i++){                                
                                    echo("<a href='cinza.php?nome_imagem=$nomes_das_imagens[$i]'> $nomes_das_imagens[$i] </a> <br>"); //mudar essa linha em cada formulário
                        } ?>
                    </div>

            </div>


        </section>

        <script>
           function abrir(){

                if(aberto % 2 == 0){
                    document.getElementById("bt1").style.display = "none";
                    document.getElementById("bt2").style.display = "block";

                    document.getElementById("form").style.display = "block";
                    aberto = aberto+1;
                    console.log(aberto)
                }

            }

                function fechar(){
                    if(aberto % 2 != 0){
                        document.getElementById("bt1").style.display = "block";
                        document.getElementById("bt2").style.display = "none";

                        document.getElementById("form").style.display = "none";
                        aberto = aberto+1;
                        console.log(aberto)
                    } 
            }

            function abrir2(){

            if(aberto % 2 == 0){
                document.getElementById("bt3").style.display = "none";
                document.getElementById("bt4").style.display = "block";
                document.getElementById("lista").style.display = "block";

                aberto = aberto+1;
                console.log(aberto)
            }

            }

            function fechar2(){
                if(aberto % 2 != 0){
                    document.getElementById("bt3").style.display = "block";
                    document.getElementById("bt4").style.display = "none";
                    document.getElementById("lista").style.display = "none";
  
                    aberto = aberto+1;
                    console.log(aberto)
                } 
            }





        </script>
    </body>
</html>

<?php include("footer.php");?>
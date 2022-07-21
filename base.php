<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="style.css" >
    </head>
    
    <body>
        <section class="corpo">
            <div class="imagem">
                <div><a class="icone" onclick="openWin()"  ><img src="icones/add.png" alt="Adicionar uma imagem"></a> <h2>Adicionar</h2></div>
                
                <div><a class="icone"onclick="openWin3()" ><img src="icones/rmv.png" alt="Funções do programa"></a> <h2>Remover</h2></div>
                
                <div><a class="icone" onclick="openWin2()"><img src="icones/rename.png" alt="Efeitos na imagem"> </a><h2>Renomear</h2></div>
            </div>
        </section>
    </body>







    <script>

        function openWin() {window.open("modulo1/add.html", "", "width=300,height=300");}
        function openWin2() {window.open("modulo2/rename.php", "", "width=1000,height=500");}
        function openWin3() {window.open("modulo2/remove.php", "", "width=1000,height=500");}
        function f1(){
            document.getElementById('links').style.display = 'inline-block';
            document.getElementById("b2").style.display = 'inline-block';
            document.getElementById("b1").style.display = 'none';}   


    </script>



</html>
<?php include("footer.php");?> 
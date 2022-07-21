<?php
    if (isset ($funcao) && $funcao== 'resize'){
      
        $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . ' --resizeW ' . $width . ' --resizeH ' . $height);
        //echo $command;
        $saida =shell_exec($command);
        //$saida = shell_exec("dir");
        //echo $saida;
      
        };   
        
        

    if (isset ($funcao) && $funcao== 'toRgb'){
      
            $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
            //echo $command;
            $saida =shell_exec($command);
            //$saida = shell_exec("dir");
            //echo $saida;          
            };     

    if (isset ($funcao) && $funcao== 'cinza'){
      
                $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
                //echo $command;
                $saida =shell_exec($command);
                //$saida = shell_exec("dir");
                //echo $saida;          
                };    

    if (isset ($funcao) && $funcao== 'Hflip'){
      
                    $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
                    //echo $command;
                    $saida =shell_exec($command);
                    //$saida = shell_exec("dir");
                    //echo $saida;          
                    };    

                    
    if (isset ($funcao) && $funcao== 'Vflip'){
      
                        $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
                        //echo $command;
                        $saida =shell_exec($command);
                        //$saida = shell_exec("dir");
                        //echo $saida;          
                        };    
        
    
    
    
    
    
     if (isset ($funcao) && $funcao== 'rotacao'){
      
        $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel1 " . $variavel1);
        //echo $command;
        $saida =shell_exec($command);
        //$saida = shell_exec("dir");
        //echo $saida;          
        };   


            
     if (isset ($funcao) && $funcao== 'gamma'){
      
        $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel2 " . $variavel2);
        //echo $command;
        $saida =shell_exec($command);
        //$saida = shell_exec("dir");
        //echo $saida;          
        };   


            
     if (isset ($funcao) && $funcao== 'saturacao'){
      
        $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel2 " . $variavel2);
        //echo $command;
        $saida =shell_exec($command);
        //$saida = shell_exec("dir");
        //echo $saida;          
        };   



            
     if (isset ($funcao) && $funcao== 'brilho'){
      
        $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel2 " . $variavel2);
       // echo $command;
        $saida =shell_exec($command);
        //$saida = shell_exec("dir");
        //echo $saida;          
        };   
   
   
   
        if (isset ($funcao) && $funcao== 'contraste'){
      
         $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel2 " . $variavel2);
         //echo $command;
         $saida =shell_exec($command);
         //$saida = shell_exec("dir");
         //echo $saida;          
         };   
 


        if (isset ($funcao) && $funcao== 'info'){
      
            $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao);
            //echo $command;
            $saida =shell_exec($command);
            //$saida = shell_exec("dir");
            //echo $saida;          
            };  


   if (isset ($funcao) && $funcao== 'detec'){
      
               $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao);
               //echo $command;
               $saida =shell_exec($command);
               //$saida = shell_exec("dir");
              // echo $saida;          
               };  



   
   if (isset ($funcao) && $funcao== 'compress'){
      
      $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel3 " . $variavel3. " --variavel4 " . $variavel4);
      // echo $command;
      $saida =shell_exec($command);
      //$saida = shell_exec("dir");
      //echo $saida;          
      }; 



if (isset ($funcao) && $funcao== 'convert'){
      
         $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao . " --variavel3 " . $variavel3);
         // echo $command;
         $saida =shell_exec($command);
         //$saida = shell_exec("dir");
         //echo $saida;          
         }; 
   
   


if (isset ($funcao) && $funcao== 'sharpen'){
      
            $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
            // echo $command;
            $saida =shell_exec($command);
            //$saida = shell_exec("dir");
            //echo $saida;          
            }; 

if (isset ($funcao) && $funcao== 'sepia'){

   $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
   // echo $command;
   $saida =shell_exec($command);
   //$saida = shell_exec("dir");
   //echo $saida;          
   }; 


if (isset ($funcao) && $funcao== 'gaussianBlur'){

   $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
   // echo $command;
   $saida =shell_exec($command);
   //$saida = shell_exec("dir");
   //echo $saida;          
   }; 


if (isset ($funcao) && $funcao== 'emboss'){

   $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
   // echo $command;
   $saida =shell_exec($command);
   //$saida = shell_exec("dir");
   //echo $saida;          
   }; 



if (isset ($funcao) && $funcao== 'coldImage'){

   $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
   // echo $command;
   $saida =shell_exec($command);
   //$saida = shell_exec("dir");
   //echo $saida;          
   }; 

   


if (isset ($funcao) && $funcao== 'warmImage'){

   $command = escapeshellcmd('py main_argparse.py --imagem ' . $imagem .' --funcao '. $funcao );
   // echo $command;
   $saida =shell_exec($command);
   //$saida = shell_exec("dir");
   //echo $saida;          
   }; 
?>



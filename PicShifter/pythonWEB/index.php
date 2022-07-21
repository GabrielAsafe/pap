<?php
    $command = escapeshellcmd('python index.py');
    $output = shell_exec($command);
    echo $output;
?>
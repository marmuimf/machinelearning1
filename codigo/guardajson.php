<!-- toma lo que venga y lo guarda en un archivo json -->

<?php

    $datos = [
        'elemento' => $_GET['patron'],
        'datos' => $_GET['datos']
    ];
    $json = json_encode($datos,JSON_PRETTY_PRINT);
    $archivo = "datos/prueba.json";
    
    file_put_contents($archivo,$json);

?>
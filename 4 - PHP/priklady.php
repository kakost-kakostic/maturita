<?php

function bmi($weight, $height) {
    $bmi = $weight / ($height ** 2);
    echo "Tvé BMI je " . $bmi;
    if ($bmi < 19)
        echo " podváha";
    else if ($bmi <= 25)
        echo " normální váha";
    else if ($bmi <= 30)
        echo " mírná obezita";
    else if ($bmi <= 40)
        echo " silnější obezita";
    else
        echo " velká obezita";
}

function calculator($operation, $a, $b) {
    switch ($operation) {
        case "plus":
            $v = $a + $a;
            echo "Soucet = $v";
            break;
        case "minus":
            $v = $a - $a;
            echo "Rozdil = $v";
            break;
        case "krat":
            $v = $a * $a;
            echo "Soucin = $v";
            break;
        case "deleno":
            $v = $a / $a;
            echo "Podil = $v";
            break;
    }
}

function quadratic($a, $b, $c) {
    $D = $b * $b - 4 * $a * $c;
    if ($D >= 0)
        echo "Rovnice ma v R reseni";
    else
        echo "Rovnice nema v R reseni";
}

function drinks($drink) {
    echo "Vyøízení objednávky: " . $drink . "<br>";
    switch($drink){
        case "cola":
            echo "Vaše cola bude dodána do 5 minut";
            break;
        case "tonic":
            echo "Váš tonic bude dodán do 5 minut";
            break;
        case "juice":
            echo "Váš juice bude dodán do 5 minut";
            break;
        case "pivo":
            echo "Pivo podáváme pouze po dovršení 18 let ";
            break;
        case "sprite":
            echo "Váš sprite bude dodán do 5 minut";
            break;
        default:
            echo "Chyba";
            break;
    }
}


// tady se tridi requesty
    $method = $_SERVER['REQUEST_METHOD'] === 'POST' ? $_POST : $_GET;
        switch ($method['action']) {
            case 'bmi':
                bmi($_GET["weight"], $_GET["height"]);
                break;
            case 'calculator':
                calculator($_POST["operace"], $_POST["a"], $_POST["b"]);
                break;
            case 'quadratic':
                quadratic($_GET["a"], $_GET["b"], $_GET["c"]);
                break;
            case 'drinks':
                drinks($_POST["drink"]);
                break;
            default:
                echo "Unknown action";
        }


?>

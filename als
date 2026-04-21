html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taschenrechner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #333;
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
       .container {
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
        }
       .display {
            background-color: #444;
            color: #fff;
            border-radius: 10px 10px 0 0;
            padding: 10px;
            text-align: right;
            font-size: 2em;
            margin-bottom: 10px;
        }
       .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }
        button {
            background-color: #555;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover, button:active {
            background-color: #666;
        }
       .result {
            background-color: #444;
            color: #fff;
            border-radius: 10px 10px 0 0;
            padding: 10px;
            text-align: right;
            font-size: 2em;
            margin-top: 10px;
        }
       .keyboard {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
       .keyboard button {
            background-color: #555;
            color: #fff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
       .keyboard button:hover,.keyboard button:active {
            background-color: #666;
        }
       .keyboard button.enter {
            background-color: #ff5733;
            color: #fff;
        }
       .keyboard button.escape {
            background-color: #ff5733;
            color: #fff;
        }
       .keyboard button.backspace {
            background-color: #ff5733;
            color: #fff;
        }
       .keyboard button.plusminus {
            background-color: #ff5733;
            color: #fff;
        }
       .keyboard button.leftparentheses {
            background-color: #ff5733;
            color: #fff;
        }
       .keyboard button.rightparentheses {
            background-color: #ff5733;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container
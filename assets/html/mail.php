
<?php
    $name = $_POST['Nom'];
    $email = $_POST['Email'];
    $message = $_POST['message']; 
    $maitheader = "From:". $name."<". $email e.">\r\n";
    $recipient = "Thierryber64@gmail.com";
    mail($recipient, "Message site Internet", $message, $maitheader) or die("Error!");
    echo'
    <DOCTYPE html>
    <html lang="fr">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Accueil</title>
            <link rel="stylesheet" href="assets/styles/Portfolio.css">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v4.7.0/css/allcss">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
            <script src="https://smtpjs.com/v3/smtp.js"></script>
            <script type="text/javascript" src="assets/java/main.js"></script>
        </head>
        <body>            
            <div class="container">
                <h1>Thank you for contacting me. I will get back to you as
                soon as possible!</h1>
                <p class="back">Go back to the <a href="index.html">homepage</a>.</p>
            </div>
        </body>

    </html>


';
?>

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EXAMEN FINAL</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
                text-align: center;
            }
            p {
                color: #666;
                text-align: center;
                font-size: 18px;
            }
            img {
                display: block;
                margin: 20px auto;
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Jurado Paucar Hugo</h1>
            <p>Esta tarea merece un 20 profesor :)</p>
            <img src="https://e7.pngegg.com/pngimages/908/777/png-clipart-security-hacker-computer-security-certified-ethical-hacker-white-hat-hacker-tshirt-computer-network-thumbnail.png" alt="Hackers">
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)


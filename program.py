from flask import Flask, render_template, url_for, request

app = Flask(__name__)
photos = ['mars1.jpg', 'mars2.jpg', 'mars3.jpg']


@app.route('/galery', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        carousel = ''
        for i in range(len(photos)):
            carousel += f'<div class="carousel-item"><img class="d-block w-50" src="/static/img/{photos[i]}" alt="{i}slide"></div>\n'
        return f''' <!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" 
                                crossorigin="anonymous">
                            <title>Пейзажи Марса</title>
                        </head>
                        <body>
                            <h1>Колонизация Марса</h1>
                            <div class="alert alert-dark" role="alert"> И на Марсе будут яблони цвести </div>
                            <h1>Пейзажи Марса</h1>
                            <div id="carousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="200" data-bs-wrap="true">
                                <div class="carousel-inner">
                                    <div class="carousel-item active">
                                        <img class="d-block w-50" src="/static/img/mars0.jpg" alt="First slide">
                                    </div>
                                    {carousel}
                                </div>
                                <form class="login_form" method="post">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
                        </body>
                    </html>'''
    elif request.method == 'POST':
        photos.append(request.form['file'])
        return 'Картинка отправлена'

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


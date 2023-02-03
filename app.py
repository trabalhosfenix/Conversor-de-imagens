from flask import Flask, request, Response, render_template, make_response,url_for
from PIL import Image
import io

from io import BytesIO

app = Flask(__name__)
user = {'username': 'Visitante'}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', user=user)

@app.route('/jpgtopng', methods=['GET'])
def jpgtopng():
    return render_template('jpgtopng.html', input="JPG", output="PNG", title='JPG para PNG', user=user)

@app.route('/pngtojpg', methods=['GET'] )
def pngtojpg():
    return render_template('pngtojpg.html', input="PNG", output="JPG", title='PNG para JPG', user=user)

@app.route('/webptopng', methods=['GET'])
def webptopng():
    return render_template('webptopng.html', input="Webp", output="PNG", title='WEBP para PNG', user=user)

@app.route("/pngtowebp", methods=["GET"])
def pngtowebp():
     return render_template('pngtowebp.html', input="PNG", output="WEBP", title='PNG para WEBP', user=user)

@app.route('/bmptopng', methods=['GET'])
def bmptopng():    
    return render_template('bmptopng.html', input="BMP", output="PNG", title='BMP para PNG', user=user)

@app.route('/pngtobmp', methods=['GET'])
def pngtobmp():    
    return render_template('pngtobmp.html', input="PNG", output="BMP", title='PNG para BMP', user=user)


@app.route('/pngtopdf', methods=['GET'])
def pngtopdf():     
    return render_template('pngtopdf.html', input="PNG", output="PDF", title='PNG para PDF', user=user)

"""  <--------------------> """

@app.route("/conversor/api/pngtojpg", methods=["POST"])
def png_to_jpg():
    image = request.files["image"]
    image_name = image.filename.split(".")[0] + ".jpg"
    image = Image.open(image)
    image = image.convert("RGB")
    byte_io=io.BytesIO()
    image.save(byte_io,"jpeg" )
    byte_io.seek(0)   
    response = Response(byte_io, content_type="image/jpeg")
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})
    return response

@app.route("/conversor/api/jpgtopng", methods=["POST"])
def jpg_to_png():
    image = request.files["image"]
    image_name = image.filename.split(".")[0] + ".png"
    image = Image.open(image)
    image = image.convert("RGB")
    byte_io=io.BytesIO()
    image.save(byte_io,"PNG" )
    byte_io.seek(0)
    response=Response(byte_io, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})
    print(response.headers)
   
    return response

@app.route("/conversor/api/webptopng", methods=["POST"])
def webp_to_png():
    image = request.files["image"]
    image_name = image.filename.split(".")[0] + ".png"
    image = Image.open(image)
    image = image.convert("RGBA")
    byte_io=io.BytesIO()
    image.save(byte_io,"PNG" )
    byte_io.seek(0)
    response=Response(byte_io, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})
    return response

@app.route('/conversor/api/pngtowebp', methods=['POST'])
def png_to_webp():
    image = request.files['image']
    image_name = image.filename.split(".")[0] + ".webp"
    img = Image.open(image)
    buffer = io.BytesIO()
    img.save(buffer, format='WEBP')
    buffer.seek(0)

    response=Response(buffer, mimetype='image/webp')
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})

    return response

@app.route("/conversor/api/bmptopng", methods=["POST"])
def bmp_to_png():
    image = request.files["image"]
    image_name = image.filename.split(".")[0] + ".png"
    image = Image.open(image)
    image = image.convert("RGBA")
    byte_io=io.BytesIO()
    image.save(byte_io,"PNG" )
    byte_io.seek(0)
    response=Response(byte_io, content_type='image/png')
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})
    return response

@app.route("/conversor/api/pngtopdf", methods=["POST"])
def png_to_pdf():
    image = request.files["image"]
    image_name = image.filename.split(".")[0] + ".pdf"
    image = Image.open(image)  
    image = image.convert("RGB")  
    byte_io=io.BytesIO()
    image.save(byte_io,"PDF" )
    byte_io.seek(0)
    response=Response(byte_io, content_type='application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})
    return response

@app.route("/conversor/api/pngtobmp", methods=["POST"])
def png_to_bmp():
    image = request.files["image"]
    image_name = image.filename.split(".")[0] + ".bmp"
    image = Image.open(image)
    image = image.convert("RGB")
    byte_io=io.BytesIO()
    image.save(byte_io,"BMP" )
    byte_io.seek(0)
    response=Response(byte_io, content_type='image/bmp')
    response.headers.set('Content-Disposition', 'attachment', filename={image_name})
    print(response.headers)
   
    return response

if __name__ == '__main__':
     app.run(port=8000, host='0.0.0.0', debug=True, threaded=True)

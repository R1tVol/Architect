import random
import string
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/index")
def hello_world():
    return """<p>Hello, World!</p><br> <a href="/rastgelegercek">Rastgele bir gerçeği görüntüle!</a>"""

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/<int:length>')
def generate(length):
    password = generate_password(length)
    return render_template('generate.html', password=password)



@app.route("/anasayfa")
def anasayfa():
    return render_template("index.html")

@app.route("/rastgelegercek")
def rastgele_gercekler(): #farklı verilebilir
    facts_list=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar." ,
                "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."]

    return f'<p> {random.choice(facts_list)}</p>'

@app.route("/doviz")
def hava_durumu():
    return render_template("index.html")

app.run(debug=True)
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.app_context().push()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


class Countriesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    countryName = db.Column(db.String, unique=True, nullable=False)
    offName = db.Column(db.String)
    nativeName = db.Column(db.String)
    capital = db.Column(db.String)
    region = db.Column(db.String)
    subregion = db.Column(db.String)
    languages = db.Column(db.String)
    population = db.Column(db.Integer)
    area = db.Column(db.String)
    flags = db.Column(db.String)


with app.app_context():
    db.create_all()


# insert data to db

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    print(request.form)
    user_input = request.form['country'].capitalize()
    url = 'https://restcountries.com/v3.1/name/' + user_input
    r = requests.get(url)
    countData = r.json()[0]
    asd = (countData['cioc']).lower()
    offName = countData['name']['official']
    nativeName = countData['name']['nativeName'][f'{asd}']['official']
    capital = countData['capital'][0]
    language = countData['languages'][f'{asd}']
    area = countData['area']
    population = countData['population']
    flag = countData['flags']['png']
    region = countData['region']
    subregion = countData['subregion']

    country = Countriesa(countryName=user_input,
                         offName=offName,
                         nativeName=nativeName,
                         capital=capital,
                         population=population,
                         languages=language,
                         area=area,
                         flags=flag,
                         region=region,
                         subregion=subregion)
    db.session.add(country)
    db.session.commit()

    name = capital
    key = '3fd8f01f267e3cfb07040c714fcb7cd3'
    wrurl = f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={key}&units=metric'
    response = requests.get(wrurl)
    data = response.json()
    curr_temp = round(data['main']['temp'])
    icon = data['weather'][0]['icon']

    return render_template('result.html',
                           curr_temp=curr_temp,
                           name=name,
                           icon=icon,
                           offName=offName,
                           nativeName=nativeName,
                           flag=flag,
                           capital=capital,
                           language=language,
                           area=area,
                           population=population,
                           region=region,
                           subregion=subregion)


if __name__ == '__main__':
    app.run(debug=True)

    print(Countriesa.query.all())

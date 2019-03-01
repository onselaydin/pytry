from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

#Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("isim soyisim",validators=[validators.length(min=4,max=50),validators.DataRequired])
    email = StringField("eposta",validators=[validators.Email(message="Mail adresi hatalı...")])
    username = StringField("kullanıcı adı",validators=[validators.length(min=4,max=50),validators.DataRequired])
    password = PasswordField("Parola",validators=[
        validators.DataRequired(message="Parola giriniz"),
        validators.EqualTo(fieldname = "confirm", message="Parola uyuşmuyor.")
    ])
    confirm = PasswordField("Parola Doğrula")

app = Flask(__name__)

app.config["MYSQL_HOST"] = "104.248.188.200"
app.config["MYSQL_PORT"] = "3306"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Onsel123"
app.config["MYSQL_DB"] = "OnBlog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    numbers = [1,2,3,4,5]
    return render_template("index.html", answer = "evet",numbers=numbers)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/article/<string:id>")
def detail(id):
    return "Article id " + id

#kullanıcı kayıt
@app.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST":
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)
        cursor = mysql.connect.cursor()
        sorgu = "Insert into users(name, email, username, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sorgu,(name, email, username, password))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("index"))
    else:
        return render_template("register.html", form = form)
    

if __name__ == "__main__":
    app.run(debug=True)

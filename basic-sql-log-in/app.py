from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from passlib.hash import sha256_crypt

#use venv to pip3 install depends.

engine = create_engine("mysql+pymysql://root:pythonsql@localhost/register")
db = scoped_session(sessionmaker(bind=engine))
                        #(mypysql+pymysql://username:password@localhost/databasename) 

#mysql -u root -p
#pythonsql(pw)
# CREATE TABLE users(id SERIAL PRIMARY KEY, role varchar(50), email varchar(50), name varchar(50), username varchar(50), pasword varchar(300));

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method == "POST":
        role = request.form.get("role")
        email = request.form.get("email")
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password)) #salts the pasword :)

        if password != confirm:
             flash("password does not match","danger")
             return redirect(url_for('register'))

        else:
            db.execute("INSERT INTO users(role, email, name, username, password) VALUES(:role, :email, :name, :username, :password)",
                                        {"role":role,"email":email,"name":name,"username":username,"password":secure_password})
            db.commit()
            return redirect(url_for('login'))

    return render_template("auth/register.html")

@app.route('/login')
def login():
    return render_template("auth/login.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import folium
import matplotlib.pyplot as plt
import io
import base64
import random
import pandas as pd

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

# config mysql connection -LOCAL-

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = '888999'
#app.config['MYSQL_DB'] = 'myflaskapp'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# config mysql connection -HEROKU CLEARDB MYSQL FOR WEB-
app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'b6080df764cd13'
app.config['MYSQL_PASSWORD'] = '98a88023'
app.config['MYSQL_DB'] = 'heroku_6a634f65adc2eaa'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# initialize mysql
mysql = MySQL(app)

#Articles = Articles()

#plot semua bencana
@app.route('/trialpage/plot', methods=["GET"])
def plotView():
    # Generate plot
    #length=10
    #randomnumber1 = random.sample(range(-20,20),length)
    #randomnumber2 = random.sample(range(10,50),length)
    korban = pd.read_excel('korban.xlsx')              #Path filenya gaada
    fig = Figure()
    #plt.style.use('dark_background')
    axis = fig.add_subplot(1, 1, 1) 
    axis.set_title("Disaster occurences in West Java")
    axis.set_xlabel("Year")
    axis.set_ylabel("Number of occurences")
    #axis.grid()
    #axis.bar(randomnumber1, randomnumber2)
    axis.bar(korban.Tahun, korban.Banjir)
    axis.bar(korban.Tahun, korban.TanahLongor)
    axis.bar(korban.Tahun, korban.GempaBumi)
    axis.bar(korban.Tahun, korban.GunungApi)
    axis.legend(['Flood', 'Landslide', 'Earthquake', 'Volcanic Eruption'])
    axis.set_xlim(2011,2019)
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("plot.html", image=pngImageB64String)

#plot banjir
@app.route('/trialpage/banjir', methods=["GET"])
def plotbanjir():
    korban = pd.read_excel('korban.xlsx')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1) 
    axis.set_title("Flood occurences in West Java")
    axis.set_xlabel("Year")
    axis.set_ylabel("Number of Occurences")
    #axis.grid()
    axis.bar(korban.Tahun, korban.Banjir)
    axis.set_xlim(2011,2019)
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:banjir/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("plot.html", image=pngImageB64String)

#plot longsor
@app.route('/trialpage/longsor', methods=["GET"])
def plotlongsor():
    korban = pd.read_excel('korban.xlsx')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1) 
    axis.set_title("Lanslide occurences in West Java")
    axis.set_xlabel("Year")
    axis.set_ylabel("Number of Occurences")
    #axis.grid()
    axis.bar(korban.Tahun, korban.TanahLongor, color='orange')
    axis.set_xlim(2011,2019)
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:longsor/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("plot.html", image=pngImageB64String)

#plot gempa
@app.route('/trialpage/gempa', methods=["GET"])
def plotgempa():
    korban = pd.read_excel('korban.xlsx')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1) 
    axis.set_title("Earthquake occurences in West Java")
    axis.set_xlabel("Year")
    axis.set_ylabel("Number of Occurences")
    #axis.grid()
    axis.bar(korban.Tahun, korban.GempaBumi, color=['green'])
    axis.set_xlim(2011,2019)
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:gempa/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("plot.html", image=pngImageB64String)

#plot gunung
@app.route('/trialpage/gunung', methods=["GET"])
def plotgunung():
    korban = pd.read_excel('korban.xlsx')
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1) 
    axis.set_title("Volcanic eruption occurences in West Java")
    axis.set_xlabel("Year")
    axis.set_ylabel("Number of Occurences")
    #axis.grid()
    axis.bar(korban.Tahun, korban.GunungApi, color=['red'])
    axis.set_xlim(2011,2019)
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:gunung/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("plot.html", image=pngImageB64String)

#index
@app.route('/') 
def index():
    return render_template('home2.html')

#about
@app.route('/about')
def about():
    return render_template('about.html')

#team
@app.route('/team')
def team():
    return render_template('team.html')

#Overview
@app.route('/overview')
def overview():
    return render_template('overview.html')

#trialpage
@app.route('/trialpage')
def trial():
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        return render_template('plot.html', x=x, y=y)
    return render_template('trial.html')

#Article
@app.route('/articles')
def articles():
    # Create Cursor
    cur =  mysql.connection.cursor()
    
    # Get articles
    result = cur.execute("SELECT * FROM articles")
    
    articles = cur.fetchall()
    
    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)
    
    # close connection
    cur.close()  

# Single Article
@app.route('/article/<string:id>/')
def article(id):
    # Create Cursor
    cur =  mysql.connection.cursor()
    
    # Get article
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    
    article = cur.fetchone()
    
    return render_template('article.html', article=article)

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
    
# User Register    
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
        
        # Create Cursor
        cur = mysql.connection.cursor()
        
        #execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        
        #commit to DB
        mysql.connection.commit()
        
        #Close connection
        cur.close()
        
        flash('You Are Now Registered and can log in', 'success')
        
        return redirect(url_for('login'))
        
        #return render_template('register.html')
    return render_template('register.html', form=form)

# User Login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        
        # Create cursor
        cur = mysql.connection.cursor()
        
        # Get User by Username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
    
        
        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']
            
            # Compare password from database and input
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username
                
                flash('You are now logged in', 'success')
                #return redirect(url_for('dashboard'))
                return redirect("https://gheoportfolio.herokuapp.com/", code=302)
            else:
                error = 'Invalid Login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login First', 'danger')
            return redirect(url_for('login'))
    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard 
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create Cursor
    cur =  mysql.connection.cursor()
    
    # Get articles
    result = cur.execute("SELECT * FROM articles")
    
    articles = cur.fetchall()
    
    if result > 0:
        return render_template('dashboard.html', articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)
    
    # close connection
    cur.close()  
        
    
    

# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
    author = StringField('Name', [validators.Length(min=1, max=200)])


# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
#@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        author = form.author.data
        
        
        # Create Cursor
        cur = mysql.connection.cursor()
        
        
        # Execute Cursor
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, author))
        
        
        # Commit to DB
        mysql.connection.commit()
        
        # Close Connection
        cur.close()
        
        flash('Article Successfully Created', 'success')
        
        return redirect(url_for('articles'))

    return render_template('add_article.html', form=form)


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create Cursor
    cur = mysql.connection.cursor()
    
    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    
    article = cur.fetchone()

    # Get Form    
    form = ArticleForm(request.form)
    
    
    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']
    form.author.data = article['author']
    
    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']
        author = request.form['author']
        
        
        # Create Cursor
        cur = mysql.connection.cursor()
        
        
        # Execute Cursor
        cur.execute("UPDATE articles SET title=%s, body=%s WHERE id = %s", (title, body, id))
        
        
        # Commit to DB
        mysql.connection.commit()
        
        # Close Connection
        cur.close()
        
        flash('Article Successfully Updated', 'success')
        
        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)    

# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = mysql.connection.cursor()
    
    # execute
    cur.execute("DELETE FROM articles WHERE id = %s", [id])
    
     # Commit to DB
    mysql.connection.commit()
        
    # Close Connection
    cur.close()
    
    flash('Article Successfully Deleted', 'success')
    
    return redirect(url_for('dashboard'))
    

#TEMPORARILY UNWRAPS THE CONTENT INSIDE SESSION LOGIN == TRUE

# Peta Resiko Bencana
@app.route('/peta')
#@is_logged_in
def peta():
    return render_template('pilihanpeta.html')

# Peta Semua Bencana
@app.route('/peta/semuabencana')
#@is_logged_in
def semua():
    return render_template('peta.html')

# Peta Semua Bencana
@app.route('/peta/bencanagunungapi')
#@is_logged_in
def petagunung():
    return render_template('petagunung.html')

# Peta Semua Bencana
@app.route('/peta/bencanabanjir')
#@is_logged_in
def petabanjir():
    return render_template('petabanjir.html')

# Peta Semua Bencana
@app.route('/peta/bencanagempa')
#@is_logged_in
def petagempa():
    return render_template('petagempa.html')

# Peta Semua Bencana
@app.route('/peta/bencanalongsor')
#@is_logged_in
def petalongsor():
    return render_template('petalongsor.html')

# Peta Gudang BUlog
@app.route('/peta/bulog')
#@is_logged_in
def petabulog():
    return render_template('petabulog.html')


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug = True)

from flask import Flask, render_template,session,url_for, request, redirect

app = Flask(__name__)
app.secret_key = "fnjkfksjbsk"
database = {
  'madan':{
    'password': '12345',
    'enrolled': 'dataScience',
    'enrolled_date': 12,
    'enrolled_month' :'January',
    'enrolled_year' : 2024,
    'phone_no' : '9735645848',
    'enroll_course' : None
  }
}
@app.route('/', methods = ['GET','POST'])
def login():
   if request.method =='POST':
    user = request.form['username']
    password = request.form['password']
    if user in database and database[user]['password']==password:
      session['username']= user
      return redirect(url_for('home'))

   return render_template('login.html')

@app.route('/home',methods =['GET','POST'])
def home():
   if request.method== 'POST':
     if request.form['submit'] == 'logout':
      session.pop("username",None) 
      return redirect(url_for('login'))
   user = session['username'] 
   return render_template("home.html",user = user)



@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == "POST":
       user = request.form['username']
       password = request.form['password']
       phone_number = request.form['phone']
       if user not in database:
         
         database[user] = {'password': str(password), 'phone_no': str(phone_number)}
         session['username'] = user
         return redirect(url_for('home'))
              

    return render_template('signup.html')






if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

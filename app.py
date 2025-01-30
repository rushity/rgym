from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Notes Page
@app.route('/notes')
def notes():
    return render_template('notes.html')

# Important Questions Page
@app.route('/important')
def important():
    return render_template('important.html')

# Sample Papers Page
@app.route('/papers')
def papers():
    return render_template('papers.html')

# Contact Page (with form)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}, your message is received!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
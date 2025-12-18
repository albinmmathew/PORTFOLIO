import os
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_dev_key')  # Secure key for production, default for dev

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you would typically send an email or save to database
        print(f"New Contact Message!\nName: {name}\nEmail: {email}\nMessage: {message}")
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('index') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)

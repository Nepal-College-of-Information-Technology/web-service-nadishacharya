from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
print("Starting Flask app...")

app = Flask(__name__)
db = TinyDB('db.json')
User = Query()

@app.route('/')
def index():
    users = db.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    db.insert({'name': name, 'email': email})
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>')
def edit(item_id):
    user = db.all()[item_id]
    return render_template('edit.html', user=user, id=item_id)

@app.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    name = request.form['name']
    email = request.form['email']
    db.update({'name': name, 'email': email}, doc_ids=[db.all()[item_id].doc_id])
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    db.remove(doc_ids=[db.all()[item_id].doc_id])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

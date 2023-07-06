from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your_password'  # Replace with your password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    urgency = db.Column(db.String(50), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    action_taken = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    all_data = Data.query.all()
    return render_template('index.html', data=all_data)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        ticket = request.form['ticket']
        owner = request.form['owner']
        urgency = request.form['urgency']
        issue_description = request.form['issue_description']
        action_taken = request.form['action_taken']

        new_data = Data(ticket=ticket, owner=owner, urgency=urgency, issue_description=issue_description, action_taken=action_taken)

        db.session.add(new_data)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/delete/<int:id>')
def delete(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    data = Data.query.get_or_404(id)
    if request.method == 'POST':
        data.ticket = request.form['ticket']
        data.owner = request.form['owner']
        data.urgency = request.form['urgency']
        data.issue_description = request.form['issue_description']
        data.action_taken = request.form['action_taken']

        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', data=data)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        results = Data.query.filter(Data.ticket == query).all()
        return render_template('search_results.html', results=results)
    else:
        return render_template('search.html')

@app.route('/email', methods=['GET', 'POST'])
def email_records():
    if request.method == 'POST':
        # request.form is a dictionary-like object that contains all form parameters
        email_address = request.form['email']
        ids = request.form.getlist('ids')

        # Fetch records
        records = Data.query.filter(Data.id.in_(ids)).all()

        # Format records and send email
        email_body = format_records(records)
        send_email(email_address, "Selected Records", email_body)

        return redirect('/')
    else:
        ids = request.args.getlist('ids')
        return render_template('enter_email.html', ids=ids)

def format_records(records):
    email_body = ""
    for record in records:
        email_body += f"ID: {record.id}, Ticket: {record.ticket}, Owner: {record.owner}, Urgency: {record.urgency}, Issue Description: {record.issue_description}, Action Taken: {record.action_taken}\n"
    return email_body

def send_email(to, subject, body):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.body = body
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug=True)

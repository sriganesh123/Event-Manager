from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import schedule
from zoneinfo import ZoneInfo
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import current_app




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'arjulasriganesh@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'cgysoebylsdzpfci'  # Replace with your password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
db = SQLAlchemy(app)
mail = Mail(app)
scheduler = BackgroundScheduler()
    
class Data1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    urgency = db.Column(db.String(50), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    action_taken = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
class Data2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    urgency = db.Column(db.String(50), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    action_taken = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
class Data3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    urgency = db.Column(db.String(50), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    action_taken = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    


with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
    
@app.route('/table1', methods=['GET'])
def table1():
    all_data1 = Data1.query.all()
    return render_template('table1.html', data=all_data1)

@app.route('/table2', methods=['GET'])
def table2():
    all_data2 = Data2.query.all()
    return render_template('table2.html', data=all_data2)

@app.route('/table3', methods=['GET'])
def table3():
    all_data3 = Data3.query.all()
    return render_template('table3.html', data=all_data3)

@app.route('/table1/create', methods=['GET', 'POST'])
def create1():
    if request.method == 'POST':
        ticket = request.form['ticket']
        owner = request.form['owner']
        urgency = request.form['urgency']
        issue_description = request.form['issue_description']
        action_taken = request.form['action_taken']
        created_at = datetime.now()

        new_data = Data1(ticket=ticket, owner=owner, urgency=urgency, issue_description=issue_description, action_taken=action_taken,created_at=created_at)

        db.session.add(new_data)
        db.session.commit()
        return redirect('/table1')
    else:
        return render_template('table1/create.html')

@app.route('/table2/create', methods=['GET', 'POST'])
def create2():
    if request.method == 'POST':
        ticket = request.form['ticket']
        owner = request.form['owner']
        urgency = request.form['urgency']
        issue_description = request.form['issue_description']
        action_taken = request.form['action_taken']
        created_at = datetime.now()

        new_data2 = Data2(ticket=ticket, owner=owner, urgency=urgency, issue_description=issue_description, action_taken=action_taken,created_at=created_at)

        db.session.add(new_data2)
        db.session.commit()
        return redirect('/table2')
    else:
        return render_template('/table2/create.html')


@app.route('/table3/create', methods=['GET', 'POST'])
def create3():
    if request.method == 'POST':
        ticket = request.form['ticket']
        owner = request.form['owner']
        urgency = request.form['urgency']
        issue_description = request.form['issue_description']
        action_taken = request.form['action_taken']
        created_at = datetime.now()

        new_data3 = Data3(ticket=ticket, owner=owner, urgency=urgency, issue_description=issue_description, action_taken=action_taken,created_at=created_at)

        db.session.add(new_data3)
        db.session.commit()
        return redirect('/table3')
    else:
        return render_template('table3/create.html')

@app.route('/table1/update/<int:id>', methods=['GET', 'POST'])
def update_table1(id):
    data = Data1.query.get_or_404(id)
    if request.method == 'POST':
        data.ticket = request.form['ticket']
        data.owner = request.form['owner']
        data.urgency = request.form['urgency']
        data.issue_description = request.form['issue_description']
        data.action_taken = request.form['action_taken']

        db.session.commit()
        return redirect('/table1')
    else:
        return render_template('table1/update.html', data=data)
        
@app.route('/table2/update/<int:id>', methods=['GET', 'POST'])
def update_table2(id):
    data = Data2.query.get_or_404(id)
    if request.method == 'POST':
        data.ticket = request.form['ticket']
        data.owner = request.form['owner']
        data.urgency = request.form['urgency']
        data.issue_description = request.form['issue_description']
        data.action_taken = request.form['action_taken']

        db.session.commit()
        return redirect('/table2')
    else:
        return render_template('table2/update.html', data=data)
        
@app.route('/table3/update/<int:id>', methods=['GET', 'POST'])
def update_table3(id):
    data = Data3.query.get_or_404(id)
    if request.method == 'POST':
        data.ticket = request.form['ticket']
        data.owner = request.form['owner']
        data.urgency = request.form['urgency']
        data.issue_description = request.form['issue_description']
        data.action_taken = request.form['action_taken']

        db.session.commit()
        return redirect('/table3')
    else:
        return render_template('table3/update.html', data=data)



@app.route('/table1/delete/<int:id>')
def delete1(id):
    data = Data1.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/table1')
    
@app.route('/table2/delete/<int:id>')
def delete2(id):
    data = Data2.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/table2')
    
@app.route('/table3/delete/<int:id>')
def delete3(id):
    data = Data3.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/table3')


@app.route('/table1/search', methods=['GET', 'POST'])
def search1():
    if request.method == 'POST':
        query = request.form.get('query')
        results = Data1.query.filter(Data1.ticket == query).all()
        return render_template('table1/search_results.html', results=results)
    else:
        return render_template('table1/search.html')
        
@app.route('/table2/search', methods=['GET', 'POST'])
def search2():
    if request.method == 'POST':
        query = request.form.get('query')
        results = Data2.query.filter(Data2.ticket == query).all()
        return render_template('search_results.html', results=results)
    else:
        return render_template('table2/search.html')

@app.route('/table3/search', methods=['GET', 'POST'])
def search3():
    if request.method == 'POST':
        query = request.form.get('query')
        results = Data3.query.filter(Data3.ticket == query).all()
        return render_template('table3/search_results.html', results=results)
    else:
        return render_template('table3/search.html')

@app.route('/table1/email', methods=['GET', 'POST'])
def email_records1():
    if request.method == 'POST':
        email_address = request.form['email']
        ids = request.form.getlist('ids[]')  # Updated to getlist() for array values
        
        # Convert non-empty IDs to integers
        id_list = [int(id) for id in ids if id]

        # Fetch records
        records = Data1.query.filter(Data1.id.in_(id_list)).all()

        # Format records and send email
        table_name = "Table 1"  # Replace with the appropriate table name
        email_body = format_records(records, table_name)
        send_email(email_address, "Selected Records", email_body)


        return redirect('/')
    else:
        ids = request.args.getlist('ids[]')
        return render_template('table1/enter_email.html', ids=ids)

        
@app.route('/table2/email', methods=['GET', 'POST'])
def email_records2():
    if request.method == 'POST':
        email_address = request.form['email']
        ids = request.form.getlist('ids[]')  # Updated to getlist() for array values
        
        # Convert non-empty IDs to integers
        id_list = [int(id) for id in ids if id]

        # Fetch records
        records = Data2.query.filter(Data2.id.in_(id_list)).all()

        # Format records and send email
        table_name = "Table 2"  # Replace with the appropriate table name
        email_body = format_records(records, table_name)
        send_email(email_address, "Selected Records", email_body)


        return redirect('/')
    else:
        ids = request.args.getlist('ids[]')
        return render_template('table2/enter_email.html', ids=ids)
     
        
@app.route('/table3/email', methods=['GET', 'POST'])
def email_records3():
    if request.method == 'POST':
        email_address = request.form['email']
        ids = request.form.getlist('ids[]')  # Updated to getlist() for array values
        
        # Convert non-empty IDs to integers
        id_list = [int(id) for id in ids if id]

        # Fetch records
        records = Data3.query.filter(Data3.id.in_(id_list)).all()

        # Format records and send email
        table_name = "Table 3"  # Replace with the appropriate table name
        email_body = format_records(records, table_name)
        send_email(email_address, "Selected Records", email_body)


        return redirect('/')
    else:
        ids = request.args.getlist('ids[]')
        return render_template('table3/enter_email.html', ids=ids)


def format_records(records, table_name):
    email_body = f"<h2>{table_name}</h2>"
    email_body += "<table style='width: 100%; border-collapse: collapse;'>"
    email_body += "<tr><th>ID</th><th>Ticket</th><th>Owner</th><th>Urgency</th><th>Issue Description</th><th>Action Taken</th></tr>"
    
    for record in records:
        email_body += f"<tr><td>{record.id}</td><td>{record.ticket}</td><td>{record.owner}</td><td>{record.urgency}</td><td>{record.issue_description}</td><td>{record.action_taken}</td></tr>"
    
    email_body += "</table>"
    
    return email_body


    
def send_email(to, subject, body):
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = f"""
    <html>
    <head>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                text-align: left;
                padding: 8px;
                border: 1px solid #ccc;
            }}
            th {{
                background-color: #f5f5f5;
            }}
        </style>
    </head>
    <body>
        {body}
    </body>
    </html>
    """
    mail.send(msg)

def send_email_with_data():
    with app.app_context():  # Use your Flask app instance here
        # Fetch the data from tables for the past 24 hours
        tz = ZoneInfo('US/Central')  # Replace with the appropriate timezone
        end_time = datetime.now(tz)
        start_time = end_time - timedelta(hours=24)

        data1_records = Data1.query.filter(Data1.created_at >= start_time, Data1.created_at <= end_time).all()
        data2_records = Data2.query.filter(Data2.created_at >= start_time, Data2.created_at <= end_time).all()
        data3_records = Data3.query.filter(Data3.created_at >= start_time, Data3.created_at <= end_time).all()

        # Format the data as HTML
        email_body = "<h2>Data for the Past 24 Hours</h2>"
        email_body += format_records(data1_records, "Table 1")
        email_body += format_records(data2_records, "Table 2")
        email_body += format_records(data3_records, "Table 3")

        # Set the subject with the last 24-hour date and starting/ending time
        start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
        end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")
        subject = f"Data for the Past 24 Hours ({start_time_str} - {end_time_str})"

        # Send the email
        send_email("bruce.wayne0459@gmail.com", subject, email_body)


def format_records1(records, table_name):
    email_body = f"<h3>{table_name}</h3>"
    email_body += "<table style='width: 100%; border-collapse: collapse;'>"
    email_body += "<tr><th>ID</th><th>Ticket</th><th>Owner</th><th>Urgency</th><th>Issue Description</th><th>Action Taken</th></tr>"
    
    for record in records:
        email_body += f"<tr><td>{record.id}</td><td>{record.ticket}</td><td>{record.owner}</td><td>{record.urgency}</td><td>{record.issue_description}</td><td>{record.action_taken}</td></tr>"
    
    email_body += "</table>"
    
    return email_body
def schedule_email_tasks():
    schedule.every().day.at("11:30").do(send_email_with_data)
    schedule.every().day.at("19:30").do(send_email_with_data)

# Run the scheduler in the background
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for 1 minute before checking the schedule again
    
if __name__ == "__main__":
    scheduler.add_job(send_email_with_data, 'cron', hour='11,19', minute=30)
    scheduler.start()
    app.run(debug=True)
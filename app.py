from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

import urllib.parse

app = Flask(__name__)

# 1. Database Configuration
# Replace with your actual MySQL connection string or use an environment variable
# Format: mysql+pymysql://username:password@host:port/database_name



# Manually encode the password or the whole string
password = urllib.parse.quote_plus("hteapp@123#")
db_uri = f"mysql+pymysql://hteapp:{password}@10.68.128.254/test"

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", db_uri)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

# 2. Define the Counter Model
class PageVisit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

# Create the table (Run this once or use a migration)
with app.app_context():
    db.create_all()
    # Initialize counter if table is empty
    if not PageVisit.query.first():
        db.session.add(PageVisit(count=0))
        db.session.commit()

@app.route('/')
def resume():
    # 3. Logic to update counter
    #  counter_record = PageVisit.query.first()
    # counter_record.count += 1
    # db.session.commit()
    
    # current_visits = counter_record.count 
    current_visits =  568;
    data = {
        "name": "Rohit Jain",
        "title": "Full Stack Developer & AI Automation Architect",
        "location": "Jaipur, Rajasthan",
        "experience": "9+ Years",
        "skills": ["Ollama", "LangChain", "n8n", "Laravel", "Python", "React", "MySQL", "PHP"],
        "visits": current_visits  # Pass the count to the template
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
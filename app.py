from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def resume():
    data = {
        "name": "Rohit Jain",
        "title": "Full Stack Developer & AI Automation Architect",
        "location": "Jaipur, Rajasthan",
        "experience": "9+ Years",
        "skills": ["Ollama", "LangChain", "n8n", "Laravel", "Python", "React", "MySQL", "PHP"]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
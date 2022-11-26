from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Sushovan Shakya',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'November 24, 2022'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'November 23, 2022'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
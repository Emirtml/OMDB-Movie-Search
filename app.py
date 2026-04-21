from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#apı key pasword 
API_KEY = "7df3091"

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_data = None
    if request.method == 'POST':
        movie_name = request.form.get('movie_name')
        if movie_name:
            url = f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"
            response = requests.get(url)
            movie_data = response.json()
    return render_template('index.html', movie=movie_data)

if __name__ == '__main__':
    app.run(debug=True)
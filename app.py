from flask import Flask
import pyjokes

app=Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    joke=pyjokes.get_joke()
    return f'<h2>{joke}</h2>'

@app.route("/MultipleJokes",methods=['GET'])
def jokes():
    jokes="<br><br>".join(pyjokes.get_jokes())
    return f'<h3>{jokes}</h3>'

if __name__=="__main__":
    app.run()
    

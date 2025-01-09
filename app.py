from flask import Flask
import pyjokes

app = Flask(__name__)

# Inline CSS with colors, more contrast, and animations
css_style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            text-align: center;
            padding: 40px;
            margin: 0;
            animation: fadeIn 1.5s ease-in;
        }
        h2 {
            color: #ff6347;  /* Tomato color for the heading */
            background-color: #fff8dc;  /* Cornsilk background for the heading */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h3 {
            color: #4682b4;  /* SteelBlue for multiple jokes */
            background-color: #e0ffff;  /* Light cyan background */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .jokes-container {
            margin-top: 30px;
            padding: 10px;
            background: linear-gradient(145deg, #A5DE2D, #B8BE25);  /* Gradient color */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            animation: slideIn 1.5s ease-out;
        }
        .joke-item {
            margin: 15px 0;
            padding: 20px;
            background-color: #2596BE;
            color: #333;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, transform 0.3s ease;
            animation: fadeInUp 0.5s ease-in-out;
        }
        .joke-item:hover {
            background-color:#A5DE2D;  /* LightCoral on hover for contrast */
            transform: translateY(-5px);
            animation: bounce 0.6s ease-in-out;
        }
        .joke-item p {
            font-size: 18px;
        }
        .joke-button {
            padding: 10px 20px;
            background-color: #A5DE2D;  /* LimeGreen button */
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }
        .joke-button:hover {
            background-color: #228b22;  /* ForestGreen on hover */
            transform: scale(1.1);  /* Slight scale effect on hover */
            animation: pulse 1s ease-in-out infinite;  /* Pulse effect */
        }

        /* Animations */
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes slideIn {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes bounce {
            0% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
            100% {
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.1);
            }
            100% {
                transform: scale(1);
            }
        }
    </style>
"""

@app.route("/", methods=['GET'])
def home():
    joke = pyjokes.get_joke()
    return f'''
    {css_style}
    <h2>Here's a Joke for You:</h2>
    <div class="joke-item">
        <p>{joke}</p>
    </div>
    <button class="joke-button" onclick="window.location.href='/MultipleJokes'">Get More Jokes</button>
    '''

@app.route("/MultipleJokes", methods=['GET'])
def jokes():
    jokes_list = "<br>".join([f'<div class="joke-item"><p>{joke}</p></div>' for joke in pyjokes.get_jokes()])
    return f'''
    {css_style}
    <h3>Here are some jokes for you:</h3>
    <div class="jokes-container">
        {jokes_list}
    </div>
    <button class="joke-button" onclick="window.location.href='/'">Back to Single Joke</button>
    '''

if __name__ == "__main__":
    app.run(debug=True)

## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number. Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

from flask import Flask, render_template, request


app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'
@app.route('/question')
def question():
    html_form = '''
    <html>
    <body>
    <form method="GET" action="http://localhost:5000/question-result">
        <label>Enter Your Favorite Number:
            <input name="num" value="0" type="number">
        </label></br>
        <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return html_form
@app.route('/question-result', methods = ['GET', 'POST'])
def displayQuestion():
    if request.method == "GET":
        result = request.args
        num = int(result.get("num"))
        strnum = str(num * 2)
        return "<h1>Double your favorite number is {}</h1>".format(strnum)




## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application. It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. If a user has to select a radio button representing a song name, it should do a search for that song in an API.
# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

@app.route('/nfl')
def nflQuiz():
    html_form = '''
    <html>
    </body>
    <form method="GET" action="http://localhost:5000/nfl-answer"> What active QB has the most 4th quarter comebacks since 2011 in the NFL? <br>
     <input type="radio" name="qb" value="Matt Stafford" checked>Matt Stafford<br>
     <input type="radio" name="qb" value="Tom Brady"> Tom Brady<br>
     <input type="radio" name="qb" value="Matt Ryan"> Matt Ryan <br>
     <input type="submit" value="Submit">
    </form>
    </body>
    </html>
    '''
    return html_form
@app.route('/nfl-answer', methods = ['GET',"POST"])
def nflAnswer():
    if request.method == "GET":
        result = request.args
        if result.get("qb") == "Matt Stafford":
            return "<h1>Correct! Matt Stafford has 26 fourth quarter comebacks since 2011</h1>"
        else:
            return "<h1>Incorrect. Matt Stafford has more fourth quarter comebacks than {}</h1>".format(result.get("qb"))

if __name__ == '__main__':
    app.run()




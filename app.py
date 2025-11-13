from flask import Flask, render_template_string

app = Flask(__name__)


HTML_FORMAT = ''' 

<html>
<head>
<title> Karunya Page </title>
<style>

body {

background-color: pink;
color: black;
display: flex;
justify-content: center;
text-align: center;
}

.card {

background-color: black;
color: white;
text-align: center;
padding: 2em;
margin: auto;
}

</style>
</head>
<body>

<h1> This is Karunya Page! </h1>
<div class="card">

<p> This is a simple page. For showing docker and ci cd demo </p>
</div>
</body>
</html>

'''
# sixth commit

@app.route('/')
def home():
    return render_template_string(HTML_FORMAT)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# i am doing my second commit
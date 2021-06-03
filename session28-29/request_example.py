from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    print("Method", request.method)
    print("Args", request.args)
    print("Form", request.form)
    print("Files", request.files)
    print("Values", request.values)
    print("Json", request.json)
    print("Data", request.data)
    return {
        "Args": request.args,
        "Form": request.form,
        "Files": list(request.files.keys()),
        "Values": request.values,
        "Json": request.json,
        "data": request.data,
    }


# Run the app on localhost..
app.run()

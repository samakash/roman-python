from flask import Flask, render_template, request

from roman import Roman

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    print(request)
    print(request.form)
    print(request.args)
    roman: str = str(request.args.get("roman"))
    arabic: int = -1
    if roman != "None":
        arabic = Roman.convert(roman)
    print('roman: ' + roman + ', arabic: ' + str(arabic))
    return render_template("index.html", roman=roman, arabic=arabic)


if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request

app = Flask(__name__)


# クイズの問題、選択肢、正解
quiz_question = "一：「摩訶般若波羅蜜多心経」の次は？"
quiz_choices = [
    ("●■観自在菩薩"),
    ("色不異空空不異色"),
    ("無苦集滅道無智亦無得"),
    ("依般若波羅蜜多●故")
]
quiz_answer = "●■観自在菩薩"

# クイズのページを表示する
@app.route("/")
def quiz():
    return render_template("index.html", question=quiz_question, choices=quiz_choices)

# 回答を受け取り、正解かどうかを判定する
@app.route("/answer", methods=["POST"])
def answer():
    selected = request.form["answer"]
    if selected == quiz_answer:
        return "正解！"
    else:
        return render_template("try_again.html", question=quiz_question, choices=quiz_choices)

if __name__ == "__main__":
    app.run(debug=True)

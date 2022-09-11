from flask import Flask, render_template, request


myweb = Flask(__name__)  # 代表目前執行的模組

#00

@myweb.route("/")  # 函式的裝飾.供附加功能
def home():
    return render_template("home1.html")


@myweb.route("/resume")  # 函式的裝飾.供附加功能
def resume():
    return render_template("resume.html")


@myweb.route("/work")  # 函式的裝飾.供附加功能
def work():


    return render_template("work.html")


@myweb.route("/work2")  # 函式的裝飾.供附加功能
def work2():
    return render_template("work2.html")


# @myweb.route("/work3")  # 函式的裝飾.供附加功能
# def work3():
#     return render_template("work3.html")


if __name__ == "__main__":  # 主程式執行
    myweb.run()                # 啟動伺服器

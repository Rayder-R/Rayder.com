from flask import Flask, render_template
myweb = Flask(__name__) # 代表目前執行的模組

@myweb.route("/") # 函式的裝飾.供附加功能
def home():
    return render_template("home1.html")

@myweb.route("/resume") # 函式的裝飾.供附加功能
def resume():
    return render_template("resume.html")

@myweb.route("/home") # 函式的裝飾.供附加功能
def homet():
    return render_template("home.html")
    
@myweb.route("/text") # 函式的裝飾.供附加功能
def text():
    return render_template("text.html")


if __name__ == "__main__":  # 如果以主程式執行
    myweb.run()                # 立刻啟動伺服器
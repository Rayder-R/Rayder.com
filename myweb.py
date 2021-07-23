from flask import Flask
myweb=Flask(__name__) # 代表目前執行的模組

@myweb.route("/") # 函式的裝飾.供附加功能
def home():
    return 'Hollo'

if __name__ == "__main__":  # 如果以主程式執行
    myweb.debug = True  
    myweb.run()                # 立刻啟動伺服器
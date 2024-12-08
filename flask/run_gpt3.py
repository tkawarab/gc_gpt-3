import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../macaw"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../deepl"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../gpt3"))
from flask import Flask, render_template, request, Markup, send_from_directory
from flask_bootstrap import Bootstrap
from gpt3_model_class import question,check_logprobes
from translate import translate
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
bootstrap = Bootstrap(app)
admin_pass = os.getenv("ADMIN_PASS")
license_key = os.getenv("LICENSE_KEY")

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        answer = 'こんにちは！'
        ans_txt = Markup(answer.replace("\n","<br>").replace("。","。<br>"))
        return render_template('index.html', answer=ans_txt)
    elif request.method == 'POST':
        input_accuracy = request.form.get('ans_accuracy')
        global input_temperature
        if input_accuracy=="1":
            input_temperature = "0"
        elif input_accuracy=="2":
            input_temperature = "1"
        else:
            input_temperature = "0"
        input_length = request.form.get('ans_length')
        if input_length=="1":
            input_max_tokens = "300"
        elif input_length=="2":
            input_max_tokens = "3000"  
        else:
            input_max_tokens = "0"
        input_cnt = request.form.get('Count')
        input_key = request.form.get('AuthKey')
        if int(input_cnt)>=5 and input_key!=license_key:
            answer = '申し訳ございません。利用上限を超えました。'
            return answer
        input_text = request.form.get('InputText')
        if input_text=='':
            answer = 'テキストを入力してください'
            return answer
        ret = question("1",input_temperature,"1.0","0.0","0.0",input_text,input_max_tokens)
        ans_txt = ret
        print("user_input:" + input_text.replace("\n",";"))
        print("user_output:" + ret.replace("\n",";"))
        return ans_txt
@app.route('/unlimited', methods=['GET', 'POST'])
def unlimited():
    if request.method == 'GET':
        return render_template('unlimited.html')
    elif request.method == 'POST':
        input_password = request.form.get('Password')
        if input_password == admin_pass:
            return license_key
        else:
            return "unmatch"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

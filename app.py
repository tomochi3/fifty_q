from flask import Flask, request, render_template, jsonify
import logging
from questions import questions  # 質問データをインポート

app = Flask(__name__)

# ロガーの設定
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 全ての回答を取得
        answers = request.form
        results = []
        
        for i, question in enumerate(questions):
            answer = answers.get(f'answer_{i}', None)
            correct_answer = question['answer']
            if answer and int(answer) == correct_answer:
                results.append(f"質問{i+1}: 正解")
            else:
                results.append(f"質問{i+1}: 不正解")
        
        return render_template('result.html', question_results=zip(questions, results))

    
    return render_template('index.html', questions=questions)




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

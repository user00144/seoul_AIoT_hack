from flask import Flask, render_template, request, jsonify
from main import get_query_engine
app = Flask(__name__)

query_engine = get_query_engine()

# 대화 기록 저장
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html', conversation=conversation_history)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    
    # llamaindex를 이용해 답변 생성 (실제 query 시스템 코드 필요)
    response = query_engine.query(user_input)  # 실제 RAG 시스템의 답변
    
    # 대화 기록에 사용자 질문과 AI 답변 추가
    conversation_history.append({'user': user_input, 'bot': response.response})
    
    return jsonify({'user': user_input, 'bot': response.response})

if __name__ == '__main__':
    app.run(debug=True)

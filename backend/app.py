from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from openai import OpenAI
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app)  # 启用CORS

# 初始化OpenAI客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "sk-iolqvtrxjeusovlavrszafqsbxjghrurkhvgxlsepdouhoma"),
    base_url="https://api.siliconflow.cn/v1"
)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # 创建流式响应
        def generate():
            response = client.chat.completions.create(
                model="Qwen/Qwen2.5-72B-Instruct",
                messages=[{
                    "role": "user",
                    "content": user_message
                }],
                stream=True
            )

            for chunk in response:
                if not chunk.choices:
                    continue
                
                # 获取内容和推理内容
                content = chunk.choices[0].delta.content or ""
                reasoning = chunk.choices[0].delta.reasoning_content or ""
                
                # 发送数据
                yield f"data: {json.dumps({'content': content, 'reasoning': reasoning})}\n\n"

        return Response(generate(), mimetype='text/event-stream')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
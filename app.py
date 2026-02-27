from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import time

app = Flask(__name__)
CORS(app)

def run_tiktok_logic(url, count):
    """裏側でTikTokの処理を行うエンジン"""
    print(f"[MoneHUB] ターゲット: {url} へ {count}アカウントで接続開始")
    # ここに将来的にアカウント作成のコードを組み込みます
    time.sleep(5) 
    print("[MoneHUB] エンジンの処理が完了しました")

@app.route('/ignite', methods=['POST'])
def ignite():
    """サイトのボタンと通信する窓口"""
    try:
        data = request.json
        target_url = data.get('url')
        count = data.get('count')

        # サイトをフリーズさせないよう、裏側で処理を開始
        thread = threading.Thread(target=run_tiktok_logic, args=(target_url, count))
        thread.start()

        return jsonify({
            "status": "success", 
            "message": "API接続成功。MoneHUBエンジンを点火しました。"
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

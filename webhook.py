from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Kiểm tra nếu dữ liệu là push event
    if data.get('ref') == 'refs/heads/main':  # Thay 'main' bằng tên nhánh của bạn
        # Chạy lệnh để pull code mới từ Git
        subprocess.call(['git', '-C', 'git@github.com:HungLM1506/Test-CICD.git', 'pull'])
        # Chạy lệnh docker-compose để khởi động lại dịch vụ
        subprocess.check_call(['python3', 'data_loading.py'])
        subprocess.check_call(['python3', 'training.py'])

    return '', 200

if __name__ == '__main__':
    app.run(host='172.31.21.228', port=5000)

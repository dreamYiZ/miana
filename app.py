from flask import Flask, render_template, request, jsonify
import os
from ollama_call import scan_image  # 导入 ollama_call 文件中的函数

app = Flask(__name__)

# 使用 os.path.join 来拼接路径
images_folder = os.path.join(os.getcwd(), 'images')

@app.route('/')
def hello_world():
    return render_template('html/home.html')

@app.route('/scan', methods=['POST'])
def scan_images():
    scanned_images = []  # 用于存储扫描结果

    for filename in os.listdir(images_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(images_folder, filename)
            result = scan_image(image_path)  # 使用 ollama 扫描图片
            scanned_images.append(result)

    return jsonify({'message': 'Scan completed', 'scanned_images': scanned_images})

if __name__ == '__main__':
    app.run(debug=True)

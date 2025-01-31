from flask import Flask, render_template, request, jsonify
import os
from ollama_call import scan_image, ocr_image  # 导入 ollama_call 文件中的函数
from runtime_util import write_to_runtime_log_file

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
        write_to_runtime_log_file(filename)
        # 将文件名后缀转换为小写，然后进行检查
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".png"):
            image_path = os.path.join(images_folder, filename)
            result = ocr_image(image_path)  # 使用 ollama 扫描图片
            # result = scan_image(image_path)  # 使用 ollama 扫描图片
            scanned_images.append(result)
            write_to_runtime_log_file(result)


    return jsonify({'message': 'Scan completed', 'scanned_images': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)

# ollama_call.py
import ollama  # 假设 ollama 库已经导入
import pytesseract
from PIL import Image

# 识别图片中的文字，采用 pytesseract
def ocr_image(image_path):
    try:
        # 打开图片文件
        img = Image.open(image_path)
        # 使用 pytesseract 识别图片中的文字
        text = pytesseract.image_to_string(img, lang='chi_sim')  # 使用中文识别
        return text
    except Exception as e:
        return {'error': str(e)}

def scan_image(image_path):
    # 使用 ollama 模型识别图片中的文字并生成描述
    try:
        res = ollama.chat(
            model="llava:7b",
            messages=[
                {
                    'role': 'user',
                    'content': '识别其中的文字，返回中文文字:',
                    'images': [image_path]  # 使用传入的 image_path
                }
            ]
        )
    except Exception as e:
        res = {'error': str(e)}

    return res

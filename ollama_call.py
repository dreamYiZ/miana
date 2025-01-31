# ollama_call.py
import ollama  # 假设 ollama 库已经导入

def scan_image(image_path):
    # 使用 ollama 模型识别图片中的文字并生成描述
    try:
        res = ollama.chat(
            model="llava",
            messages=[
                {
                    'role': 'user',
                    'content': 'Describe this image:',
                    'images': [image_path]  # 使用传入的 image_path
                }
            ]
        )
    except Exception as e:
        res = {'error': str(e)}

    return res

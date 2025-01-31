import os
import datetime

def write_to_runtime_log_file(data):
    # 创建 runtime 文件夹如果不存在
    os.makedirs('runtime', exist_ok=True)
    # 设置日志文件路径
    log_file_path = os.path.join('runtime', 'runtime.log')

    # 获取当前时间，并格式化为字符串
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 将数据转换为字符串
    data_str = str(data)

    # 写入日志文件
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{current_time}\n{data_str}\n\n')



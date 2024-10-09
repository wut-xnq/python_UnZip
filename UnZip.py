import os
import zipfile
import rarfile
import py7zr

# 定义文件夹路径
folder_path = 'C:/Users/HP/Desktop/综测'  # 修改为你的文件夹路径

# 获取文件夹中的所有文件名
file_list = os.listdir(folder_path)

# 创建一个列表，用来存储解压失败的文件
failed_files = []

# 逐个解压文件
for file_name in file_list:
    try:
        # 只处理 .zip, .rar, .7z 文件
        if file_name.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(folder_path, file_name), 'r') as zip_ref:
                # 创建同名文件夹
                extract_path = os.path.join(folder_path, os.path.splitext(file_name)[0])
                os.makedirs(extract_path, exist_ok=True)
                zip_ref.extractall(extract_path)

        elif file_name.endswith('.rar'):
            with rarfile.RarFile(os.path.join(folder_path, file_name), 'r') as rar_ref:
                extract_path = os.path.join(folder_path, os.path.splitext(file_name)[0])
                os.makedirs(extract_path, exist_ok=True)
                rar_ref.extractall(extract_path)

        elif file_name.endswith('.7z'):
            with py7zr.SevenZipFile(os.path.join(folder_path, file_name), 'r') as seven_z_ref:
                extract_path = os.path.join(folder_path, os.path.splitext(file_name)[0])
                os.makedirs(extract_path, exist_ok=True)
                seven_z_ref.extractall(extract_path)

    except Exception as e:
        # 如果解压失败，记录文件名并打印错误信息
        print(f"Failed to extract {file_name}: {e}")
        failed_files.append(file_name)

# 打印所有未解压成功的文件名
if failed_files:
    print("\n以下压缩包未能解压成功：")
    for failed_file in failed_files:
        print(failed_file)
else:
    print("所有压缩包已成功解压。")

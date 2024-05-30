import os

def copy_txt_files_to_root(source_folder, destination_folder):
    # 确保目标文件夹存在，如果不存在则创建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取源文件夹中的所有子文件夹
    for subfolder_name in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder_name)
        
        # 检查是否为文件夹
        if os.path.isdir(subfolder_path):
            # 获取子文件夹中的所有文件
            for filename in os.listdir(subfolder_path):
                # 检查是否为txt文件
                if filename.endswith('.txt'):
                    source_path = os.path.join(subfolder_path, filename)
                    destination_path = os.path.join(destination_folder, filename)
                    # 使用 cp 命令复制文件到目标文件夹
                    os.system(f'cp "{source_path}" "{destination_path}"')
                    print(f'COPY {filename} TO {destination_folder}')

# 设置源文件夹和目标文件夹的路径
source_folder = 'runs/detect'
destination_folder = 'runs/Team5264testv5'

# 执行复制动作
copy_txt_files_to_root(source_folder, destination_folder)


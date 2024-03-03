import os
import yaml


def convert_labels_to_single_class(directory):
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为.txt文件（YOLO标签文件）
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)

            # 读取文件内容
            with open(filepath, "r") as file:
                lines = file.readlines()

            # 替换每行的第一个字段为0
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                parts[0] = "0"
                new_lines.append(" ".join(parts) + "\n")

            # 将修改后的内容写回文件
            with open(filepath, "w") as file:
                file.writelines(new_lines)


def find_datasets_to_modify(root_directory):
    datasets_to_modify = []

    # 遍历主文件夹中的每个数据集文件夹
    for dataset in os.listdir(root_directory):
        dataset_path = os.path.join(root_directory, dataset)

        # 检查data.yaml文件是否存在
        yaml_path = os.path.join(dataset_path, "data.yaml")
        if os.path.exists(yaml_path):
            with open(yaml_path, "r") as file:
                data = yaml.safe_load(file)

                # 根据nc字段来判断是否需要修改标签
                if data.get("nc", 1) > 1:
                    # 对于train、valid、test，只要它们存在就检查它们的labels文件夹
                    for subdir in ["train", "valid", "test"]:
                        labels_path = os.path.join(dataset_path, subdir, "labels")
                        if os.path.exists(labels_path):
                            datasets_to_modify.append(labels_path)

    return datasets_to_modify


# 使用示例
root_directory = "datasets"  # 替换为您的主文件夹路径
to_modify = find_datasets_to_modify(root_directory)
print(to_modify)
for dir in to_modify:
    convert_labels_to_single_class(dir)


# 使用示例
# directory = "datasets/2/valid/labels"  # 替换为您的标签文件夹路径
# convert_labels_to_single_class(directory)

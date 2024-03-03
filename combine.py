import os
import shutil


def merge_datasets(dataset_folder, output_folder):
    # 确保输出目录存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 为合并后的数据集创建结构
    for subset in ["train", "valid", "test"]:
        os.makedirs(os.path.join(output_folder, subset, "images"), exist_ok=True)
        os.makedirs(os.path.join(output_folder, subset, "labels"), exist_ok=True)

    # 文件ID用于重命名
    file_id = 0

    # 遍历每个数据集
    for dataset in os.listdir(dataset_folder):
        dataset_path = os.path.join(dataset_folder, dataset)

        for subset in ["train", "valid", "test"]:
            subset_path = os.path.join(dataset_path, subset)

            # 检查子集目录是否存在
            if not os.path.exists(subset_path):
                continue

            # 获取图片和标签列表
            images_list = [
                f
                for f in os.listdir(os.path.join(subset_path, "images"))
                if f.endswith((".jpg", ".jpeg", ".png"))
            ]
            labels_set = set(
                f
                for f in os.listdir(os.path.join(subset_path, "labels"))
                if f.endswith(".txt")
            )

            # 验证每张图片是否有一个对应的标签
            for image_file in images_list:
                basename = os.path.splitext(image_file)[0]

                # 使用set来检查相应的txt文件是否存在
                if f"{basename}.txt" not in labels_set:
                    print(
                        f"Warning: Missing label for image {image_file} in {subset_path}/images"
                    )
                    continue

                # 为图片和标签构建新的路径和文件名
                new_image_path = os.path.join(
                    output_folder, subset, "images", f"{file_id}.jpg"
                )
                new_label_path = os.path.join(
                    output_folder, subset, "labels", f"{file_id}.txt"
                )

                # 复制图片和标签到新路径
                shutil.copy(
                    os.path.join(subset_path, "images", image_file), new_image_path
                )
                shutil.copy(
                    os.path.join(subset_path, "labels", f"{basename}.txt"),
                    new_label_path,
                )

                # 自增文件ID
                file_id += 1

    print(f"{file_id} files have done.")


# 使用示例
dataset_folder = "datasets"
output_folder = "all"
merge_datasets(dataset_folder, output_folder)

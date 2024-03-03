from ultralytics import YOLO

# 加载模型
# model = YOLO('yolov8n.pt')  # 加载预训练模型（建议用于训练）
model = YOLO("/home/huayin/bubble-det/runs/detect/train2/weights/last.pt")

formats = ["onnx", "torchscript", "tflite", "tfjs"]
for format in formats:
    try:
        success = model.export(format=format)
        print(f"success: {success}")
    except Exception as e:
        print(f"error: {e}")
exit(0)

# 使用模型
# model.train(data="coco128.yaml", epochs=1)  # 训练模型

epoch = 800 - 33
model.train(
    data="./datasets/all/data.yaml",
    epochs=epoch,
    workers=5,
    device=[1],
    imgsz=1280,
    close_mosaic=epoch,
    batch=1,
)  # 训练模型
metrics = model.val()  # 在验证集上评估模型性能

success = model.export()  # 将模型导出为 ONNX 格式
print(f"success: {success}")


# Validate the model
# metrics = model.val()  # no arguments needed, dataset and settings remembered
# print(f"metrics: {metrics}")
# metrics.box.map    # map50-95
# metrics.box.map50  # map50
# metrics.box.map75  # map75
# metrics.box.maps   # a list contains map50-95 of each category


# model.export(format='onnx')

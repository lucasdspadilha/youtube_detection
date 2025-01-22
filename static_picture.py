import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt')
img = cv2.imread('./dataset/images_to_train/train/image62.png')
if img is None:
    print('Erro ao carregar a imagem!')
results = model(img)
results.render()
print(f"results: {results}")
cv2.imshow('Resultado', img)
cv2.waitKey(0)
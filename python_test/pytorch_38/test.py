import torch
import torchvision
from PIL import Image
from model_class import *

image_path = "image/dog1.png"
image_path = "image/air1.png"
image_path = "image/horse2.png"

image = Image.open(image_path)
print(image)
image = image.convert('RGB')

transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)), torchvision.transforms.ToTensor()])

image = transform(image)
print(image.shape)

image = torch.reshape(image, (1, 3, 32, 32))

# model_c1 = torch.load("model/model_c1_cpu_2.pth", map_location=torch.device('cpu'))
model_c1 = torch.load("model/model_c1_gpu_30.pth", map_location=torch.device('cpu'))
print(model_c1)

model_c1.eval()
with torch.no_grad():
    output = model_c1(image)

print(output)

print(output.argmax(1))
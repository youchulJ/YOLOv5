# YOLOv5
using google colab 

from google.colab import drive
drive.mount('/content/drive')

!git clone https://github.com/ultralytics/yolov5

%cd yolov5
!pip install -r requirements.txt # install dependencies

%cat /content/dataset/data.yaml

!pip install -U PyYAML

%cd /content/yolov5

#!python train.py --img 640 --batch 30 --epochs 20 --data /content/dataset/data.yaml --cfg /content/yolov5/models/yolov5s.yaml --weights yolov5s.pt --name test1
#!python train.py --img 640 --batch 16 --epochs 3 --data /content/dataset/data.yaml --weights yolov5s.pt
!python train.py --img 416 --batch 16 --epochs 50 --data /content/dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name styrofoam_yolov5s_results

%load_ext tensorboard
%tensorboard --logdir /content/yolov5/runs/train/styrofoam_yolov5s_results/

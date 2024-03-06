## Copy and paste this code as is to use it in Google Colab.

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Clone YOLOv5 repository
!git clone https://github.com/ultralytics/yolov5 

%cd yolov5 
!pip install -r requirements.txt # Install dependencies

# Check contents of data.yaml
%cat /content/dataset/data.yaml

# Install PyYAML for YAML parsing (required for proper functioning)
!pip install -U PyYAML

# Navigate to YOLOv5 directory
%cd /content/yolov5

# Train YOLOv5
!python train.py --img 640 --batch 30 --epochs 20 --data /content/dataset/data.yaml --cfg /content/yolov5/models/yolov5s.yaml --weights yolov5s.pt --name test1

# You can customize parameters such as image size, batch size, epochs, YOLOv5 version, and name.
!python train.py --img 416 --batch 16 --epochs 50 --data /content/dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name styrofoam_yolov5s_results

# Visualize and analyze training progress using TensorBoard
%load_ext tensorboard
%tensorboard --logdir /content/yolov5/runs

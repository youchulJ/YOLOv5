##구글 코랩에서 이용하는 방식으로 그대로 옯겨서 붙여사용하면 된다.1 


# 구글 드라이브 불러오기
from google.colab import drive
drive.mount('/content/drive')

# yolov5 불러오기
 !git clone https://github.com/ultralytics/yolov5 

%cd yolov5 
!pip install -r requirements.txt # install dependencies 

#data.yaml내의 내용 점검
%cat /content/dataset/data.yaml

#pyyaml install 설정 (안하면 잘 안된다고 하여 넣음)
!pip install -U PyYAML

#yolov5의 위치로 이동하기 
%cd /content/yolov5

#yolov5 트레이닝 하기 
!python train.py --img 640 --batch 30 --epochs 20 --data /content/dataset/data.yaml --cfg /content/yolov5/models/yolov5s.yaml --weights yolov5s.pt --name test1

#or 각 내용은 img size, batch size, epoch 등등 그리고 yolov5 버전도 바꿔주면됨 이름설정 마찬가지
!python train.py  --img 416 --batch 16 --epochs 50 --data /content/dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name styrofoam_yolov5s_results

# tesorboard를 통하여 그래프 확인하고 분석하기! 
%load_ext tensorboard
%tensorboard --logdir /content/yolov5/runs
sudo apt-get install -y libatlas-base-dev python-tk libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev ibxvidcore-dev libx264-dev qt4-dev-tools libatlas-base-dev
pip3 install tensorflow pillow lxml jupyter matplotlib cython opencv-python numpy==1.20.0
sudo apt-get install -y protobuf-compiler
protoc --version

mkdir ~/tensorflow1
cd ~/tensorflow1

git clone --depth 1 https://github.com/tensorflow/models.git

#touch .bashrc

#export PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow1/models/research:/home/pi/tensorflow1/models/research/slim >> ~/.bashrc

cd /home/pi/tensorflow1/models/research
protoc object_detection/protos/*.proto --python_out=.
cd /home/pi/tensorflow1/models/research/object_detection

wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz

wget https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/master/Object_detection_picamera.py

---
layout: publication
title: 'Yolov7: Trainable Bag-of-freebies Sets New State-of-the-art For Real-time
  Object Detectors'
authors: Chien-yao Wang, Alexey Bochkovskiy, Hong-yuan Mark Liao
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: wang2022yolov7
citations: 7005
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.02696'}]
tags: ["CVPR", "Efficiency"]
short_authors: Chien-yao Wang, Alexey Bochkovskiy, Hong-yuan Mark Liao
---
YOLOv7 surpasses all known object detectors in both speed and accuracy in the
range from 5 FPS to 160 FPS and has the highest accuracy 56.8% AP among all
known real-time object detectors with 30 FPS or higher on GPU V100. YOLOv7-E6
object detector (56 FPS V100, 55.9% AP) outperforms both transformer-based
detector SWIN-L Cascade-Mask R-CNN (9.2 FPS A100, 53.9% AP) by 509% in speed
and 2% in accuracy, and convolutional-based detector ConvNeXt-XL Cascade-Mask
R-CNN (8.6 FPS A100, 55.2% AP) by 551% in speed and 0.7% AP in accuracy, as
well as YOLOv7 outperforms: YOLOR, YOLOX, Scaled-YOLOv4, YOLOv5, DETR,
Deformable DETR, DINO-5scale-R50, ViT-Adapter-B and many other object detectors
in speed and accuracy. Moreover, we train YOLOv7 only on MS COCO dataset from
scratch without using any other datasets or pre-trained weights. Source code is
released in https://github.com/WongKinYiu/yolov7.
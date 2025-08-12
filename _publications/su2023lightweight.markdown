---
layout: publication
title: Lightweight Pixel Difference Networks For Efficient Visual Representation Learning
authors: "Zhuo Su, Jiehua Zhang, Longguang Wang, Hua Zhang, Zhen Liu, Matti Pietik\xE4\
  inen, Li Liu"
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: su2023lightweight
citations: 22
additional_links: [{name: Code, url: 'https://github.com/hellozhuo/pidinet\}\{https://github.com/hellozhuo/pidinet\'},
  {name: Paper, url: 'https://arxiv.org/abs/2402.00422'}]
tags: ["Efficiency"]
short_authors: Su et al.
---
Recently, there have been tremendous efforts in developing lightweight Deep
Neural Networks (DNNs) with satisfactory accuracy, which can enable the
ubiquitous deployment of DNNs in edge devices. The core challenge of developing
compact and efficient DNNs lies in how to balance the competing goals of
achieving high accuracy and high efficiency. In this paper we propose two novel
types of convolutions, dubbed *Pixel Difference Convolution (PDC) and
Binary PDC (Bi-PDC)* which enjoy the following benefits: capturing higher-order
local differential information, computationally efficient, and able to be
integrated with existing DNNs. With PDC and Bi-PDC, we further present two
lightweight deep networks named *Pixel Difference Networks (PiDiNet)* and
*Binary PiDiNet (Bi-PiDiNet)* respectively to learn highly efficient yet
more accurate representations for visual tasks including edge detection and
object recognition. Extensive experiments on popular datasets (BSDS500,
ImageNet, LFW, YTF, *etc.*) show that PiDiNet and Bi-PiDiNet achieve the
best accuracy-efficiency trade-off. For edge detection, PiDiNet is the first
network that can be trained without ImageNet, and can achieve the human-level
performance on BSDS500 at 100 FPS and with \(<\)1M parameters. For object
recognition, among existing Binary DNNs, Bi-PiDiNet achieves the best accuracy
and a nearly \(2\times\) reduction of computational cost on ResNet18. Code
available at
\href\{https://github.com/hellozhuo/pidinet\}\{https://github.com/hellozhuo/pidinet\}.
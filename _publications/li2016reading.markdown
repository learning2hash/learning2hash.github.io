---
layout: publication
title: Reading Car License Plates Using Deep Convolutional Neural Networks And Lstms
authors: Hui Li, Chunhua Shen
conference: Arxiv
year: 2016
bibkey: li2016reading
citations: 170
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.05610'}]
tags: []
short_authors: Hui Li, Chunhua Shen
---
In this work, we tackle the problem of car license plate detection and
recognition in natural scene images. Inspired by the success of deep neural
networks (DNNs) in various vision applications, here we leverage DNNs to learn
high-level features in a cascade framework, which lead to improved performance
on both detection and recognition.
  Firstly, we train a \(37\)-class convolutional neural network (CNN) to detect
all characters in an image, which results in a high recall, compared with
conventional approaches such as training a binary text/non-text classifier.
False positives are then eliminated by the second plate/non-plate CNN
classifier. Bounding box refinement is then carried out based on the edge
information of the license plates, in order to improve the
intersection-over-union (IoU) ratio. The proposed cascade framework extracts
license plates effectively with both high recall and precision. Last, we
propose to recognize the license characters as a \{sequence labelling\} problem.
A recurrent neural network (RNN) with long short-term memory (LSTM) is trained
to recognize the sequential features extracted from the whole license plate via
CNNs. The main advantage of this approach is that it is segmentation free. By
exploring context information and avoiding errors caused by segmentation, the
RNN method performs better than a baseline method of combining segmentation and
deep CNN classification; and achieves state-of-the-art recognition accuracy.
---
layout: publication
title: 'Fkimnet: A Finger Dorsal Image Matching Network Comparing Component (major,
  Minor And Nail) Matching With Holistic (finger Dorsal) Matching'
authors: Daksh Thapar, Gaurav Jaswal, Aditya Nigam
conference: 2019 International Joint Conference on Neural Networks (IJCNN)
year: 2019
bibkey: thapar2019fkimnet
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.01289'}]
tags: [Evaluation, Distance Metric Learning, Datasets]
short_authors: Daksh Thapar, Gaurav Jaswal, Aditya Nigam
---
Current finger knuckle image recognition systems, often require users to
place fingers' major or minor joints flatly towards the capturing sensor. To
extend these systems for user non-intrusive application scenarios, such as
consumer electronics, forensic, defence etc, we suggest matching the full
dorsal fingers, rather than the major/ minor region of interest (ROI) alone. In
particular, this paper makes a comprehensive study on the comparisons between
full finger and fusion of finger ROI's for finger knuckle image recognition.
These experiments suggest that using full-finger, provides a more elegant
solution. Addressing the finger matching problem, we propose a CNN
(convolutional neural network) which creates a \(128\)-D feature embedding of an
image. It is trained via. triplet loss function, which enforces the L2 distance
between the embeddings of the same subject to be approaching zero, whereas the
distance between any 2 embeddings of different subjects to be at least a
margin. For precise training of the network, we use dynamic adaptive margin,
data augmentation, and hard negative mining. In distinguished experiments, the
individual performance of finger, as well as weighted sum score level fusion of
major knuckle, minor knuckle, and nail modalities have been computed,
justifying our assumption to consider full finger as biometrics instead of its
counterparts. The proposed method is evaluated using two publicly available
finger knuckle image datasets i.e., PolyU FKP dataset and PolyU Contactless FKI
Datasets.
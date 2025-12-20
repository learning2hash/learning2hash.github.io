---
layout: publication
title: Deep Metric Learning-based Image Retrieval System For Chest Radiograph And
  Its Clinical Applications In COVID-19
authors: Aoxiao Zhong, Xiang Li, Dufan Wu, Hui Ren, Kyungsang Kim, Younggon Kim, Varun
  Buch, Nir Neumark, Bernardo Bizzo, Won Young Tak, Soo Young Park, Yu Rim Lee, Min
  Kyu Kang, Jung Gil Park, Byung Seok Kim, Woo Jin Chung, Ning Guo, Ittai Dayan, Mannudeep
  K. Kalra, Quanzheng Li
conference: Medical Image Analysis
year: 2020
bibkey: zhong2020deep
citations: 76
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.03663'}]
tags: ["Datasets", "Distance Metric Learning", "Image Retrieval", "Neural Hashing"]
short_authors: Zhong et al.
---
In recent years, deep learning-based image analysis methods have been widely
applied in computer-aided detection, diagnosis and prognosis, and has shown its
value during the public health crisis of the novel coronavirus disease 2019
(COVID-19) pandemic. Chest radiograph (CXR) has been playing a crucial role in
COVID-19 patient triaging, diagnosing and monitoring, particularly in the
United States. Considering the mixed and unspecific signals in CXR, an image
retrieval model of CXR that provides both similar images and associated
clinical information can be more clinically meaningful than a direct image
diagnostic model. In this work we develop a novel CXR image retrieval model
based on deep metric learning. Unlike traditional diagnostic models which aims
at learning the direct mapping from images to labels, the proposed model aims
at learning the optimized embedding space of images, where images with the same
labels and similar contents are pulled together. It utilizes multi-similarity
loss with hard-mining sampling strategy and attention mechanism to learn the
optimized embedding space, and provides similar images to the query image. The
model is trained and validated on an international multi-site COVID-19 dataset
collected from 3 different sources. Experimental results of COVID-19 image
retrieval and diagnosis tasks show that the proposed model can serve as a
robust solution for CXR analysis and patient management for COVID-19. The model
is also tested on its transferability on a different clinical decision support
task, where the pre-trained model is applied to extract image features from a
new dataset without any further training. These results demonstrate our deep
metric learning based image retrieval model is highly efficient in the CXR
retrieval, diagnosis and prognosis, and thus has great clinical value for the
treatment and management of COVID-19 patients.
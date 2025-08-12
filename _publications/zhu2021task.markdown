---
layout: publication
title: Task-aware Meta Learning-based Siamese Neural Network For Classifying Obfuscated
  Malware
authors: Jinting Zhu, Julian Jang-Jaccard, Amardeep Singh, Paul A. Watters, Seyit
  Camtepe
conference: Future Internet 2023 15(6) 214
year: 2021
bibkey: zhu2021task
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.13409'}]
tags: []
short_authors: Zhu et al.
---
Malware authors apply different techniques of control flow obfuscation, in
order to create new malware variants to avoid detection. Existing Siamese
neural network (SNN)-based malware detection methods fail to correctly classify
different malware families when such obfuscated malware samples are present in
the training dataset, resulting in high false-positive rates. To address this
issue, we propose a novel task-aware few-shot-learning-based Siamese Neural
Network that is resilient against the presence of malware variants affected by
such control flow obfuscation techniques. Using the average entropy features of
each malware family as inputs, in addition to the image features, our model
generates the parameters for the feature layers, to more accurately adjust the
feature embedding for different malware families, each of which has obfuscated
malware variants. In addition, our proposed method can classify malware
classes, even if there are only one or a few training samples available. Our
model utilizes few-shot learning with the extracted features of a pre-trained
network (e.g., VGG-16), to avoid the bias typically associated with a model
trained with a limited number of training samples. Our proposed approach is
highly effective in recognizing unique malware signatures, thus correctly
classifying malware samples that belong to the same malware family, even in the
presence of obfuscated malware variants. Our experimental results, validated by
N-way on N-shot learning, show that our model is highly effective in
classification accuracy, exceeding a rate \textgreater 91%, compared to other
similar methods.
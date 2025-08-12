---
layout: publication
title: A Few-shot Meta-learning Based Siamese Neural Network Using Entropy Features
  For Ransomware Classification
authors: Jinting Zhu, Julian Jang-jaccard, Amardeep Singh, Ian Welch, Harith Ai-sahaf,
  Seyit Camtepe
conference: Computers &amp; Security
year: 2022
bibkey: zhu2021few
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.00668'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhu et al.
---
Ransomware defense solutions that can quickly detect and classify different
ransomware classes to formulate rapid response plans have been in high demand
in recent years. Though the applicability of adopting deep learning techniques
to provide automation and self-learning provision has been proven in many
application domains, the lack of data available for ransomware (and other
malware)samples has been raised as a barrier to developing effective deep
learning-based solutions. To address this concern, we propose a few-shot
meta-learning based Siamese Neural Network that not only detects ransomware
attacks but is able to classify them into different classes. Our proposed model
utilizes the entropy feature directly extracted from ransomware binary files to
retain more fine-grained features associated with different ransomware
signatures. These entropy features are used further to train and optimize our
model using a pre-trained network (e.g. VGG-16) in a meta-learning fashion.
This approach generates more accurate weight factors, compared to feature
images are used, to avoid the bias typically associated with a model trained
with a limited number of training samples. Our experimental results show that
our proposed model is highly effective in providing a weighted F1-score
exceeding the rate>86% compared
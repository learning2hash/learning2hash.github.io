---
layout: publication
title: Relation-aware Based Siamese Denoising Autoencoder For Malware Few-shot Classification
authors: Jinting Zhu, Julian Jang-Jaccard, Ian Welch, Harith Ai-Sahaf, Seyit Camtepe,
  Aeryn Dunmore, Cybersecurity Lab
conference: Arxiv
year: 2023
bibkey: zhu2023relation
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.14029'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhu et al.
---
When malware employs an unseen zero-day exploit, traditional security
measures such as vulnerability scanners and antivirus software can fail to
detect them. This is because these tools rely on known patches and signatures,
which do not exist for new zero-day attacks. Furthermore, existing machine
learning methods, which are trained on specific and occasionally outdated
malware samples, may struggle to adapt to features in new malware. To address
this issue, there is a need for a more robust machine learning model that can
identify relationships between malware samples without being trained on a
particular malware feature set. This is particularly crucial in the field of
cybersecurity, where the number of malware samples is limited and obfuscation
techniques are widely used. Current approaches using stacked autoencoders aim
to remove the noise introduced by obfuscation techniques through reconstruction
of the input. However, this approach ignores the semantic relationships between
features across different malware samples. To overcome this limitation, we
propose a novel Siamese Neural Network (SNN) that uses relation-aware
embeddings to calculate more accurate similarity probabilities based on
semantic details of different malware samples. In addition, by using entropy
images as inputs, our model can extract better structural information and
subtle differences in malware signatures, even in the presence of obfuscation
techniques. Evaluations on two large malware sample sets using the N-shot and
N-way methods show that our proposed model is highly effective in predicting
previously unseen malware, even in the presence of obfuscation techniques.
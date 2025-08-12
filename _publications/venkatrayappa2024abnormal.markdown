---
layout: publication
title: Abnormal Event Detection In Videos Using Deep Embedding
authors: Darshan Venkatrayappa
conference: Arxiv
year: 2024
bibkey: venkatrayappa2024abnormal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.09804'}]
tags: ["Unsupervised"]
short_authors: Darshan Venkatrayappa
---
Abnormal event detection or anomaly detection in surveillance videos is
currently a challenge because of the diversity of possible events. Due to the
lack of anomalous events at training time, anomaly detection requires the
design of learning methods without supervision. In this work we propose an
unsupervised approach for video anomaly detection with the aim to jointly
optimize the objectives of the deep neural network and the anomaly detection
task using a hybrid architecture. Initially, a convolutional autoencoder is
pre-trained in an unsupervised manner with a fusion of depth, motion and
appearance features. In the second step, we utilize the encoder part of the
pre-trained autoencoder and extract the embeddings of the fused input. Now, we
jointly train/ fine tune the encoder to map the embeddings to a hypercenter.
Thus, embeddings of normal data fall near the hypercenter, whereas embeddings
of anomalous data fall far away from the hypercenter.
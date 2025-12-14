---
layout: publication
title: 'Real-time Wireless Transmitter Authorization: Adapting To Dynamic Authorized
  Sets With Information Retrieval'
authors: Samurdhi Karunaratne, Samer Hanna, Danijela Cabric
conference: 2021 IEEE International Symposium on Dynamic Spectrum Access Networks
  (DySPAN)
year: 2021
bibkey: karunaratne2021real
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.02584'}]
tags: [Hashing Methods, Locality Sensitive Hashing, Neural Hashing, Efficiency]
short_authors: Samurdhi Karunaratne, Samer Hanna, Danijela Cabric
---
As the Internet of Things (IoT) continues to grow, ensuring the security of
systems that rely on wireless IoT devices has become critically important. Deep
learning-based passive physical layer transmitter authorization systems have
been introduced recently for this purpose, as they accommodate the limited
computational and power budget of such devices. These systems have been shown
to offer excellent outlier detection accuracies when trained and tested on a
fixed authorized transmitter set. However in a real-life deployment, a need may
arise for transmitters to be added and removed as the authorized set of
transmitters changes. In such cases, the system could experience long
down-times, as retraining the underlying deep learning model is often a
time-consuming process. In this paper, we draw inspiration from information
retrieval to address this problem: by utilizing feature vectors as RF
fingerprints, we first demonstrate that training could be simplified to
indexing those feature vectors into a database using locality sensitive hashing
(LSH). Then we show that approximate nearest neighbor search could be performed
on the database to perform transmitter authorization that matches the accuracy
of deep learning models, while allowing for more than 100x faster retraining.
Furthermore, dimensionality reduction techniques are used on the feature
vectors to show that the authorization latency of our technique could be
reduced to approach that of traditional deep learning-based systems.
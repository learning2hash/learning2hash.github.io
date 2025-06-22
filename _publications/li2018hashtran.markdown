---
layout: publication
title: Hashtran-dnn A Framework For Enhancing Robustness Of Deep Neural Networks Against
  Adversarial Malware Samples
authors: Li Deqiang et al.
conference: Arxiv
year: 2018
citations: 18
bibkey: li2018hashtran
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.06498'}]
tags: [Hashing Methods, Supervised, Has Code]
---
Adversarial machine learning in the context of image processing and related
applications has received a large amount of attention. However, adversarial
machine learning, especially adversarial deep learning, in the context of
malware detection has received much less attention despite its apparent
importance. In this paper, we present a framework for enhancing the robustness
of Deep Neural Networks (DNNs) against adversarial malware samples, dubbed
Hashing Transformation Deep Neural Networks\} (HashTran-DNN). The core idea is
to use hash functions with a certain locality-preserving property to transform
samples to enhance the robustness of DNNs in malware classification. The
framework further uses a Denoising Auto-Encoder (DAE) regularizer to
reconstruct the hash representations of samples, making the resulting DNN
classifiers capable of attaining the locality information in the latent space.
We experiment with two concrete instantiations of the HashTran-DNN framework to
classify Android malware. Experimental results show that four known attacks can
render standard DNNs useless in classifying Android malware, that known
defenses can at most defend three of the four attacks, and that HashTran-DNN
can effectively defend against all of the four attacks.
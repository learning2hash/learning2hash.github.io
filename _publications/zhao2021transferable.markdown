---
layout: publication
title: A Transferable Anti-forensic Attack On Forensic Cnns Using A Generative Adversarial
  Network
authors: Xinwei Zhao, Chen Chen, Matthew C. Stamm
conference: Arxiv
year: 2021
bibkey: zhao2021transferable
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.09568'}]
tags: ["Robustness"]
short_authors: Xinwei Zhao, Chen Chen, Matthew C. Stamm
---
With the development of deep learning, convolutional neural networks (CNNs)
have become widely used in multimedia forensics for tasks such as detecting and
identifying image forgeries. Meanwhile, anti-forensic attacks have been
developed to fool these CNN-based forensic algorithms. Previous anti-forensic
attacks often were designed to remove forgery traces left by a single
manipulation operation as opposed to a set of manipulations. Additionally,
recent research has shown that existing anti-forensic attacks against forensic
CNNs have poor transferability, i.e. they are unable to fool other forensic
CNNs that were not explicitly used during training. In this paper, we propose a
new anti-forensic attack framework designed to remove forensic traces left by a
variety of manipulation operations. This attack is transferable, i.e. it can be
used to attack forensic CNNs are unknown to the attacker, and it introduces
only minimal distortions that are imperceptible to human eyes. Our proposed
attack utilizes a generative adversarial network (GAN) to build a generator
that can attack color images of any size. We achieve attack transferability
through the use of a new training strategy and loss function. We conduct
extensive experiment to demonstrate that our attack can fool many state-of-art
forensic CNNs with varying levels of knowledge available to the attacker.
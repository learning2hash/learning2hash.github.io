---
layout: publication
title: A Baseline For Few-shot Image Classification
authors: Guneet S. Dhillon, Pratik Chaudhari, Avinash Ravichandran, Stefano Soatto
conference: International Conference on Learning Representations (ICLR) 2020
year: 2019
bibkey: dhillon2019baseline
citations: 313
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.02729'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Dhillon et al.
---
Fine-tuning a deep network trained with the standard cross-entropy loss is a
strong baseline for few-shot learning. When fine-tuned transductively, this
outperforms the current state-of-the-art on standard datasets such as
Mini-ImageNet, Tiered-ImageNet, CIFAR-FS and FC-100 with the same
hyper-parameters. The simplicity of this approach enables us to demonstrate the
first few-shot learning results on the ImageNet-21k dataset. We find that using
a large number of meta-training classes results in high few-shot accuracies
even for a large number of few-shot classes. We do not advocate our approach as
the solution for few-shot learning, but simply use the results to highlight
limitations of current benchmarks and few-shot protocols. We perform extensive
studies on benchmark datasets to propose a metric that quantifies the
"hardness" of a few-shot episode. This metric can be used to report the
performance of few-shot algorithms in a more systematic way.
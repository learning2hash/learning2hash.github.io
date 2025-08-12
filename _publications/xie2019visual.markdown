---
layout: publication
title: 'Visual Entailment: A Novel Task For Fine-grained Image Understanding'
authors: Ning Xie, Farley Lai, Derek Doran, Asim Kadav
conference: Arxiv
year: 2019
bibkey: xie2019visual
citations: 164
additional_links: [{name: Code, url: 'https://github.com/'}, {name: Paper, url: 'https://arxiv.org/abs/1901.06706'}]
tags: ["Datasets"]
short_authors: Xie et al.
---
Existing visual reasoning datasets such as Visual Question Answering (VQA),
often suffer from biases conditioned on the question, image or answer
distributions. The recently proposed CLEVR dataset addresses these limitations
and requires fine-grained reasoning but the dataset is synthetic and consists
of similar objects and sentence structures across the dataset.
  In this paper, we introduce a new inference task, Visual Entailment (VE) -
consisting of image-sentence pairs whereby a premise is defined by an image,
rather than a natural language sentence as in traditional Textual Entailment
tasks. The goal of a trained VE model is to predict whether the image
semantically entails the text. To realize this task, we build a dataset SNLI-VE
based on the Stanford Natural Language Inference corpus and Flickr30k dataset.
We evaluate various existing VQA baselines and build a model called Explainable
Visual Entailment (EVE) system to address the VE task. EVE achieves up to 71%
accuracy and outperforms several other state-of-the-art VQA based models.
Finally, we demonstrate the explainability of EVE through cross-modal attention
visualizations. The SNLI-VE dataset is publicly available at
https://github.com/ necla-ml/SNLI-VE.
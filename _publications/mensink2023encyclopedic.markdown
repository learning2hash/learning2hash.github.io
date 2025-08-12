---
layout: publication
title: 'Encyclopedic VQA: Visual Questions About Detailed Properties Of Fine-grained
  Categories'
authors: "Thomas Mensink, Jasper Uijlings, Lluis Castrejon, Arushi Goel, Felipe Cadar,\
  \ Howard Zhou, Fei Sha, Andr\xE9 Araujo, Vittorio Ferrari"
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: mensink2023encyclopedic
citations: 7
additional_links: [{name: Code, url: 'https://github.com/google-research/google-research/tree/master/encyclopedic_vqa'},
  {name: Paper, url: 'https://arxiv.org/abs/2306.09224'}]
tags: ["ICCV"]
short_authors: Mensink et al.
---
We propose Encyclopedic-VQA, a large scale visual question answering (VQA)
dataset featuring visual questions about detailed properties of fine-grained
categories and instances. It contains 221k unique question+answer pairs each
matched with (up to) 5 images, resulting in a total of 1M VQA samples.
Moreover, our dataset comes with a controlled knowledge base derived from
Wikipedia, marking the evidence to support each answer. Empirically, we show
that our dataset poses a hard challenge for large vision+language models as
they perform poorly on our dataset: PaLI [14] is state-of-the-art on OK-VQA
[37], yet it only achieves 13.0% accuracy on our dataset. Moreover, we
experimentally show that progress on answering our encyclopedic questions can
be achieved by augmenting large models with a mechanism that retrieves relevant
information from the knowledge base. An oracle experiment with perfect
retrieval achieves 87.0% accuracy on the single-hop portion of our dataset, and
an automatic retrieval-augmented prototype yields 48.8%. We believe that our
dataset enables future research on retrieval-augmented vision+language models.
It is available at
https://github.com/google-research/google-research/tree/master/encyclopedic_vqa .
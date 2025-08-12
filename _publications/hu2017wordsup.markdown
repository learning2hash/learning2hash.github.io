---
layout: publication
title: 'Wordsup: Exploiting Word Annotations For Character Based Text Detection'
authors: Han Hu, Chengquan Zhang, Yuxuan Luo, Yuzhuo Wang, Junyu Han, Errui Ding
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: hu2017wordsup
citations: 205
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.06720'}]
tags: ["ICCV"]
short_authors: Hu et al.
---
Imagery texts are usually organized as a hierarchy of several visual
elements, i.e. characters, words, text lines and text blocks. Among these
elements, character is the most basic one for various languages such as
Western, Chinese, Japanese, mathematical expression and etc. It is natural and
convenient to construct a common text detection engine based on character
detectors. However, training character detectors requires a vast of location
annotated characters, which are expensive to obtain. Actually, the existing
real text datasets are mostly annotated in word or line level. To remedy this
dilemma, we propose a weakly supervised framework that can utilize word
annotations, either in tight quadrangles or the more loose bounding boxes, for
character detector training. When applied in scene text detection, we are thus
able to train a robust character detector by exploiting word annotations in the
rich large-scale real scene text datasets, e.g. ICDAR15 and COCO-text. The
character detector acts as a key role in the pipeline of our text detection
engine. It achieves the state-of-the-art performance on several challenging
scene text detection benchmarks. We also demonstrate the flexibility of our
pipeline by various scenarios, including deformed text detection and math
expression recognition.
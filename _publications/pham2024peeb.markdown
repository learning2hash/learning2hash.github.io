---
layout: publication
title: 'PEEB: Part-based Image Classifiers With An Explainable And Editable Language
  Bottleneck'
authors: Thang M. Pham, Peijie Chen, Tin Nguyen, Seunghyun Yoon, Trung Bui, Anh Totti
  Nguyen
conference: 'Findings of the Association for Computational Linguistics: NAACL 2024'
year: 2024
bibkey: pham2024peeb
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.05297'}]
tags: ["NAACL"]
short_authors: Pham et al.
---
CLIP-based classifiers rely on the prompt containing a \{class name\} that is
known to the text encoder. Therefore, they perform poorly on new classes or the
classes whose names rarely appear on the Internet (e.g., scientific names of
birds). For fine-grained classification, we propose PEEB - an explainable and
editable classifier to (1) express the class name into a set of text
descriptors that describe the visual parts of that class; and (2) match the
embeddings of the detected parts to their textual descriptors in each class to
compute a logit score for classification. In a zero-shot setting where the
class names are unknown, PEEB outperforms CLIP by a huge margin (~10x in top-1
accuracy). Compared to part-based classifiers, PEEB is not only the
state-of-the-art (SOTA) on the supervised-learning setting (88.80% and 92.20%
accuracy on CUB-200 and Dogs-120, respectively) but also the first to enable
users to edit the text descriptors to form a new classifier without any
re-training. Compared to concept bottleneck models, PEEB is also the SOTA in
both zero-shot and supervised-learning settings.
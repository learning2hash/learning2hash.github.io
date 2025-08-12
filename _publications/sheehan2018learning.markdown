---
layout: publication
title: Learning To Interpret Satellite Images Using Wikipedia
authors: Evan Sheehan, Burak Uzkent, Chenlin Meng, Zhongyi Tang, Marshall Burke, David
  Lobell, Stefano Ermon
conference: Proceedings of the Twenty-Eighth International Joint Conference on Artificial
  Intelligence
year: 2019
bibkey: sheehan2018learning
citations: 29
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.10236'}]
tags: ["IJCAI"]
short_authors: Sheehan et al.
---
Despite recent progress in computer vision, fine-grained interpretation of
satellite images remains challenging because of a lack of labeled training
data. To overcome this limitation, we propose using Wikipedia as a previously
untapped source of rich, georeferenced textual information with global
coverage. We construct a novel large-scale, multi-modal dataset by pairing
geo-referenced Wikipedia articles with satellite imagery of their corresponding
locations. To prove the efficacy of this dataset, we focus on the African
continent and train a deep network to classify images based on labels extracted
from articles. We then fine-tune the model on a human annotated dataset and
demonstrate that this weak form of supervision can drastically reduce the
quantity of human annotated labels and time required for downstream tasks.
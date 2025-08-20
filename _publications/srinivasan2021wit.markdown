---
layout: publication
title: 'WIT: Wikipedia-based Image Text Dataset For Multimodal Multilingual Machine
  Learning'
authors: Krishna Srinivasan, Karthik Raman, Jiecao Chen, Michael Bendersky, Marc Najork
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: srinivasan2021wit
citations: 130
additional_links: [{name: Code, url: 'https://github.com/google-research-datasets/wit'},
  {name: Paper, url: 'https://arxiv.org/abs/2103.01913'}]
tags: [Text Retrieval, SIGIR, Datasets, Evaluation]
short_authors: Srinivasan et al.
---
The milestone improvements brought about by deep representation learning and
pre-training techniques have led to large performance gains across downstream
NLP, IR and Vision tasks. Multimodal modeling techniques aim to leverage large
high-quality visio-linguistic datasets for learning complementary information
(across image and text modalities). In this paper, we introduce the
Wikipedia-based Image Text (WIT) Dataset
(https://github.com/google-research-datasets/wit) to better facilitate
multimodal, multilingual learning. WIT is composed of a curated set of 37.6
million entity rich image-text examples with 11.5 million unique images across
108 Wikipedia languages. Its size enables WIT to be used as a pretraining
dataset for multimodal models, as we show when applied to downstream tasks such
as image-text retrieval. WIT has four main and unique advantages. First, WIT is
the largest multimodal dataset by the number of image-text examples by 3x (at
the time of writing). Second, WIT is massively multilingual (first of its kind)
with coverage over 100+ languages (each of which has at least 12K examples) and
provides cross-lingual texts for many images. Third, WIT represents a more
diverse set of concepts and real world entities relative to what previous
datasets cover. Lastly, WIT provides a very challenging real-world test set, as
we empirically illustrate using an image-text retrieval task as an example.
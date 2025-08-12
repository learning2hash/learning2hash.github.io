---
layout: publication
title: 'Fungitastic: A Multi-modal Dataset And Benchmark For Image Categorization'
authors: Lukas Picek, Klara Janouskova, Vojtech Cermak, Jiri Matas
conference: Arxiv
year: 2024
bibkey: picek2024fungitastic
citations: 0
additional_links: [{name: Code, url: 'https://github.com/BohemianVRA/FungiTastic/'},
  {name: Paper, url: 'https://arxiv.org/abs/2408.13632'}]
tags: ["Datasets", "Evaluation", "Tools & Libraries"]
short_authors: Picek et al.
---
We introduce a new, challenging benchmark and a dataset, FungiTastic, based
on fungal records continuously collected over a twenty-year span. The dataset
is labelled and curated by experts and consists of about 350k multimodal
observations of 6k fine-grained categories (species). The fungi observations
include photographs and additional data, e.g., meteorological and climatic
data, satellite images, and body part segmentation masks. FungiTastic is one of
the few benchmarks that include a test set with DNA-sequenced ground truth of
unprecedented label reliability. The benchmark is designed to support (i)
standard closed-set classification, (ii) open-set classification, (iii)
multi-modal classification, (iv) few-shot learning, (v) domain shift, and many
more. We provide tailored baselines for many use cases, a multitude of
ready-to-use pre-trained models on
https://huggingface.co/collections/BVRA/fungitastic-66a227ce0520be533dc6403b,
and a framework for model training. The documentation and the baselines are
available at https://github.com/BohemianVRA/FungiTastic/ and
https://www.kaggle.com/datasets/picekl/fungitastic.
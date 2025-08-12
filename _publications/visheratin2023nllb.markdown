---
layout: publication
title: NLLB-CLIP -- Train Performant Multilingual Image Retrieval Model On A Budget
authors: Alexander Visheratin
conference: Arxiv
year: 2023
bibkey: visheratin2023nllb
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01859'}]
tags: ["Image Retrieval"]
short_authors: Alexander Visheratin
---
Today, the exponential rise of large models developed by academic and
industrial institutions with the help of massive computing resources raises the
question of whether someone without access to such resources can make a
valuable scientific contribution. To explore this, we tried to solve the
challenging task of multilingual image retrieval having a limited budget of
$1,000. As a result, we present NLLB-CLIP - CLIP model with a text encoder from
the NLLB model. To train the model, we used an automatically created dataset of
106,246 good-quality images with captions in 201 languages derived from the
LAION COCO dataset. We trained multiple models using image and text encoders of
various sizes and kept different parts of the model frozen during the training.
We thoroughly analyzed the trained models using existing evaluation datasets
and newly created XTD200 and Flickr30k-200 datasets. We show that NLLB-CLIP is
comparable in quality to state-of-the-art models and significantly outperforms
them on low-resource languages.
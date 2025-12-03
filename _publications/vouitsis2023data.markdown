---
layout: publication
title: Data-efficient Multimodal Fusion On A Single GPU
authors: "No\xEBl Vouitsis, Zhaoyan Liu, Satya Krishna Gorti, Valentin Villecroze,\
  \ Jesse C. Cresswell, Guangwei Yu, Gabriel Loaiza-Ganem, Maksims Volkovs"
conference: Arxiv
year: 2023
bibkey: vouitsis2023data
citations: 1
additional_links: [{name: Code, url: 'https://github.com/layer6ai-labs/fusemix'},
  {name: Paper, url: 'https://arxiv.org/abs/2312.10144'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Multimodal Retrieval", "Text Retrieval"]
short_authors: Vouitsis et al.
---
The goal of multimodal alignment is to learn a single latent space that is
shared between multimodal inputs. The most powerful models in this space have
been trained using massive datasets of paired inputs and large-scale
computational resources, making them prohibitively expensive to train in many
practical scenarios. We surmise that existing unimodal encoders pre-trained on
large amounts of unimodal data should provide an effective bootstrap to create
multimodal models from unimodal ones at much lower costs. We therefore propose
FuseMix, a multimodal augmentation scheme that operates on the latent spaces of
arbitrary pre-trained unimodal encoders. Using FuseMix for multimodal
alignment, we achieve competitive performance -- and in certain cases
outperform state-of-the art methods -- in both image-text and audio-text
retrieval, with orders of magnitude less compute and data: for example, we
outperform CLIP on the Flickr30K text-to-image retrieval task with \(\sim \!
600\times\) fewer GPU days and \(\sim \! 80\times\) fewer image-text pairs.
Additionally, we show how our method can be applied to convert pre-trained
text-to-image generative models into audio-to-image ones. Code is available at:
https://github.com/layer6ai-labs/fusemix.
---
layout: publication
title: Linking Representations With Multimodal Contrastive Learning
authors: Abhishek Arora, Xinmei Yang, Shao-Yu Jheng, Melissa Dell
conference: Arxiv
year: 2023
bibkey: arora2023linking
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.03464'}]
tags: [Neural Hashing, Self-Supervised, Datasets, Supervised]
short_authors: Arora et al.
---
Many applications require linking individuals, firms, or locations across
datasets. Most widely used methods, especially in social science, do not employ
deep learning, with record linkage commonly approached using string matching
techniques. Moreover, existing methods do not exploit the inherently multimodal
nature of documents. In historical record linkage applications, documents are
typically noisily transcribed by optical character recognition (OCR). Linkage
with just OCR'ed texts may fail due to noise, whereas linkage with just image
crops may also fail because vision models lack language understanding (e.g., of
abbreviations or other different ways of writing firm names). To leverage
multimodal learning, this study develops CLIPPINGS (Contrastively LInking
Pooled Pre-trained Embeddings). CLIPPINGS aligns symmetric vision and language
bi-encoders, through contrastive language-image pre-training on document images
and their corresponding OCR'ed texts. It then contrastively learns a metric
space where the pooled image-text embedding for a given instance is close to
embeddings in the same class (e.g., the same firm or location) and distant from
embeddings of a different class. Data are linked by treating linkage as a
nearest neighbor retrieval problem with the multimodal embeddings. CLIPPINGS
outperforms widely used string matching methods by a wide margin in linking
mid-20th century Japanese firms across financial documents. A purely
self-supervised model - trained only by aligning the embeddings for the image
crop of a firm name and its corresponding OCR'ed text - also outperforms
popular string matching methods. Fascinatingly, a multimodally pre-trained
vision-only encoder outperforms a unimodally pre-trained vision-only encoder,
illustrating the power of multimodal pre-training even if only one modality is
available for linking at inference time.
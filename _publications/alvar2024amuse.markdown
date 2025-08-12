---
layout: publication
title: 'AMUSE: Adaptive Multi-segment Encoding For Dataset Watermarking'
authors: Saeed Ranjbar Alvar, Mohammad Akbari, David Ming Xuan Yue, Yong Zhang
conference: Arxiv
year: 2024
bibkey: alvar2024amuse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.05628'}]
tags: ["Datasets"]
short_authors: Alvar et al.
---
Curating high quality datasets that play a key role in the emergence of new
AI applications requires considerable time, money, and computational resources.
So, effective ownership protection of datasets is becoming critical. Recently,
to protect the ownership of an image dataset, imperceptible watermarking
techniques are used to store ownership information (i.e., watermark) into the
individual image samples. Embedding the entire watermark into all samples leads
to significant redundancy in the embedded information which damages the
watermarked dataset quality and extraction accuracy. In this paper, a
multi-segment encoding-decoding method for dataset watermarking (called AMUSE)
is proposed to adaptively map the original watermark into a set of shorter
sub-messages and vice versa. Our message encoder is an adaptive method that
adjusts the length of the sub-messages according to the protection requirements
for the target dataset. Existing image watermarking methods are then employed
to embed the sub-messages into the original images in the dataset and also to
extract them from the watermarked images. Our decoder is then used to
reconstruct the original message from the extracted sub-messages. The proposed
encoder and decoder are plug-and-play modules that can easily be added to any
watermarking method. To this end, extensive experiments are preformed with
multiple watermarking solutions which show that applying AMUSE improves the
overall message extraction accuracy upto 28% for the same given dataset
quality. Furthermore, the image dataset quality is enhanced by a PSNR of
\(\approx\)2 dB on average, while improving the extraction accuracy for one of
the tested image watermarking methods.
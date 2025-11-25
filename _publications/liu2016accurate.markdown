---
layout: publication
title: Accurate Deep Representation Quantization With Gradient Snapping Layer For
  Similarity Search
authors: Shicong Liu, Hongtao Lu
conference: Arxiv
year: 2016
bibkey: liu2016accurate
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.09645'}]
tags: ["Quantization", "Similarity Search"]
short_authors: Shicong Liu, Hongtao Lu
---
Recent advance of large scale similarity search involves using deeply learned
representations to improve the search accuracy and use vector quantization
methods to increase the search speed. However, how to learn deep
representations that strongly preserve similarities between data pairs and can
be accurately quantized via vector quantization remains a challenging task.
Existing methods simply leverage quantization loss and similarity loss, which
result in unexpectedly biased back-propagating gradients and affect the search
performances. To this end, we propose a novel gradient snapping layer (GSL) to
directly regularize the back-propagating gradient towards a neighboring
codeword, the generated gradients are un-biased for reducing similarity loss
and also propel the learned representations to be accurately quantized. Joint
deep representation and vector quantization learning can be easily performed by
alternatively optimize the quantization codebook and the deep neural network.
The proposed framework is compatible with various existing vector quantization
approaches. Experimental results demonstrate that the proposed framework is
effective, flexible and outperforms the state-of-the-art large scale similarity
search methods.
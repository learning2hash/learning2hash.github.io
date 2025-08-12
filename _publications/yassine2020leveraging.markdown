---
layout: publication
title: Leveraging Subword Embeddings For Multinational Address Parsing
authors: "Marouane Yassine, David Beauchemin, Fran\xE7ois Laviolette, Luc Lamontagne"
conference: 2020 6th IEEE Congress on Information Science and Technology (CiSt)
year: 2020
bibkey: yassine2020leveraging
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.16152'}]
tags: []
short_authors: Yassine et al.
---
Address parsing consists of identifying the segments that make up an address
such as a street name or a postal code. Because of its importance for tasks
like record linkage, address parsing has been approached with many techniques.
Neural network methods defined a new state-of-the-art for address parsing.
While this approach yielded notable results, previous work has only focused on
applying neural networks to achieve address parsing of addresses from one
source country. We propose an approach in which we employ subword embeddings
and a Recurrent Neural Network architecture to build a single model capable of
learning to parse addresses from multiple countries at the same time while
taking into account the difference in languages and address formatting systems.
We achieved accuracies around 99 % on the countries used for training with no
pre-processing nor post-processing needed. We explore the possibility of
transferring the address parsing knowledge obtained by training on some
countries' addresses to others with no further training in a zero-shot transfer
learning setting. We achieve good results for 80 % of the countries (33 out of
41), almost 50 % of which (20 out of 41) is near state-of-the-art performance.
In addition, we propose an open-source Python implementation of our trained
models.
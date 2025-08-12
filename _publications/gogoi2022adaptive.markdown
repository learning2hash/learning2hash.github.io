---
layout: publication
title: Adaptive Prototypical Networks
authors: Manas Gogoi, Sambhavi Tiwari, Shekhar Verma
conference: Arxiv
year: 2022
bibkey: gogoi2022adaptive
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.12479'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Manas Gogoi, Sambhavi Tiwari, Shekhar Verma
---
Prototypical network for Few shot learning tries to learn an embedding
function in the encoder that embeds images with similar features close to one
another in the embedding space. However, in this process, the support set
samples for a task are embedded independently of one other, and hence, the
inter-class closeness is not taken into account. Thus, in the presence of
similar-looking classes in a task, the embeddings will tend to be close to each
other in the embedding space and even possibly overlap in some regions, which
is not desirable for classification. In this paper, we propose an approach that
intuitively pushes the embeddings of each of the classes away from the others
in the meta-testing phase, thereby grouping them closely based on the distinct
class labels rather than only the similarity of spatial features. This is
achieved by training the encoder network for classification using the support
set samples and labels of the new task. Extensive experiments conducted on
benchmark data sets show improvements in meta-testing accuracy when compared
with Prototypical Networks and also other standard few-shot learning models.
---
layout: publication
title: 'SIR: Similar Image Retrieval For Product Search In E-commerce'
authors: Theban Stanley, Nihar Vanjara, Yanxin Pan, Ekaterina Pirogova, Swagata Chakraborty,
  Abon Chaudhuri
conference: Lecture Notes in Computer Science
year: 2020
bibkey: stanley2020sir
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.13836'}]
tags: [Text Retrieval, Evaluation, Supervised, Image Retrieval]
short_authors: Stanley et al.
---
We present a similar image retrieval (SIR) platform that is used to quickly
discover visually similar products in a catalog of millions. Given the size,
diversity, and dynamism of our catalog, product search poses many challenges.
It can be addressed by building supervised models to tagging product images
with labels representing themes and later retrieving them by labels. This
approach suffices for common and perennial themes like "white shirt" or
"lifestyle image of TV". It does not work for new themes such as
"e-cigarettes", hard-to-define ones such as "image with a promotional badge",
or the ones with short relevance span such as "Halloween costumes". SIR is
ideal for such cases because it allows us to search by an example, not a
pre-defined theme. We describe the steps - embedding computation, encoding, and
indexing - that power the approximate nearest neighbor search back-end. We also
highlight two applications of SIR. The first one is related to the detection of
products with various types of potentially objectionable themes. This
application is run with a sense of urgency, hence the typical time frame to
train and bootstrap a model is not permitted. Also, these themes are often
short-lived based on current trends, hence spending resources to build a
lasting model is not justified. The second application is a variant item
detection system where SIR helps discover visual variants that are hard to find
through text search. We analyze the performance of SIR in the context of these
applications.
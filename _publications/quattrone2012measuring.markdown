---
layout: publication
title: Measuring Similarity In Large-scale Folksonomies
authors: Giovanni Quattrone, Emilio Ferrara, Pasquale de Meo, Licia Capra
conference: SEKE 11 Proceedings of the 23rd International Conference on Software Engineering
  and Knowledge Engineering pp. 385-391 2011
year: 2012
bibkey: quattrone2012measuring
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1207.6037'}]
tags: ["Distance Metric Learning"]
short_authors: Quattrone et al.
---
Social (or folksonomic) tagging has become a very popular way to describe
content within Web 2.0 websites. Unlike taxonomies, which overimpose a
hierarchical categorisation of content, folksonomies enable end-users to freely
create and choose the categories (in this case, tags) that best describe some
content. However, as tags are informally defined, continually changing, and
ungoverned, social tagging has often been criticised for lowering, rather than
increasing, the efficiency of searching, due to the number of synonyms,
homonyms, polysemy, as well as the heterogeneity of users and the noise they
introduce. To address this issue, a variety of approaches have been proposed
that recommend users what tags to use, both when labelling and when looking for
resources.
  As we illustrate in this paper, real world folksonomies are characterized by
power law distributions of tags, over which commonly used similarity metrics,
including the Jaccard coefficient and the cosine similarity, fail to compute.
We thus propose a novel metric, specifically developed to capture similarity in
large-scale folksonomies, that is based on a mutual reinforcement principle:
that is, two tags are deemed similar if they have been associated to similar
resources, and vice-versa two resources are deemed similar if they have been
labelled by similar tags. We offer an efficient realisation of this similarity
metric, and assess its quality experimentally, by comparing it against cosine
similarity, on three large-scale datasets, namely Bibsonomy, MovieLens and
CiteULike.
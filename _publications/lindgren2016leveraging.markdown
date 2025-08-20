---
layout: publication
title: Leveraging Sparsity For Efficient Submodular Data Summarization
authors: Erik M. Lindgren, Shanshan Wu, Alexandros G. Dimakis
conference: Arxiv
year: 2016
bibkey: lindgren2016leveraging
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.02690'}]
tags: [Locality Sensitive Hashing, Hashing Methods, Datasets, Image Retrieval]
short_authors: Erik M. Lindgren, Shanshan Wu, Alexandros G. Dimakis
---
The facility location problem is widely used for summarizing large datasets
and has additional applications in sensor placement, image retrieval, and
clustering. One difficulty of this problem is that submodular optimization
algorithms require the calculation of pairwise benefits for all items in the
dataset. This is infeasible for large problems, so recent work proposed to only
calculate nearest neighbor benefits. One limitation is that several strong
assumptions were invoked to obtain provable approximation guarantees. In this
paper we establish that these extra assumptions are not necessary---solving the
sparsified problem will be almost optimal under the standard assumptions of the
problem. We then analyze a different method of sparsification that is a better
model for methods such as Locality Sensitive Hashing to accelerate the nearest
neighbor computations and extend the use of the problem to a broader family of
similarities. We validate our approach by demonstrating that it rapidly
generates interpretable summaries.
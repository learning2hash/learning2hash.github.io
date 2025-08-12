---
layout: publication
title: Named Entity Linking With Entity Representation By Multiple Embeddings
authors: Oleg Vasilyev, Alex Dauenhauer, Vedant Dharnidharka, John Bohannon
conference: Arxiv
year: 2022
bibkey: vasilyev2022named
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.10498'}]
tags: ["Datasets", "Evaluation", "Survey Paper"]
short_authors: Vasilyev et al.
---
We propose a simple and practical method for named entity linking (NEL),
based on entity representation by multiple embeddings. To explore this method,
and to review its dependency on parameters, we measure its performance on
Namesakes, a highly challenging dataset of ambiguously named entities. Our
observations suggest that the minimal number of mentions required to create a
knowledge base (KB) entity is very important for NEL performance. The number of
embeddings is less important and can be kept small, within as few as 10 or
less. We show that our representations of KB entities can be adjusted using
only KB data, and the adjustment can improve NEL performance. We also compare
NEL performance of embeddings obtained from tuning language model on diverse
news texts as opposed to tuning on more uniform texts from public datasets
XSum, CNN / Daily Mail. We found that tuning on diverse news provides better
embeddings.
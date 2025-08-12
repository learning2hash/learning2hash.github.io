---
layout: publication
title: Corpus-level Fine-grained Entity Typing
authors: "Yadollah Yaghoobzadeh, Heike Adel, Hinrich Sch\xFCtze"
conference: Journal of Artificial Intelligence Research
year: 2018
bibkey: yaghoobzadeh2017corpus
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.02275'}]
tags: ["Datasets"]
short_authors: "Yadollah Yaghoobzadeh, Heike Adel, Hinrich Sch\xFCtze"
---
This paper addresses the problem of corpus-level entity typing, i.e.,
inferring from a large corpus that an entity is a member of a class such as
"food" or "artist". The application of entity typing we are interested in is
knowledge base completion, specifically, to learn which classes an entity is a
member of. We propose FIGMENT to tackle this problem. FIGMENT is embedding-
based and combines (i) a global model that scores based on aggregated
contextual information of an entity and (ii) a context model that first scores
the individual occurrences of an entity and then aggregates the scores. Each of
the two proposed models has some specific properties. For the global model,
learning high quality entity representations is crucial because it is the only
source used for the predictions. Therefore, we introduce representations using
name and contexts of entities on the three levels of entity, word, and
character. We show each has complementary information and a multi-level
representation is the best. For the context model, we need to use distant
supervision since the context-level labels are not available for entities.
Distant supervised labels are noisy and this harms the performance of models.
Therefore, we introduce and apply new algorithms for noise mitigation using
multi-instance learning. We show the effectiveness of our models in a large
entity typing dataset, built from Freebase.
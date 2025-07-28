---
layout: publication
title: 'Recipe: Does A Multi-modal Recipe Knowledge Graph Fit A Multi-purpose Recommendation
  System?'
authors: Ali Pesaranghader, Touqir Sajed
conference: Arxiv
year: 2023
bibkey: pesaranghader2023recipe
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.04579'}]
tags: ["Recommender Systems"]
short_authors: Ali Pesaranghader, Touqir Sajed
---
Over the past two decades, recommendation systems (RSs) have used machine
learning (ML) solutions to recommend items, e.g., movies, books, and
restaurants, to clients of a business or an online platform. Recipe
recommendation, however, has not yet received much attention compared to those
applications. We introduce RECipe as a multi-purpose recipe recommendation
framework with a multi-modal knowledge graph (MMKG) backbone. The motivation
behind RECipe is to go beyond (deep) neural collaborative filtering (NCF) by
recommending recipes to users when they query in natural language or by
providing an image. RECipe consists of 3 subsystems: (1) behavior-based
recommender, (2) review-based recommender, and (3) image-based recommender.
Each subsystem relies on the embedding representations of entities and
relations in the graph. We first obtain (pre-trained) embedding representations
of textual entities, such as reviews or ingredients, from a fine-tuned model of
Microsoft's MPNet. We initialize the weights of the entities with these
embeddings to train our knowledge graph embedding (KGE) model. For the visual
component, i.e., recipe images, we develop a KGE-Guided variational autoencoder
(KG-VAE) to learn the distribution of images and their latent representations.
Once KGE and KG-VAE models are fully trained, we use them as a multi-purpose
recommendation framework. For benchmarking, we created two knowledge graphs
(KGs) from public datasets on Kaggle for recipe recommendation. Our experiments
show that the KGE models have comparable performance to the neural solutions.
We also present pre-trained NLP embeddings to address important applications
such as zero-shot inference for new users (or the cold start problem) and
conditional recommendation with respect to recipe categories. We eventually
demonstrate the application of RECipe in a multi-purpose recommendation
setting.
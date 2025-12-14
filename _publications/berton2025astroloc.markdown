---
layout: publication
title: 'Astroloc: Robust Space To Ground Image Localizer'
authors: Gabriele Berton, Alex Stoken, Carlo Masone
conference: Arxiv
year: 2025
bibkey: berton2025astroloc
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.07003'}]
tags: [Evaluation, Supervised, Image Retrieval, Datasets, Unsupervised]
short_authors: Gabriele Berton, Alex Stoken, Carlo Masone
---
Astronauts take thousands of photos of Earth per day from the International
Space Station, which, once localized on Earth's surface, are used for a
multitude of tasks, ranging from climate change research to disaster
management. The localization process, which has been performed manually for
decades, has recently been approached through image retrieval solutions: given
an astronaut photo, find its most similar match among a large database of
geo-tagged satellite images, in a task called Astronaut Photography
Localization (APL). Yet, existing APL approaches are trained only using
satellite images, without taking advantage of the millions open-source
astronaut photos. In this work we present the first APL pipeline capable of
leveraging astronaut photos for training. We first produce full localization
information for 300,000 manually weakly labeled astronaut photos through an
automated pipeline, and then use these images to train a model, called
AstroLoc. AstroLoc learns a robust representation of Earth's surface features
through two losses: astronaut photos paired with their matching satellite
counterparts in a pairwise loss, and a second loss on clusters of satellite
imagery weighted by their relevance to astronaut photography via unsupervised
mining. We find that AstroLoc achieves a staggering 35% average improvement in
recall@1 over previous SOTA, pushing the limits of existing datasets with a
recall@100 consistently over 99%. Finally, we note that AstroLoc, without any
fine-tuning, provides excellent results for related tasks like the
lost-in-space satellite problem and historical space imagery localization.
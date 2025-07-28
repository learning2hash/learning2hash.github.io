---
layout: publication
title: 'Banknote-net: Open Dataset For Assistive Universal Currency Recognition'
authors: Felipe Oviedo, Srinivas Vinnakota, Eugene Seleznev, Hemant Malhotra, Saqib
  Shaikh, Juan Lavista Ferres
conference: Arxiv
year: 2022
bibkey: oviedo2022banknote
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.03738'}]
tags: ["Datasets"]
short_authors: Oviedo et al.
---
Millions of people around the world have low or no vision. Assistive software
applications have been developed for a variety of day-to-day tasks, including
optical character recognition, scene identification, person recognition, and
currency recognition. This last task, the recognition of banknotes from
different denominations, has been addressed by the use of computer vision
models for image recognition. However, the datasets and models available for
this task are limited, both in terms of dataset size and in variety of
currencies covered. In this work, we collect a total of 24,826 images of
banknotes in variety of assistive settings, spanning 17 currencies and 112
denominations. Using supervised contrastive learning, we develop a machine
learning model for universal currency recognition. This model learns compliant
embeddings of banknote images in a variety of contexts, which can be shared
publicly (as a compressed vector representation), and can be used to train and
test specialized downstream models for any currency, including those not
covered by our dataset or for which only a few real images per denomination are
available (few-shot learning). We deploy a variation of this model for public
use in the last version of the Seeing AI app developed by Microsoft. We share
our encoder model and the embeddings as an open dataset in our BankNote-Net
repository.
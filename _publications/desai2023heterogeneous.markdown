---
layout: publication
title: 'Heterogeneous Federated Collaborative Filtering Using FAIR: Federated Averaging
  In Random Subspaces'
authors: Aditya Desai, Benjamin Meisburger, Zichang Liu, Anshumali Shrivastava
conference: Arxiv
year: 2023
bibkey: desai2023heterogeneous
citations: 0
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/2311.01722'}]
tags: ["Datasets", "Hashing Methods", "Locality-Sensitive-Hashing", "Recommender Systems"]
short_authors: Desai et al.
---
Recommendation systems (RS) for items (e.g., movies, books) and ads are
widely used to tailor content to users on various internet platforms.
Traditionally, recommendation models are trained on a central server. However,
due to rising concerns for data privacy and regulations like the GDPR,
federated learning is an increasingly popular paradigm in which data never
leaves the client device. Applying federated learning to recommendation models
is non-trivial due to large embedding tables, which often exceed the memory
constraints of most user devices. To include data from all devices in federated
learning, we must enable collective training of embedding tables on devices
with heterogeneous memory capacities. Current solutions to heterogeneous
federated learning can only accommodate a small range of capacities and thus
limit the number of devices that can participate in training. We present
Federated Averaging in Random subspaces (FAIR), which allows arbitrary
compression of embedding tables based on device capacity and ensures the
participation of all devices in training. FAIR uses what we call consistent and
collapsible subspaces defined by hashing-based random projections to jointly
train large embedding tables while using varying amounts of compression on user
devices. We evaluate FAIR on Neural Collaborative Filtering tasks with multiple
datasets and verify that FAIR can gather and share information from a wide
range of devices with varying capacities, allowing for seamless collaboration.
We prove the convergence of FAIR in the homogeneous setting with non-i.i.d data
distribution. Our code is open source at \{https://github.com/apd10/FLCF\}
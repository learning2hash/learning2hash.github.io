---
layout: publication
title: 'Faircop: Facial Image Retrieval Using Contrastive Personalization'
authors: Devansh Gupta, Aditya Saini, Drishti Bhasin, Sarthak Bhagat, Shagun Uppal,
  Rishi Raj Jain, Ponnurangam Kumaraguru, Rajiv Ratn Shah
conference: Arxiv
year: 2022
bibkey: gupta2022faircop
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.15870'}]
tags: [Image Retrieval, Efficiency, Self-Supervised, Datasets, Scalability, Tools
    & Libraries, Recommender Systems]
short_authors: Gupta et al.
---
Retrieving facial images from attributes plays a vital role in various
systems such as face recognition and suspect identification. Compared to other
image retrieval tasks, facial image retrieval is more challenging due to the
high subjectivity involved in describing a person's facial features. Existing
methods do so by comparing specific characteristics from the user's mental
image against the suggested images via high-level supervision such as using
natural language. In contrast, we propose a method that uses a relatively
simpler form of binary supervision by utilizing the user's feedback to label
images as either similar or dissimilar to the target image. Such supervision
enables us to exploit the contrastive learning paradigm for encapsulating each
user's personalized notion of similarity. For this, we propose a novel loss
function optimized online via user feedback. We validate the efficacy of our
proposed approach using a carefully designed testbed to simulate user feedback
and a large-scale user study. Our experiments demonstrate that our method
iteratively improves personalization, leading to faster convergence and
enhanced recommendation relevance, thereby, improving user satisfaction. Our
proposed framework is also equipped with a user-friendly web interface with a
real-time experience for facial image retrieval.
---
layout: publication
title: Understanding And Detecting Hateful Content Using Contrastive Learning
authors: "Felipe Gonz\xE1lez-Pizarro, Savvas Zannettou"
conference: Proceedings of the International AAAI Conference on Web and Social Media
year: 2023
bibkey: "gonz\xE1lezpizarro2023understanding"
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.08387'}]
tags: ["AAAI", "Datasets", "Evaluation", "Self-Supervised", "Tools & Libraries"]
short_authors: "Felipe Gonz\xE1lez-Pizarro, Savvas Zannettou"
---
The spread of hate speech and hateful imagery on the Web is a significant
problem that needs to be mitigated to improve our Web experience. This work
contributes to research efforts to detect and understand hateful content on the
Web by undertaking a multimodal analysis of Antisemitism and Islamophobia on
4chan's /pol/ using OpenAI's CLIP. This large pre-trained model uses the
Contrastive Learning paradigm. We devise a methodology to identify a set of
Antisemitic and Islamophobic hateful textual phrases using Google's Perspective
API and manual annotations. Then, we use OpenAI's CLIP to identify images that
are highly similar to our Antisemitic/Islamophobic textual phrases. By running
our methodology on a dataset that includes 66M posts and 5.8M images shared on
4chan's /pol/ for 18 months, we detect 173K posts containing 21K
Antisemitic/Islamophobic images and 246K posts that include 420 hateful
phrases. Among other things, we find that we can use OpenAI's CLIP model to
detect hateful content with an accuracy score of 0.81 (F1 score = 0.54). By
comparing CLIP with two baselines proposed by the literature, we find that CLIP
outperforms them, in terms of accuracy, precision, and F1 score, in detecting
Antisemitic/Islamophobic images. Also, we find that Antisemitic/Islamophobic
imagery is shared in a similar number of posts on 4chan's /pol/ compared to
Antisemitic/Islamophobic textual phrases, highlighting the need to design more
tools for detecting hateful imagery. Finally, we make available (upon request)
a dataset of 246K posts containing 420 Antisemitic/Islamophobic phrases and 21K
likely Antisemitic/Islamophobic images (automatically detected by CLIP) that
can assist researchers in further understanding Antisemitism and Islamophobia.
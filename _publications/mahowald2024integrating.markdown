---
layout: publication
title: Integrating Visual And Textual Inputs For Searching Large-scale Map Collections
  With CLIP
authors: Jamie Mahowald, Benjamin Charles Germain Lee
conference: Arxiv
year: 2024
bibkey: mahowald2024integrating
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.01190'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Scalability", "Tools & Libraries"]
short_authors: Jamie Mahowald, Benjamin Charles Germain Lee
---
Despite the prevalence and historical importance of maps in digital
collections, current methods of navigating and exploring map collections are
largely restricted to catalog records and structured metadata. In this paper,
we explore the potential for interactively searching large-scale map
collections using natural language inputs ("maps with sea monsters"), visual
inputs (i.e., reverse image search), and multimodal inputs (an example map +
"more grayscale"). As a case study, we adopt 562,842 images of maps publicly
accessible via the Library of Congress's API. To accomplish this, we use the
mulitmodal Contrastive Language-Image Pre-training (CLIP) machine learning
model to generate embeddings for these maps, and we develop code to implement
exploratory search capabilities with these input strategies. We present results
for example searches created in consultation with staff in the Library of
Congress's Geography and Map Division and describe the strengths, weaknesses,
and possibilities for these search queries. Moreover, we introduce a
fine-tuning dataset of 10,504 map-caption pairs, along with an architecture for
fine-tuning a CLIP model on this dataset. To facilitate re-use, we provide all
of our code in documented, interactive Jupyter notebooks and place all code
into the public domain. Lastly, we discuss the opportunities and challenges for
applying these approaches across both digitized and born-digital collections
held by galleries, libraries, archives, and museums.
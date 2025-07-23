---
layout: publication
title: 'NUDGE: Lightweight Non-parametric Fine-tuning Of Embeddings For Retrieval'
authors: Zeighami Sepanta, Wellmer Zac, Parameswaran Aditya
conference: Arxiv
year: 2024
bibkey: zeighami2024nudge
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.02343'}]
tags: ["Datasets", "Efficiency", "Image Retrieval", "Similarity Search"]
short_authors: Zeighami Sepanta, Wellmer Zac, Parameswaran Aditya
---
\\(k\\)-Nearest Neighbor search on dense vector embeddings (\\(k\\)-NN retrieval)
from pre-trained embedding models is the predominant retrieval method for text
and images, as well as Retrieval-Augmented Generation (RAG) pipelines. In
practice, application developers often fine-tune the embeddings to improve
their accuracy on the dataset and query workload in hand. Existing approaches
either fine-tune the pre-trained model itself or, more efficiently, but at the
cost of accuracy, train adaptor models to transform the output of the
pre-trained model. We present NUDGE, a family of novel non-parametric embedding
fine-tuning approaches that are significantly more accurate and efficient than
both sets of existing approaches. NUDGE directly modifies the embeddings of
data records to maximize the accuracy of \\(k\\)-NN retrieval. We present a
thorough theoretical and experimental study of NUDGE's non-parametric approach.
We show that even though the underlying problem is NP-Hard, constrained
variations can be solved efficiently. These constraints additionally ensure
that the changes to the embeddings are modest, avoiding large distortions to
the semantics learned during pre-training. In experiments across five
pre-trained models and nine standard text and image retrieval datasets, NUDGE
runs in minutes and often improves NDCG@10 by more than 10% over existing
fine-tuning methods. On average, NUDGE provides 3.3x and 4.3x higher increase
in accuracy and runs 200x and 3x faster, respectively, over fine-tuning the
pre-trained model and training adaptors.
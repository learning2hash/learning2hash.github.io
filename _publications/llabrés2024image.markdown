---
layout: publication
title: Image-text Matching For Large-scale Book Collections
authors: "Artemis Llabr\xE9s, Arka Ujjal Dey, Dimosthenis Karatzas, Ernest Valveny"
conference: Lecture Notes in Computer Science
year: 2024
bibkey: "llabr\xE9s2024image"
citations: 0
additional_links: [{name: Code, url: 'https://github.com/llabres/library-dataset'},
  {name: Paper, url: 'https://arxiv.org/abs/2407.19812'}]
tags: [Tools & Libraries, Datasets, Scalability]
short_authors: "Llabr\xE9s et al."
---
We address the problem of detecting and mapping all books in a collection of images to entries in a given book catalogue. Instead of performing independent retrieval for each book detected, we treat the image-text mapping problem as a many-to-many matching process, looking for the best overall match between the two sets. We combine a state-of-the-art segmentation method (SAM) to detect book spines and extract book information using a commercial OCR. We then propose a two-stage approach for text-image matching, where CLIP embeddings are used first for fast matching, followed by a second slower stage to refine the matching, employing either the Hungarian Algorithm or a BERT-based model trained to cope with noisy OCR input and partial text matches. To evaluate our approach, we publish a new dataset of annotated bookshelf images that covers the whole book collection of a public library in Spain. In addition, we provide two target lists of book metadata, a closed-set of 15k book titles that corresponds to the known library inventory, and an open-set of 2.3M book titles to simulate an open-world scenario. We report results on two settings, on one hand on a matching-only task, where the book segments and OCR is given and the objective is to perform many-to-many matching against the target lists, and a combined detection and matching task, where books must be first detected and recognised before they are matched to the target list entries. We show that both the Hungarian Matching and the proposed BERT-based model outperform a fuzzy string matching baseline, and we highlight inherent limitations of the matching algorithms as the target increases in size, and when either of the two sets (detected books or target book list) is incomplete. The dataset and code are available at https://github.com/llabres/library-dataset
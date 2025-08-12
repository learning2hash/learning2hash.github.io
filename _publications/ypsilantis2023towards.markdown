---
layout: publication
title: 'Towards Universal Image Embeddings: A Large-scale Dataset And Challenge For
  Generic Image Representations'
authors: "Nikolaos-Antonios Ypsilantis, Kaifeng Chen, Bingyi Cao, M\xE1rio Lipovsk\xFD\
  , Pelin Dogan-Sch\xF6nberger, Grzegorz Makosa, Boris Bluntschli, Mojtaba Seyedhosseini,\
  \ Ond\u0159ej Chum, Andr\xE9 Araujo"
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: ypsilantis2023towards
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01858'}]
tags: ["Datasets", "ICCV"]
short_authors: Ypsilantis et al.
---
Fine-grained and instance-level recognition methods are commonly trained and
evaluated on specific domains, in a model per domain scenario. Such an
approach, however, is impractical in real large-scale applications. In this
work, we address the problem of universal image embedding, where a single
universal model is trained and used in multiple domains. First, we leverage
existing domain-specific datasets to carefully construct a new large-scale
public benchmark for the evaluation of universal image embeddings, with 241k
query images, 1.4M index images and 2.8M training images across 8 different
domains and 349k classes. We define suitable metrics, training and evaluation
protocols to foster future research in this area. Second, we provide a
comprehensive experimental evaluation on the new dataset, demonstrating that
existing approaches and simplistic extensions lead to worse performance than an
assembly of models trained for each domain separately. Finally, we conducted a
public research competition on this topic, leveraging industrial datasets,
which attracted the participation of more than 1k teams worldwide. This
exercise generated many interesting research ideas and findings which we
present in detail. Project webpage: https://cmp.felk.cvut.cz/univ_emb/
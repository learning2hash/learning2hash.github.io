---
layout: publication
title: Efficient Medical Image Retrieval Using Densenet And FAISS For BIRADS Classification
authors: Md Shaikh Rahman, Feiroz Humayara, Syed Maudud E Rabbi, Muhammad Mahbubur
  Rashid
conference: Arxiv
year: 2024
bibkey: rahman2024efficient
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.01473'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Image Retrieval", "Similarity Search"]
short_authors: Rahman et al.
---
That datasets that are used in todays research are especially vast in the
medical field. Different types of medical images such as X-rays, MRI, CT scan
etc. take up large amounts of space. This volume of data introduces challenges
like accessing and retrieving specific images due to the size of the database.
An efficient image retrieval system is essential as the database continues to
grow to save time and resources. In this paper, we propose an approach to
medical image retrieval using DenseNet for feature extraction and use FAISS for
similarity search. DenseNet is well-suited for feature extraction in complex
medical images and FAISS enables efficient handling of high-dimensional data in
large-scale datasets. Unlike existing methods focused solely on classification
accuracy, our method prioritizes both retrieval speed and diagnostic relevance,
addressing a critical gap in real-time case comparison for radiologists. We
applied the classification of breast cancer images using the BIRADS system. We
utilized DenseNet's powerful feature representation and FAISSs efficient
indexing capabilities to achieve high precision and recall in retrieving
relevant images for diagnosis. We experimented on a dataset of 2006 images from
the Categorized Digital Database for Low Energy and Subtracted Contrast
Enhanced Spectral Mammography (CDD-CESM) images available on The Cancer Imaging
Archive (TCIA). Our method outperforms conventional retrieval techniques,
achieving a precision of 80% at k=5 for BIRADS classification. The dataset
includes annotated CESM images and medical reports, providing a comprehensive
foundation for our research.
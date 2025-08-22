---
layout: publication
title: Siamese Content-based Search Engine For A More Transparent Skin And Breast
  Cancer Diagnosis Through Histological Imaging
authors: "Zahra Tabatabaei, Adri\xE1n Colomer, Javier Oliver Moll, Valery Naranjo"
conference: Arxiv
year: 2024
bibkey: tabatabaei2024siamese
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.08272'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Tabatabaei et al.
---
Computer Aid Diagnosis (CAD) has developed digital pathology with Deep
Learning (DL)-based tools to assist pathologists in decision-making.
Content-Based Histopathological Image Retrieval (CBHIR) is a novel tool to seek
highly correlated patches in terms of similarity in histopathological features.
In this work, we proposed two CBHIR approaches on breast (Breast-twins) and
skin cancer (Skin-twins) data sets for robust and accurate patch-level
retrieval, integrating a custom-built Siamese network as a feature extractor.
The proposed Siamese network is able to generalize for unseen images by
focusing on the similar histopathological features of the input pairs. The
proposed CBHIR approaches are evaluated on the Breast (public) and Skin
(private) data sets with top K accuracy. Finding the optimum amount of K is
challenging, but also, as much as K increases, the dissimilarity between the
query and the returned images increases which might mislead the pathologists.
To the best of the author's belief, this paper is tackling this issue for the
first time on histopathological images by evaluating the top first retrieved
images. The Breast-twins model achieves 70% of the F1score at the top first,
which exceeds the other state-of-the-art methods at a higher amount of K such
as 5 and 400. Skin-twins overpasses the recently proposed Convolutional Auto
Encoder (CAE) by 67%, increasing the precision. Besides, the Skin-twins model
tackles the challenges of Spitzoid Tumors of Uncertain Malignant Potential
(STUMP) to assist pathologists with retrieving top K images and their
corresponding labels. So, this approach can offer a more explainable CAD tool
to pathologists in terms of transparency, trustworthiness, or reliability among
other characteristics.
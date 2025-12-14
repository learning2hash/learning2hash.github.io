---
layout: publication
title: 'Wwfedcbmir: World-wide Federated Content-based Medical Image Retrieval'
authors: "Zahra Tabatabaei, Yuandou Wang, Adri\xE1n Colomer, Javier Oliver Moll, Zhiming\
  \ Zhao, Valery Naranjo"
conference: Bioengineering
year: 2023
bibkey: tabatabaei2023wwfedcbmir
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.03383'}]
tags: [Evaluation, Image Retrieval]
short_authors: Tabatabaei et al.
---
The paper proposes a Federated Content-Based Medical Image Retrieval
(FedCBMIR) platform that utilizes Federated Learning (FL) to address the
challenges of acquiring a diverse medical data set for training CBMIR models.
CBMIR assists pathologists in diagnosing breast cancer more rapidly by
identifying similar medical images and relevant patches in prior cases compared
to traditional cancer detection methods. However, CBMIR in histopathology
necessitates a pool of Whole Slide Images (WSIs) to train to extract an optimal
embedding vector that leverages search engine performance, which may not be
available in all centers. The strict regulations surrounding data sharing in
medical data sets also hinder research and model development, making it
difficult to collect a rich data set. The proposed FedCBMIR distributes the
model to collaborative centers for training without sharing the data set,
resulting in shorter training times than local training. FedCBMIR was evaluated
in two experiments with three scenarios on BreaKHis and Camelyon17 (CAM17). The
study shows that the FedCBMIR method increases the F1-Score (F1S) of each
client to 98%, 96%, 94%, and 97% in the BreaKHis experiment with a generalized
model of four magnifications and does so in 6.30 hours less time than total
local training. FedCBMIR also achieves 98% accuracy with CAM17 in 2.49 hours
less training time than local training, demonstrating that our FedCBMIR is both
fast and accurate for both pathologists and engineers. In addition, our
FedCBMIR provides similar images with higher magnification for non-developed
countries where participate in the worldwide FedCBMIR with developed countries
to facilitate mitosis measuring in breast cancer diagnosis. We evaluate this
scenario by scattering BreaKHis into four centers with different
magnifications.
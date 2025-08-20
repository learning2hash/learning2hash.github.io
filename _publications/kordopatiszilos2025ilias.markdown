---
layout: publication
title: 'ILIAS: Instance-level Image Retrieval At Scale'
authors: "Giorgos Kordopatis-Zilos, Vladan Stojni\u0107, Anna Manko, Pavel \u0160\
  uma, Nikolaos-Antonios Ypsilantis, Nikos Efthymiadis, Zakaria Laskar, Ji\u0159\xED\
  \ Matas, Ond\u0159ej Chum, Giorgos Tolias"
conference: Arxiv
year: 2025
bibkey: kordopatiszilos2025ilias
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.11748'}]
tags: [Scalability, Datasets, Hybrid ANN Methods, Re-ranking, Image Retrieval, Evaluation]
short_authors: Kordopatis-Zilos et al.
---
This work introduces ILIAS, a new test dataset for Instance-Level Image retrieval At Scale. It is designed to evaluate the ability of current and future foundation models and retrieval techniques to recognize particular objects. The key benefits over existing datasets include large scale, domain diversity, accurate ground truth, and a performance that is far from saturated. ILIAS includes query and positive images for 1,000 object instances, manually collected to capture challenging conditions and diverse domains. Large-scale retrieval is conducted against 100 million distractor images from YFCC100M. To avoid false negatives without extra annotation effort, we include only query objects confirmed to have emerged after 2014, i.e. the compilation date of YFCC100M. An extensive benchmarking is performed with the following observations: i) models fine-tuned on specific domains, such as landmarks or products, excel in that domain but fail on ILIAS ii) learning a linear adaptation layer using multi-domain class supervision results in performance improvements, especially for vision-language models iii) local descriptors in retrieval re-ranking are still a key ingredient, especially in the presence of severe background clutter iv) the text-to-image performance of the vision-language foundation models is surprisingly close to the corresponding image-to-image case. website: https://vrg.fel.cvut.cz/ilias/
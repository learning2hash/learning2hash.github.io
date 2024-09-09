---
    layout: publication
    title: "Combating Ambiguity for Hash-code Learning in Medical Instance Retrieval"
    authors: Fang Jiansheng, Fu Huazhu, Zeng Dan, Yan Xiao, Yan Yuguang, Liu Jiang
    conference: Arxiv
    year: 2021
    bibkey: fang2021combating
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2105.08872"}
    tags: ['ARXIV']
    ---
    When encountering a dubious diagnostic case, medical instance retrieval can help radiologists make evidence-based diagnoses by finding images containing instances similar to a query case from a large image database. The similarity between the query case and retrieved similar cases is determined by visual features extracted from pathologically abnormal regions. However, the manifestation of these regions often lacks specificity, i.e., different diseases can have the same manifestation, and different manifestations may occur at different stages of the same disease. To combat the manifestation ambiguity in medical instance retrieval, we propose a novel deep framework called Y-Net, encoding images into compact hash-codes generated from convolutional features by feature aggregation. Y-Net can learn highly discriminative convolutional features by unifying the pixel-wise segmentation loss and classification loss. The segmentation loss allows exploring subtle spatial differences for good spatial-discriminability while the classification loss utilizes class-aware semantic information for good semantic-separability. As a result, Y-Net can enhance the visual features in pathologically abnormal regions and suppress the disturbing of the background during model training, which could effectively embed discriminative features into the hash-codes in the retrieval stage. Extensive experiments on two medical image datasets demonstrate that Y-Net can alleviate the ambiguity of pathologically abnormal regions and its retrieval performance outperforms the state-of-the-art method by an average of 9.27\% on the returned list of 10.
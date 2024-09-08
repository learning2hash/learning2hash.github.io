---
    layout: publication
    title: "Deep Binary Reconstruction for Cross-modal Hashing"
    authors: Li Xuelong, Hu Di, Nie Feiping
    conference: Arxiv
    year: 2017
    bibkey: li2017deep
    additional_links:
       - {name: "DOI", url: "10.1145/3123266.3123355"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1708.05127"}
    tags: ['GAN', 'Cross-Modal', 'Arxiv', 'Image Retrieval', 'Supervised', 'Unsupervised']
    ---
    With the increasing demand of massive multimodal data storage and organization, cross-modal retrieval based on hashing technique has drawn much attention nowadays. It takes the binary codes of one modality as the query to retrieve the relevant hashing codes of another modality. However, the existing binary constraint makes it difficult to find the optimal cross-modal hashing function. Most approaches choose to relax the constraint and perform thresholding strategy on the real-value representation instead of directly solving the original objective. In this paper, we first provide a concrete analysis about the effectiveness of multimodal networks in preserving the inter- and intra-modal consistency. Based on the analysis, we provide a so-called Deep Binary Reconstruction (DBRC) network that can directly learn the binary hashing codes in an unsupervised fashion. The superiority comes from a proposed simple but efficient activation function, named as Adaptive Tanh (ATanh). The ATanh function can adaptively learn the binary codes and be trained via back-propagation. Extensive experiments on three benchmark datasets demonstrate that DBRC outperforms several state-of-the-art methods in both image2text and text2image retrieval task.
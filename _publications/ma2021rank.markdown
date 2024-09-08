---
    layout: publication
    title: "Rank-Consistency Deep Hashing for Scalable Multi-Label Image Search"
    authors: Ma Cheng, Lu Jiwen, Zhou Jie
    conference: IEEE Transactions on Multimedia,
    year: 2021
    bibkey: ma2021rank
    additional_links:
       - {name: "DOI", url: "10.1109/TMM.2020.3034534"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2102.01486"}
    tags: ['TIP', 'IEEE Transactions on Multimedia,', 'Image Retrieval']
    ---
    As hashing becomes an increasingly appealing technique for large-scale image retrieval, multi-label hashing is also attracting more attention for the ability to exploit multi-level semantic contents. In this paper, we propose a novel deep hashing method for scalable multi-label image search. Unlike existing approaches with conventional objectives such as contrast and triplet losses, we employ a rank list, rather than pairs or triplets, to provide sufficient global supervision information for all the samples. Specifically, a new rank-consistency objective is applied to align the similarity orders from two spaces, the original space and the hamming space. A powerful loss function is designed to penalize the samples whose semantic similarity and hamming distance are mismatched in two spaces. Besides, a multi-label softmax cross-entropy loss is presented to enhance the discriminative power with a concise formulation of the derivative function. In order to manipulate the neighborhood structure of the samples with different labels, we design a multi-label clustering loss to cluster the hashing vectors of the samples with the same labels by reducing the distances between the samples and their multiple corresponding class centers. The state-of-the-art experimental results achieved on three public multi-label datasets, MIRFLICKR-25K, IAPRTC12 and NUS-WIDE, demonstrate the effectiveness of the proposed method.
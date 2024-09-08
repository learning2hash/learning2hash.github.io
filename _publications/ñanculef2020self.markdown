---
    layout: publication
    title: "Self-Supervised Bernoulli Autoencoders for Semi-Supervised Hashing"
    authors: Ñanculef Ricardo, Mena Francisco, Macaluso Antonio, Lodi Stefano, Sartori Claudio
    conference: Arxiv
    year: 2020
    bibkey: ñanculef2020self
    additional_links:
       - {name: "DOI", url: "10.1007/978-3-030-93420-0_25"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2007.08799"}
   - {name: "Code", url: "https://github.com/amacaluso/SSB-VAE."}
    tags: ['Self-Supervised', 'Arxiv', 'Semi-Supervised', 'Unsupervised', 'Supervised']
    ---
    Semantic hashing is an emerging technique for large-scale similarity search based on representing high-dimensional data using similarity-preserving binary codes used for efficient indexing and search. It has recently been shown that variational autoencoders, with Bernoulli latent representations parametrized by neural nets, can be successfully trained to learn such codes in supervised and unsupervised scenarios, improving on more traditional methods thanks to their ability to handle the binary constraints architecturally. However, the scenario where labels are scarce has not been studied yet. This paper investigates the robustness of hashing methods based on variational autoencoders to the lack of supervision, focusing on two semi-supervised approaches currently in use. The first augments the variational autoencoder's training objective to jointly model the distribution over the data and the class labels. The second approach exploits the annotations to define an additional pairwise loss that enforces consistency between the similarity in the code (Hamming) space and the similarity in the label space. Our experiments show that both methods can significantly increase the hash codes' quality. The pairwise approach can exhibit an advantage when the number of labelled points is large. However, we found that this method degrades quickly and loses its advantage when labelled samples decrease. To circumvent this problem, we propose a novel supervision method in which the model uses its label distribution predictions to implement the pairwise objective. Compared to the best baseline, this procedure yields similar performance in fully supervised settings but improves the results significantly when labelled data is scarce. Our code is made publicly available at https://github.com/amacaluso/SSB-VAE.
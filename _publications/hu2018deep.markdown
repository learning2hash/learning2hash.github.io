---
    layout: publication
    title: "Deep LDA Hashing"
    authors: Hu Di, Nie Feiping, Li Xuelong
    conference: Arxiv
    year: 2018
    bibkey: hu2018deep
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1810.03402"}
    tags: ['Supervised', 'Arxiv']
    ---
    The conventional supervised hashing methods based on classification do not entirely meet the requirements of hashing technique, but Linear Discriminant Analysis (LDA) does. In this paper, we propose to perform a revised LDA objective over deep networks to learn efficient hashing codes in a truly end-to-end fashion. However, the complicated eigenvalue decomposition within each mini-batch in every epoch has to be faced with when simply optimizing the deep network w.r.t. the LDA objective. In this work, the revised LDA objective is transformed into a simple least square problem, which naturally overcomes the intractable problems and can be easily solved by the off-the-shelf optimizer. Such deep extension can also overcome the weakness of LDA Hashing in the limited linear projection and feature learning. Amounts of experiments are conducted on three benchmark datasets. The proposed Deep LDA Hashing shows nearly 70 points improvement over the conventional one on the CIFAR-10 dataset. It also beats several state-of-the-art methods on various metrics.
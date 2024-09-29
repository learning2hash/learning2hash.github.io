---
layout: publication
title: Neural Locality Sensitive Hashing For Entity Blocking
authors: Wang Runhui, Kong Luyang, Tao Yefan, Borthwick Andrew, Golac Davor, Johnson Henrik, Hijazi Shadie, Deng Dong, Zhang Yongfeng
conference: "Arxiv"
year: 2024
bibkey: wang2024neural
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2401.18064"}
tags: ['ARXIV', 'LSH', 'Supervised']
---
Locality45;sensitive hashing (LSH) is a fundamental algorithmic technique widely employed in large45;scale data processing applications such as nearest45;neighbor search entity resolution and clustering. However its applicability in some real45;world scenarios is limited due to the need for careful design of hashing functions that align with specific metrics. Existing LSH45;based Entity Blocking solutions primarily rely on generic similarity metrics such as Jaccard similarity whereas practical use cases often demand complex and customized similarity rules surpassing the capabilities of generic similarity metrics. Consequently designing LSH functions for these customized similarity rules presents considerable challenges. In this research we propose a neuralization approach to enhance locality45;sensitive hashing by training deep neural networks to serve as hashing functions for complex metrics. We assess the effectiveness of this approach within the context of the entity resolution problem which frequently involves the use of task45;specific metrics in real45;world applications. Specifically we introduce NLSHBlock (Neural45;LSH Block) a novel blocking methodology that leverages pre45;trained language models fine45;tuned with a novel LSH45;based loss function. Through extensive evaluations conducted on a diverse range of real45;world datasets we demonstrate the superiority of NLSHBlock over existing methods exhibiting significant performance improvements. Furthermore we showcase the efficacy of NLSHBlock in enhancing the performance of the entity matching phase particularly within the semi45;supervised setting.

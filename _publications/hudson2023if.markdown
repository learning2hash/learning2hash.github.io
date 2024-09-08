---
    layout: publication
    title: "If At First You Don't Succeed: Test Time Re-ranking for Zero-shot, Cross-domain Retrieval"
    authors: Hudson Finlay G. C., Smith William A. P.
    conference: Arxiv
    year: 2023
    bibkey: hudson2023if
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2303.17703"}
    tags: ['Image Retrieval', 'Arxiv']
    ---
    In this paper we propose a novel method for zero-shot, cross-domain image retrieval in which we make two key contributions. The first is a test-time re-ranking procedure that enables query-gallery pairs, without meaningful shared visual features, to be matched by incorporating gallery-gallery ranks into an iterative re-ranking process. The second is the use of cross-attention at training time and knowledge distillation to encourage cross-attention-like features to be extracted at test time from a single image. When combined with the Vision Transformer architecture and zero-shot retrieval losses, our approach yields state-of-the-art results on the Sketchy and TU-Berlin sketch-based image retrieval benchmarks. However, unlike many previous methods, none of the components in our approach are engineered specifically towards the sketch-based image retrieval task - it can be generally applied to any cross-domain, zero-shot retrieval task. We therefore also show results on zero-shot cartoon-to-photo retrieval using the Office-Home dataset.
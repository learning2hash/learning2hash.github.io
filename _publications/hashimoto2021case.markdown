---
layout: publication
title: Case-based Similar Image Retrieval For Weakly Annotated Large Histopathological
  Images Of Malignant Lymphoma Using Deep Metric Learning
authors: Noriaki Hashimoto, Yusuke Takagi, Hiroki Masuda, Hiroaki Miyoshi, Kei Kohno,
  Miharu Nagaishi, Kensaku Sato, Mai Takeuchi, Takuya Furuta, Keisuke Kawamoto, Kyohei
  Yamada, Mayuko Moritsubo, Kanako Inoue, Yasumasa Shimasaki, Yusuke Ogura, Teppei
  Imamoto, Tatsuzo Mishina, Ken Tanaka, Yoshino Kawaguchi, Shigeo Nakamura, Koichi
  Ohshima, Hidekata Hontani, Ichiro Takeuchi
conference: Medical Image Analysis
year: 2023
bibkey: hashimoto2021case
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.03602'}]
tags: ["Distance Metric Learning", "Evaluation", "Image Retrieval", "Supervised"]
short_authors: Hashimoto et al.
---
In the present study, we propose a novel case-based similar image retrieval
(SIR) method for hematoxylin and eosin (H&E)-stained histopathological images
of malignant lymphoma. When a whole slide image (WSI) is used as an input
query, it is desirable to be able to retrieve similar cases by focusing on
image patches in pathologically important regions such as tumor cells. To
address this problem, we employ attention-based multiple instance learning,
which enables us to focus on tumor-specific regions when the similarity between
cases is computed. Moreover, we employ contrastive distance metric learning to
incorporate immunohistochemical (IHC) staining patterns as useful supervised
information for defining appropriate similarity between heterogeneous malignant
lymphoma cases. In the experiment with 249 malignant lymphoma patients, we
confirmed that the proposed method exhibited higher evaluation measures than
the baseline case-based SIR methods. Furthermore, the subjective evaluation by
pathologists revealed that our similarity measure using IHC staining patterns
is appropriate for representing the similarity of H&E-stained tissue images for
malignant lymphoma.
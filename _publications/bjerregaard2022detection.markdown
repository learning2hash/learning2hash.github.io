---
layout: publication
title: Detection Of Furigana Text In Images
authors: "Nikolaj Kj\xF8ller Bjerregaard, Veronika Cheplygina, Stefan Heinrich"
conference: Arxiv
year: 2022
bibkey: bjerregaard2022detection
citations: 3
additional_links: [{name: Code, url: 'https://github.com/nikolajkb/FuriganaDetection\'},
  {name: Paper, url: 'https://arxiv.org/abs/2207.03960'}]
tags: ["Datasets", "Evaluation"]
short_authors: "Nikolaj Kj\xF8ller Bjerregaard, Veronika Cheplygina, Stefan Heinrich"
---
Furigana are pronunciation notes used in Japanese writing. Being able to
detect these can help improve optical character recognition (OCR) performance
or make more accurate digital copies of Japanese written media by correctly
displaying furigana. This project focuses on detecting furigana in Japanese
books and comics. While there has been research into the detection of Japanese
text in general, there are currently no proposed methods for detecting
furigana.
  We construct a new dataset containing Japanese written media and annotations
of furigana. We propose an evaluation metric for such data which is similar to
the evaluation protocols used in object detection except that it allows groups
of objects to be labeled by one annotation. We propose a method for detection
of furigana that is based on mathematical morphology and connected component
analysis. We evaluate the detections of the dataset and compare different
methods for text extraction. We also evaluate different types of images such as
books and comics individually and discuss the challenges of each type of image.
  The proposed method reaches an F1-score of 76% on the dataset. The method
performs well on regular books, but less so on comics, and books of irregular
format. Finally, we show that the proposed method can improve the performance
of OCR by 5% on the manga109 dataset.
  Source code is available via
\texttt\{https://github.com/nikolajkb/FuriganaDetection\}
---
layout: publication
title: Date-field Retrieval In Scene Image And Video Frames Using Text Enhancement
  And Shape Coding
authors: Partha Pratim Roy, Ayan Kumar Bhunia, Umapada Pal
conference: Neurocomputing
year: 2017
bibkey: roy2017date
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.06833'}]
tags: []
short_authors: Partha Pratim Roy, Ayan Kumar Bhunia, Umapada Pal
---
Text recognition in scene image and video frames is difficult because of low
resolution, blur, background noise, etc. Since traditional OCRs do not perform
well in such images, information retrieval using keywords could be an
alternative way to index/retrieve such text information. Date is a useful piece
of information which has various applications including date-wise videos/scene
searching, indexing or retrieval. This paper presents a date spotting based
information retrieval system for natural scene image and video frames where
text appears with complex backgrounds. We propose a line based date spotting
approach using Hidden Markov Model (HMM) which is used to detect the date
information in a given text. Different date models are searched from a line
without segmenting characters or words. Given a text line image in RGB, we
apply an efficient gray image conversion to enhance the text information.
Wavelet decomposition and gradient sub-bands are used to enhance text
information in gray scale. Next, Pyramid Histogram of Oriented Gradient (PHOG)
feature has been extracted from gray image and binary images for date-spotting
framework. Binary and gray image features are combined by MLP based Tandem
approach. Finally, to boost the performance further, a shape coding based
scheme is used to combine the similar shape characters in same class during
word spotting. For our experiment, three different date models have been
constructed to search similar date information having numeric dates that
contains numeral values and punctuations and semi-numeric that contains dates
with numerals along with months in scene/video text. We have tested our system
on 1648 text lines and the results show the effectiveness of our proposed date
spotting approach.
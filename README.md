# FaceProject

---
Lines2Face project page: https://liyuhangustc.github.io/Lines2Face/

To write a readme file using Markdown in github, see: [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet) or [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).

Github Markdown is not able to automatically  generate table of content with `[toc]`. Use [this tool](https://ecotrust-canada.github.io/markdown-toc/) instead.

---
## Recommended readings 2019-12-12 by tennyson
### paper list
* MarioNETte: Few-shot Face Reenactment Preserving Identity of Unseen Targets.[paper](https://arxiv.org/abs/1911.08139)
* How far are we from solving the 2D & 3D Face Alignment problem. [paper](https://arxiv.org/abs/1703.07332)
### relative materials
* Frequently-used normalization methods: BN, LN, IN and GN.[zhihu](https://zhuanlan.zhihu.com/p/72589565)

## Meeting Note 2019-11-29
### paper list
* Semantic Component Decomposition for Face Attribute Manipulation.[paper](http://jiaya.me/papers/faceattri_cvpr19.pdf)
* R3 Adversarial Network for Cross Model Face Recognition. [paper](http://openaccess.thecvf.com/content_CVPR_2019/papers/Chen_R3_Adversarial_Network_for_Cross_Model_Face_Recognition_CVPR_2019_paper.pdf)
* SinGAN: Learning a Generative Model from a Single Natural Image.[paper](https://arxiv.org/pdf/1905.01164.pdf)

## Meeting Note 2019-11-8
### Work Assignment
* Binxin Yang: investigate papers on domain adaptation
* Zihan Chen: more sketch drawings
* Zhihua Cheng: investigate papers on few-shot learning

## Meeting Note 2019-11-4
### Discussion
* Few sketches and many edge maps
* Domain gap between sketches and edge maps: the gap is larger than that between different classes of natural images, but smaller than that between different style images.
* Combining **domain transfer** and **few-shot learning**
### Work Assignment
* Binxin Yang: paper reading on graph convolution on 11-5 afternoon
* Zihan Chen: more sketch drawings
* Zhihua Cheng: investigate papers on transfer learning

## Meeting Note 2019-10-9
### Discussion
* Task: sketch to photo genertation 
* Challenges: 1) dataset collection, 2) geometric unalignment, and 3) few shot learning/domain transfering
### Work Assignment
* Binxin Yang: QT interactive tool
* Zihan Chen: sketch drawings
* Zhihua Cheng: sketch dataset/paper collection
### Paper List
* **CariGANs** CariGANs: Unpaired Photo-to-Caricature Translation.[Project](https://cari-gan.github.io/)
* **FUNIT** Few-Shot Unsupervised Image-to-Image Translation. [Project](https://nvlabs.github.io/FUNIT/)
* **MaskGAN** MaskGAN: Towards Diverse and Interactive Facial Image Manipulation. [Paper](https://arxiv.org/pdf/1907.11922.pdf)

## Meeting Note 2019-9-24
### Discussion
##### Image generation from attribute values
* Image generation from attribute values (instead of attribute labels)
##### Image generation by mixing two images
* Weights of two input images
* Two potential methods based on two architectures: conditional and unconditional
* Artbreeder.com
##### Image generation from sketches progressively
* Image generation progressively from sketches (stroke by stroke, instead of entire well-drawn sketches)
### Future work
* Mask-face dataset survey
* Face2mask, face parsing survey
* Mask2Face generation by pix2pixHD
* Mask editing interface
* Image generation by mixing images survey

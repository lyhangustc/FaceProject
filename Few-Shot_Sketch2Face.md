# Summary
## Hand-drawn dataset
### Hand-drawn sketch
The hand-drawn sketches are obtained by people with trained drawing skills. They display a 
* Lines are smooth, due to being drawn by drawing board
* Paired with real face images
* Complete face structures
* Different levels of details
* ~50 sketches only ¨C few-shot

![hand-drawn sketch](/figures/datasets/handdrawn_sketch_groundtruth.png)

### Hand-drawn contour
* Lines are not so smooth
* Deformed/twisted/unreal shape of faces
* Only contains connecting lines of landmarks, no hairs, ears, glasses, makeup or necks.
* No paired real face images 
* ~200 collected

![hand-drawn contour](/figures/datasets/handdrawn_contour.png)

## Challenges
### 1. Data domain sift
There exists a domain gap between the hand-drawn data and the edge maps/contours. If we train the model with edge maps/contours, and then test the model with hand-drawn sketches/hand-drawn contours, artifacts can be found in the outputs. Three kinds of artifacts are summarized as below.
1. Hair artifact

![Hair artifact](/figures/CSA-GAN_edge_df2photo/hair_artifacts.PNG "Hair artifact")

1. Ornament artifact

![Ornament artifact](/figures/CSA-GAN_edge_df2photo/ornamenet_artifacts.png "Ornament  artifact")

1. Texture artifact

![Texture artifact](/figures/CSA-GAN_edge_df2photo/texture_artifacts.png "Texture artifact")

### 2. Few-shot
The number of the collected hand-drawn sketches/hand-drawn contour is not large enough to train a large-scale model. The model is supposed to use the hand-drawn data in a few-shot form.
#### Basic idea:
* Embedder: outputs style-invariant embedding
* Style: line styles of different kinds of sketches (hand-drawn sketches, edge maps, contours)
* Style-invariant embedding is acquired by averaging embeddings of sketch patches which are cropped from input sketch.

#### Architecture
##### Few-shot hand-drawn face sketches to realistic face images synthesis
* Similar to few-shot face switch model (e.g. talking head model)
* Contour2photo with guidance of K(=1, 3, 5, 8) ID face images.
* Embedder: ID images to ID-specific embedding (with only shape/pose/position information)

![Talking head model](/figures/architecture/talking_head_model.png "Talking head model")
 
##### Current architecture
* Generator

![Few-shot generator](/figures/architecture/few-shot_generator.png "Talking head model")

* Discriminator and loss: same as CSA-GAN, e.g. four-scale discriminator, L_adv + L_l1 + L_fm

* AdaIN Residual Block

![AdaIN Residual Block](/figures/architecture/adain_res_block.png "AdaIN Residual Block")

 
 

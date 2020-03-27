# 3-27 Weekly Report
## Few-shot sketch2face model
### 1. All-zero problem (solved, [3-21](#3-21), [3-22](#3-22))
* The outputs of the model are all zeros, the losses are all zeros
* NaN gradient in decoder: detect NaN gradients in one of decoder layers
- [x] The newly implement of SN meets a bug of uninitialized variables.
- [x] Use the old version of SN to solve this problem.

### 2. Out of GPU memory (solved, [3-25](#3-25))
* Caused continuously added to the graph while iterating
- [x] Solved by calling tf.get_default_graph().finalize() before iterating

## Embedding projector (not done, [3-21](#3-21), [3-26](#3-26))
* Code debugging is done
* The loading takes too long (~5 min) to start for unknown reason (as comparision, ~30 sec to start training).
- [ ] Not sure the inputs for the embeddings.
- [ ] Not tested in Pytorch code.

## CelebAMask-HQ dataset ([3-26](#3-26))
- [ ] Train pix2pixHD with mask_edge2face

## Result collection
* `~/results`
- [ ] Online displaying

## Paper Reading 
### [Which Training Methods for GANs do actually Converge?](#which-training-methods-for-gans-do-actually-converge)
### [Selfie2Anime](#3-24)

# 3-26
## Embedding projector of Tensorboard
##### Mnist data can be displayed by the project, but the embeddings of our generator is not able to be displayed.
* The other dimension rather than the first one (batch_size) should be flattened, e.g. shape=[N, HxWxC].
* The N and HxWxC should be large than 3 in order to compute PCA/t-SNE, 
## CelebAMask-HQ
* [Github](https://github.com/switchablenorms/CelebAMask-HQ)
* 30000 face images from CelebA-HQ
* Example
![CelebAMask-HQ Example](/figures/daily_report/3-26/CelebAMask-HQ_example.PNG)


# 3-25
## Debug out of GPU memory
* The GPU memory is full after running 499 steps
* 99% of the time, when using tensorflow, "memory leaks" are actually due to operations that are continuously added to the graph while iterating — instead of building the graph first, then using it in a loop. 
* Call tf.get_default_graph().finalize() before your loop and look for any error it may throw.
[StackOverThrow](https://stackoverflow.com/questions/51175837/tensorflow-runs-out-of-memory-while-computing-how-to-find-memory-leaks)


# 3-24
## Paper Reading
### Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation
Junho Kim (NCSOFT), Minjae Kim (NCSOFT), Hyeonwoo Kang (NCSOFT), Kwanghee Lee (Boeing Korea)
[ArXiv](https://arxiv.org/abs/1907.10830) [code](https://github.com/taki0112/UGATI)
* Unsupervised image-to-image translation
* Focus on geometric/shape changes, [selfie2anime dataset](https://drive.google.com/file/d/1xOWj1UVgp6NKMT3HbPhBbtq2A4EDkghF/view?usp=sharing)
* **Adaptive Layer-Instance Normalization**: sum of Adaptive IN and LN with trainable weights.
    * IN: more source semantic details from input in the output
    * LN: more target style in the output 
* Auxiliary classifiers (source/target) in both generator and discriminator 

## Web page
* [Selfie2Anime](https://selfie2anime.com) by [Nathan Glover](https://github.com/t04glovern)
* [Selfie2Waifu](https://waifu.lofiu.com) by [creke](https://github.com/creke)
* [Baidu AI Selfie2Anime](https://ai.baidu.com/tech/imageprocess/selfie_anime)

## Telegram Bot
* [Selfie2AnimeBot](https://t.me/selfie2animebot) by [Alex Spirin](https://github.com/sxela)
#### Code Reading
* Auxiliary classifier have two branch from global_avg_pooling and global_max_pooling
* Auxiliary classifier: x==>Global_avg/max_pooling==>fc*==>logit==>cat(avg, max), NHWC==>NC==>N1==>1==>2
* Attention map: x==>multiply(x, fc\*weight)==>cat(avg, max)==>conv==>reduce_sum, NHWC==>NHW1==>NHW2==>NHWC==>NHW1
* Adaptive Resiual blocks: use same channel so that the gamma/beta sizes are fixed ( NC instead of [NC_1, NC_2...]
* MLP: use a global pooling first to reduce the number of weights
* Kernel sizes of first annn

#### Architecture
<div align="center">
  <img src = '/figures/daily_report/3-24/generator_fix.png' width = '785px' height = '500px'>
</div>

---

<div align="center">
  <img src = '/figures/daily_report/3-24/discriminator_fix.png' width = '785px' height = '450px'>
</div>


## Results
### Ablation study
<div align="center">
  <img src = '/figures/daily_report/3-24/ablation.png' width = '438px' height = '346px'>
</div>

### User study
<div align="center">
  <img src = '/figures/daily_report/3-24/user_study.png' width = '738px' height = '187px'>
</div>

### Kernel Inception Distance (KID)
<div align="center">
  <img src = '/figures/daily_report/3-24/kid_fix2.png' width = '750px' height = '400px'>
</div>


# 3-23
### Github
* Setup github environment
* Write a summary report of the project: `~/Few-Shot_Sketch2Face.md`
* Collect experimental results and make web files for displaying: `~/results`

# 3-22	
### All-zero problem 
####	Solution plan 1: training few-shot model with random style embedding vector
*	Code with random style vector done, all-zeros problem not occurred (Figure 1), but
*	GPU out of memory at 499th  step
*	The model size is fixed, and GPU memory is enough for training
*	Memory leak after 499 steps? Not solved
*	Remove model-saving part, not solved
*	Switch generator back to CSA-GAN generator, out of memory in 412th step
*	Compared to CSA-GAN code, new discriminator/loss/train_op implementation. Which part raise the memory leak???? Not solved.
*	Code with zeros style vector, done, all-zeros problem not occurred (Figure 2)
####	Solution plan 2: another architecture for style embedder network
*	Conv x5 + fc => Downsample + fc, still all-zero problem
*	Conv x5 + fc => Downsample + 1x1 Conv
#### Solution plan 3: visualize histograms of trainable variables
*	Code done
*	NaN in gradients of decoder, reasons to be checked searched by Bing:
- [ ]	Model overfitting leads to loss=0, decrease the size of model, working, see above
- [ ]	Use add_check_numerics to tf.RunOption()
- [x]	Use tf.kera.callbacks.Tensorborad instead of tf.summary.histogram
- [x]	Use ReLU/tanh instead of sigmoid, done, not solved
- [x]	Compute gan loss by digit before activation, done, not solved
####	Conclusions on all-zero problem so far
* 	Unknown mistakes in style embedder => NaN gradients => Output all zeros
####	Model:
- [ ]	Add K1 loss 
- [x]	Add L2 regularization to model, not compared
- [x]	Use hinge loss as basic gan loss and discriminator loss, not compared
### Paper Reading
##### Which Training Methods for GANs do actually Converge?
ICML 2018
##### Conclusion
*	WGAN and WGAN-GP and DRAGAN do not ensure local convergence of GAN. 
*	Use Gradient penalty on real data (L2 regularization, R1) and fake data (L2 regularization, R1).
*	 R1 <=> R2 <=> R1+R2 in stabilizing GAN training. 

![Local Convegence](/figures/daily_report/3-22/image003.jpg "Local Convegence")

![Optimization](/figures/daily_report/3-22/image004.jpg "Optimization")

### [Different Losses of GANs](https://github.com/TwistedW/tf-GANs-Loss)

![Different Losses of GANs](/figures/daily_report/3-22/image005.jpg "Local Convegence")
![Different Losses of GANs](/figures/daily_report/3-22/image006.jpg "Local Convegence")




# 3-21
### Task 1: debug on few-shot sketch2face model
##### All-zero problem
* the outputs of the model are all zeros, the losses are all zeros
* NaN gradient in decoder: detect NaN gradients in one of decoder layers
##### Task 2: visualize the embeddings of CSA-GAN
* Using Tensorboard projector
### Working log
##### Visualize embeddings (Task 2)
- [x] A mnist visualization example (mnist_embedding.py, figure)
- [ ] Add embedding projector to CSA-GAN
##### Visualize histograms by Tensorboard (Task 1)
* Visualize histograms of trainable variables and gradients
* CSA-GAN 
##### Few-shot model with random style code 
* Few-shot model with random style code (Task 1)
* Use randomly sampled vector as style code to avoid the all-zero problem (training)
* GPU out of memory when saving model for unknown reason (hacked by not saving model)

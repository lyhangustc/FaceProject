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

![Local Convegence](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

![Optimization](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")



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

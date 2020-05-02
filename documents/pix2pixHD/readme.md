# Version log
  * local_version0: Using local enhancer and global generator,instance_norm, data augmentation using contour translation and rotation.
  * local_version1: Using local enhancer and global generator,batch_norm, data augmentation using contour translation and rotation.
  * local_version2: Using local enhancer and global generator,use SLRN to replace the norm of downsample, data augmentation using contour translation and rotation.
  * global_version0: Using global generator only,instance_norm, data augmentation using contour translation and rotation, remove the first two instance norm.
  * global_version1: Using global generator only, instance_norm, data augmentation using contour and gt translation and rotation, remove the first two instance norm.
  * global_version2: Using standard global generator, instance_norm, data augmentation using contour translation and rotation.
  * global_version3: Using global generator, use SLRN to replace the norm of downsample, data augmentation using contour translation and rotation.
  * global_version4: celebAHQ-mask 1width as input, Using global generator, use SLRN to replace the norm of downsample, data augmentation using contour translation and rotation.
  * global_version5: celebAHQ-mask 2width as input, Using global generator, use SLRN to replace the norm of downsample, data augmentation using contour translation and rotation.
  * global_version6: celebAHQ-mask 2width as input, Using global generator, baseline.

### Model
* pix2pixHD with global generator (without local enhancer)
* Add SAP
* Add generator feature matching loss
### Data
* 512x512
* sketch: mask edge
* deform sketch
  * x10: each sketch randomly generate 10 deformed sketches
  * deform radius: 11
  * deform probability: 0.5
* Augmentation
  * rotation: -10~10 degree
  * translation: -20~20 pixel

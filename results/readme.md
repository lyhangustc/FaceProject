This directory is arranged as:
```
--model
	--training_data
		--test_data
			--index.html
			--result_image_folder
		--test_data_1
			--index.html
			--result_image_folder
```
The web file ```~/results/model/training_data/test_data/index.html``` shows the results from **model** trained with **training_data** and tested with **test_data**. 

For example, results from model pix2pixHD trained with contour2photo dataset and tested with hand-drawn contours is placed in ```~/results/pix2pixHD/contour2photo/handdrawn_contour/index.html```

The index.html files are generated by python scripts. An example python script is shown in ```~/results/display.py```.

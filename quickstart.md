# Quickstart Commands

## Prerequisites
1. Follow the "Installation Instruction" in the [README.md](README.md), make sure you skip step 3 and 5
2. Make sure your `data` folder is one level above this repository (aka ../data/). This is where the competition datasets will be
   1. See my directory structure below


## Downloading weights
1. http://118.189.199.196:219/nextcloud/index.php/apps/files/?dir=/TIL2020&fileid=582393
2. Password: testtest69
3. Note that the unconverted models (weights basically) should be around 240mb

## Converting weights to model
1. Create a `saved_models/` folder
2. Store the weights I have uploaded in `snapshots/` (create if not there)
3. Run the code (edit the names appropriately)

`python keras_retinanet/bin/convert_model.py snapshots/resnet50_csv_01.h5 saved_models/test.h5 `


## Evaluating model
1. If you followed the file structure from above, you should be able to run evaluate like this
2. `python keras_retinanet/bin/evaluate.py csv val_annot.csv test_class.csv saved_models/test.h5`

## Sample Directory Structure
```
.
├── data (contains train/train/ and val/val/)
├── keras-retinanet
└── Your other repos/stuff
```
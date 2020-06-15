# Quickstart Commands

- [Quickstart Commands](#quickstart-commands)
  - [Prerequisites](#prerequisites)
  - [Downloading weights](#downloading-weights)
  - [Converting weights to model](#converting-weights-to-model)
  - [Evaluating model](#evaluating-model)
  - [Training model](#training-model)
  - [Sample Directory Structure](#sample-directory-structure)

## Prerequisites
1. Follow the "Installation Instruction" in the [README.md](README.md), make sure you skip step 3 and 5
2. Make sure your `data` folder is one level above this repository (aka ../data/). This is where the competition datasets will be
   1. See my directory structure below
3. run `pipenv install` to pull packages or if you are inside condas env `pip install -r requirements.txt`


## Downloading weights
1. Go here http://118.189.199.196:219/nextcloud/index.php/s/a99bnswn73rWQ4B
2. Password: testtest69
3. Note that the unconverted models (weights basically) should be around 240mb

## Converting weights to model
1. Create a `saved_models/` folder
2. Store the weights I have uploaded in `snapshots/` (create if not there)
3. Run the code (edit the names appropriately) in `pipenv shell`

`python keras_retinanet/bin/convert_model.py snapshots/resnet50_csv_01.h5 saved_models/test.h5 `


## Evaluating model
1. If you followed the file structure from above, you should be able to run evaluate like this in `pipenv shell`
2. `python keras_retinanet/bin/evaluate.py csv val_annot.csv class.csv saved_models/test.h5`


## Training model
1. Make sure your most recent snapshot **weight**(not converted model) is saved in `snapshots/`. Im assuming the snapshot used is on epoch 6 here.
2. Find GPU ID with `nvidia-smi`. Im assuming 2
3. Run `python keras_retinanet/bin/train.py --snapshot snapshots/resnet50_csv_06.h5 --batch-size 2 --steps 6100 --gpu 2 --initial-epoch 7 csv test_annot.csv class.csv`
4. Monitor GPU usage (if using) to ensure everything is running correctly.


## Sample Directory Structure
```
.
├── data (contains train/train/ and val/val/)
├── keras-retinanet
└── Your other repos/stuff
```
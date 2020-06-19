# Quickstart Commands

- [Quickstart Commands](#quickstart-commands)
  - [Prerequisites](#prerequisites)
  - [Downloading weights](#downloading-weights)
  - [Converting weights to model](#converting-weights-to-model)
  - [Evaluating model](#evaluating-model)
  - [Training model](#training-model)
    - [Optimizing AWS GPU settings](#optimizing-aws-gpu-settings)
  - [New model training plan](#new-model-training-plan)
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

`python keras_retinanet/bin/convert_model.py --backbone=resnet101 --config config.ini snapshots/resnet50_csv_01.h5 saved_models/test.h5 `


## Evaluating model
1. If you followed the file structure from above, you should be able to run evaluate like this in `pipenv shell`
2. `python keras_retinanet/bin/evaluate.py --backbone=resnet101 csv val_annot.csv class.csv saved_models/test.h5`


## Training model
1. If using AWS, refer to section below on optimizing performance
2. Go into condas environment
3. Make sure your most recent snapshot **weight**(not converted model) is saved in `snapshots/`. Im assuming the snapshot used is on epoch 6 here.
4. Find GPU ID with `nvidia-smi`. Im assuming 2
5. (EXAMPLE) Run `python keras_retinanet/bin/train.py --snapshot snapshots/resnet50_csv_06.h5 --config config.ini --steps 13317 --initial-epoch 6 --no-evaluation csv test_annot.csv class.csv`
6. Monitor GPU usage (if using) to ensure everything is running correctly.

### Optimizing AWS GPU settings
1. Follow this guide https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize_gpu.html
2. Run all this outside condas environment
3. `sudo nvidia-persistenced`
4. For P3 (Tesla V100) `sudo nvidia-smi -ac 877,1530` to set GPU clockspeed to maximum.


## New model training plan
- ResNet101
- Freeze Backbone
- 10 Epochs
- Customized anchors
`python keras_retinanet/bin/train.py --backbone=resnet101 --config config.ini --steps 6658 --batch-size 2 --epochs 10 --freeze-backbone --compute-val-loss csv test_annot.csv class.csv`

## Sample Directory Structure
```
.
├── data (contains train/train/ and val/val/)
├── keras-retinanet
└── Your other repos/stuff
```


## Docker

1. Run `apt-get install -y libsm6 libxext6 libxrender-dev libxext-dev && pip install -r requirements.txt`
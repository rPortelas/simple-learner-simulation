
Simple Toy environment for teacher algorithms
==================================


## Installation
Git clone the repo and:
```
cd simple-learner-simulation/
conda create --name learnersim python=3.6
conda activate learnersim
pip install -e .
```

## Launching experiments on the toy env (example is with ALP-GMM teacher)
```
python3 toy_run.py --seed 42 --exp_name test_full_toy_env -v2 --teacher ALP-GMM -rnd 10 -rsc
```

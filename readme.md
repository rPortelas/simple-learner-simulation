
Meta Automatic Curriculum Learning
==================================


## Installation

1- Unzip and install codebase with Python >= 3.6, using Conda for example 
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

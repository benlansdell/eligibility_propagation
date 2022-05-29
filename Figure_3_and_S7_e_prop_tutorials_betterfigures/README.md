## Installation guide

We recommend using a conda installation with python 3.6 and tensorflow 1.15 for this simulation.

```
conda create --name eprop-figure3 python==3.6.2
conda activate eprop-figure3
conda install --file requirements.txt
python tutorial_evidence_accumulation_with_alif.py
```


## Tutorials on eligibility propagation (e-prop)

In the first tutorial  `tutorial_pattern_generation.py`, one trains a recurrent network (RNN) of Leaky Integrate and
Fire (LIF) neurons using the eligibility propagation (e-prop) algorithm on a pattern generation task.
This task does not require working memory.

In the second tutorial `tutorial_evidence_accumulation_with_alif.py` the task requires to remember over a long delay,
hence we equiped the neuron model with an adaptive threshold with a longer time constant. The eligibility traces that
result in e-prop with this adaptive neuron model are richer.

In both tutorial e-prop is implemented in two ways, either the eligiblity traces and learning signals are hard coded,
or the auto-differentiation of tensorflow is tweacked to be mathematically equivalent to e-prop.
To verify this equivalence we made sure to check that the two loss gradients are equal (see `numerical_verification_).
The figure below was obtained by running:  
```tutorial_evidence_accumulation_with_alif.py -feedback random -eprop -eprop_impl hardcoded -n_batch 32```  

When running the hardcoded implementation of e-prop on a GPU and encountering an OOM error, it is recommended to reduce the batch size to 16 or 8. The early stopping criterion should be reached after around 200 - 500 iterations. This code is written and tested with tensorflow 1.12.0, numpy 1.17.3 and python 3.6.9. 

<img src="./figures/evidence_acc_training.png"
     alt="Raster plot"
     style="width: 200;" />

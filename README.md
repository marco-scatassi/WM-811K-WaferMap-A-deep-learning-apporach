# WM-811K-WaferMap-A-deep-learning-apporach

Beeing able to identify specific class defects in product, such as wafermap, can help in understand what's wrong in the production chain. So that it became possible
to take necessary actions faster and in a targeted manner. In this repo, you can find the step followed by me togheter with my colleagues **Greta Gravina** and **Niccolò Puccinelli** in order to developed a simple CNN to face the problem previously descripted. In particular, the problem consists in identify the type of defect of wafermaps among 9:

<p align="center"> Center - Donut - Edge-Loc - Edge-Ring - Loc - Near-full - Random - Scratch - none </p>

Due to the **extreme imbalance of the dataset**, both among failure classes and between the non failure class (none) and the failure classes, we have focused on the **generation of synthetic data** that together with classical augmentation techniques have lead in improve model performance. In particular, the final model shows more uniform performance across classes than the initial one as well as a greater mean percentual of correct classified images.


|           | Initial Model | Final Model | Difference in  performance |
|-----------|:-------------:|:-----------:|:--------------------------:|
| Center    |     88.61%    |    89.65%   |            1.04%           |
| Donut     |     79.78%    |    86.52%   |            6.74%           |
| Edge-Loc  |     66.46%    |    87.00%   |           20.54%           |
| Edge-Ring |     97.93%    |    96.64%   |           -1.29%           |
| Loc       |     66.61%    |    64.72%   |           -1.89%           |
| Near-full |     79.17%    |    91.67%   |            12.5%           |
| Random    |     84.78%    |    90.58%   |            5.8%            |
| Scratch   |     29.03%    |    67.57%   |           38.54%           |
| None      |     99.33%    |    98.8%    |            -0.5%           |
| Mean      |     76.86%    |    85.9%    |            9.04            |

More details can be found in the *Presentation slides.pdf* file. 

In addition, following this link https://marco-scatassi-wm-811k-wafermap-a-deep-lear-model-deploy-vy0bqn.streamlit.app/ it's possible to play a little with one of the tested models in order to see how it works. I hope you will enjoy it 😄.

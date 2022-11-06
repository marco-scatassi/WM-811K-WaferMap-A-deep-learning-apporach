# WM-811K-WaferMap-A-deep-learning-apporach

Beeing able to identify specific class defects in product, such as wafermap, can help in understand what's wrong in the production chain. So that it became possible
to take necessary actions faster and in a targeted manner. In this repo, you can find the step followed by me togheter with my colleagues **Greta Gravina** and **Niccolò Puccinelli** in order to developed a simple CNN to face the problem previously descripted. In particular, the problem consists in identify the type of defect of a specific wafermap among 9:

Center - Donut - Edge-Loc - Edge-Ring - Loc - Near-full - Random - Scratch - none

Selecting a type of failure will show you 10 images associated with that specific defect. Clicking the button under a certain image you can see the class predicted for that image by the model and the probability of belonging to each class (i.e. the output of the model).

===============
Bias correction
===============

We've temporarily retired our bias correction algorithm (KDDM) because it came with heavy dependencies that complicated
installation and deployment. We're currently working on implementing bias correction algorithms to  `xclim`, which will
then be offered as a WPS service in the platform sometimes this fall.

..
    Climate models are simplified representations of complex real world processes. An obvious example of this simplification
    is representation of the landscape as an array of flat grid cells of uniform altitude, temperature, humidity,
    snow depth, etc, even though we know full well that there are variations within each grid cell. These simplifications
    have consequences on the realism of model simulations. Models might not represent correctly, or at all, important climate
    phenomena such as the El-Nino/La Nina episodes, the rapid melt of Arctic sea ice with raising air temperature or the breakup
    of Antartica's ice sheets. Another consequence is that when comparing observed climate conditions with their
    corresponding simulated variables, systematic differences appear. One model might overestimate tropical night-time temperature,
    while another might underestimate monsoon precipitation over East Asia.

    These systematic biases usually have to be corrected before using future climate simulations to assess the impacts of
    climate change. Indeed, if one wants to model crop productivity around 2050 with a model that is systematically too dry
    over the historical period, future projections likely won't make sense. So-called *bias correction* methods are used to
    post-process climate simulations such that their statistics over the historical period match those of observations. The
    hypothesis is that the bias over the future period is likely the same as the bias over the historical period. This is a
    fairly strong hypothesis that has been shown to be false [], but until someone finds a better approach, it's the best we
    can do.

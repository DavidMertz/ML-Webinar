
# Machine Learning with scikit-learn

## Overall Introduction: Welcome to Machine Learning with scikit-learn

Welcome to this Safari webinar, "Machine Learning with scikit-learn."  Over the next six hours and nine lessons we introduce the main concepts and techniques used in modern machine learning and look at numerous examples written in scikit-learn.

My name is David Mertz, and I’ve been involved with the Python community for 20 years, with Data Science under various previous names, and with Machine Learning since way back when it was more likely to be called "Artificial Intelligence."  I was a director of the Python Software Foundation for six years, and continue to serve on, or chair, a variety of PSF working groups.

I have also written quite a bit about Python: the column _Charming Python_ for IBM developerWorks, for many years; the Addison-Wesley book _Text Procesing in Python_; two short books for O’Reilly.  I created the data science training program for Anaconda Inc. and was a senior trainer for them.

A few years ago, I worked for 8 years with the folks at D. E. Shaw Research.  They have built the world's fastest, highly-specialized—down to the ASICs and network layer—supercomputer for performing molecular dynamics. I am pleased to find Python has become the default high-level language for most scientific computing projects.

Nowadays, I run a training business called "KDM Training" with some amazing and accomplished colleagues. We deliver hands-on training for Data Science and Scientific Python.  We would love to hear from you, and would especially love your business for our live, on-site trainings.  Our email is `info@kdm.training` and our website is `http://kdm.training`.

--

The Scikit-learn library provides a large range of algorithms in machine learning that are unified under a common and intuitive Python API. Most of the dozens of classes provided for various kinds of models share the large majority of the same calling interface. Very often—as we will see in examples below—you can easily substitute one algorithm for another with nearly no change in your underlying code. This allows you to explore the problem space quickly, and often arrive at an optimal, or at least satisficing approach to your problem domain or datasets.

Scikit-learn is built on the foundations of the Numeric Python stack.  It uses NumPy for its fundamental data structures and optimized performance.  It plays well with Pandas and matplotlib.  It is Free Software under a BSD license.  The great bulk of machine learning programming in Python is done with scikit-learn—at least outside the specialized domain of "deep neural networks" which we will discuss briefly in the first lesson.

--

In order to get best advantage from this course, you should do a few things to prepare, or already be familiar with things mentioned.  A good basic knowledge of Python is important.  A few intuitions about statistics and linear algebra are useful, but we will not explore mathematical details underlying algorithms in any great length.  Scikit-learn packages many of the numeric niceties for you, and implements algorithms in efficient ways.

The examples we go through in this course often utilize Pandas DataFrames as containers to store data sets.  Therefore, it will be easier for you to follow this course if you have a working knowlege of Pandas.  However, we will not use particular arcane techniques in that large library; you should be able to follow even if you do not already use Pandas.  Similarly, we will occasionally visualize results using matplotlib and a few other libraries; you will not need to learn those APIs to follow this course, but also do not be surprised to see a few of those APIs used.

The course content itself is presented using Jupyter notebooks.  These are available to download from https://github.com/DavidMertz/ML-Webinar.  If you have not used Jupyter notebooks, it is worthwhile to spend a half-hour on an introductory tutorial before working through the material in this course.  All of the content present in this video will closely match that available at the GitHub repository; the repository may be updated or tweaked by the time you watch this.  The notebook and other resources associate with this course are licensed as Attribution-NonCommercial-ShareAlike 4.0 International; this video itself is made available only for registrants at Safari, and is not redistributable.

Beyond downloading the content of the GitHub repository, you should setup a suitable environment for running the Jupyter notebooks.  The repository contains a file `environment.yml` for creating an environment using the `conda` package manager and a file `requirements.txt` for creating an environment under the `pip` package manager.  Please use one of these to install a suitable environment, then launch the material using `jupyter notebook Outline.ipynb` at the command line.

--

I hope you will enjoy and learn a great deal from the next several hours of training.  Please feel free to pause the video wherever it is convenient, and play around with techniques, concepts, and code presented within the interactive Jupyter notebooks.  I hope your personally customized version of these notebooks will be a valuable resource for you to return to later.

In the the notebooks that you downloaded, a variety of exercises will be available for you to practice working with the APIs and techniques discussed in this course.  As you go through the material on your own, I encourage you to pause the video to try these exercises and/or to return to the notebooks after you have finished watching.


## Lesson 1: What is Machine Learning?

Welcome to lesson one.  In this first lesson we address many essential concepts in machine learning; little in this lesson is specific to Python or scikit-learn, and almost all of it will apply equally if you happen to use a different library or programming language.

After a brief detour into talking about deep learning and why it is—although fascinating—not the focus of this particular course, we will see the main concepts you need to understand for machine learning.  You will learn about the main types of tasks that can be accomplished with ML.  We will then look at issues of dimensionality, of feature engineering and selection, of feature/variable types, and explore a few of the techniques and concepts that make it practical to work with machine learning libraries and systems.

At the end of this lesson you will have a broad understanding of all the main concepts used in machine learning.

## Lesson 2: Exploring a data set

Welcome to lesson two.  In this lesson we prepare a dataset for machine learning models.  In the real world, data always arrives messy and flawed.  Before you can get to applying machine learning techniques, it is almost always necessary to massage, and filter, and generally clean up your data.

Much of what you will probably do in exploration and cleaning of datasets will utilize Pandas, which is a rich library for exactly those tasks.  This lesson will do most of its work using that tool.  Pandas is not a per se requirement for scikit-learn, but they play very well together.

At the end of this lesson, you will have an initial idea of how to get a "feel" for your data and be able to think about likely problems and anamolies within novel datasets.  After many years of practice as a working data scientist, you will be highly skilled at these same judgements.

## Lesson 3: Classification

Welcome to lesson three.  One of the main techniques you will use within machine learning—specifically wihtin what we call *supervised* machine learning is Classification.  As we discussed in lesson one, classification is trying to match a collection of multiple features to a *categorical* target.  That is, we know that the prediction we are hoping to make is that a newly observed item belongs to one of N known classes.

There are many algorithms for performing classification, a large number of them are available in scikit-learn.  We will look at a number of different classifiers in this lesson, and compare some features of each of them.  This lesson will give you a first exposure to the scikit-learn APIs, which are mostly similar across its numerous classes, both for classifiers and for other models and transformations.

At the end of this lesson you will have a sense of the range of classifiers available and some context to choose among them in your own datasets and goals.

## Lesson 4: Regression

Welcome to lesson four.  Within supervised machine learning, the two basic types of models are classifiers and regressors.  Both have precedent in standard statistics, but machine learning techniques go beyond the "closed form" mathematical techniques that precede them.  We will look at a number of regressors in this lesson, starting from the linear regression family that is common in general statistics.

This lesson also introduces some of the sample data sets that are bundled with scikit-learn and that can often be a useful starting point for exploring techniques and coding styles.

By the end of this lesson, you will have an overview of most of the regression models available in scikit-learn.

## Lesson 5: Clustering

Welcome to lesson five.  As well as supervised learning—i.e. classification and regression—that we have looked at in prior lessons—there are various models of *unsupervised* learning as well.  When we do not have any *a priori* about what the *target* of an algorithm is, an approach we can still take is to look at how complex multi-dimensional features *cluster* into distinct categories.  This is very common to find in datasets.

This lesson overviews a number of clustering algorithms and uses them to create synthetic classifications of several datasets.  It will give you some hands on experience with the minor API differences scikit-learn uses to work in an unsupervised rather than supervised domain.  For clustering, it is especially useful to try to visualize or explore the classifications produced by models since they do not necessarily have obvious names for the classes; we explore such visualization in this lesson.

## Lesson 6: Hyperparameters

Welcome to lesson six.  Most of the models in scikit-learn—or indeed, in any other machine learning library—utilize what are called "hyperparameters" in the domain.  We introduced this concept in lesson one, but have not explored it in more depth yet.

When a model is trained, it gains configuration data, often called "parameters."  These are the data that define what it means for a model to be trained on one dataset versus another, and are attached to the model object.  However, almost all algorithms in machine learning also utilize hyperparameters to control exactly what variation of the basic algorithm is used, or cut-offs assumed, constants that are utilized in underlying formulae, or other algorithmic variations.  These hyperparameters are usually used in creating model instances, and before any actual training is performed.  In many cases, their values can dramatically change the effectiveness and success of a model.

It is often, even usually, difficult to judge in advance what the best choice of hyperparameters is.  Therefore, performing what is called a "grid search" over the parametric space of hyperparameters is often desirable.  Scikit-learn contains wrapper classes that both emulate the APIs of underlying models and provide easy access to the basic operation of a grid search.

## Lesson 7: Feature engineering and feature selection

Welcome to lesson seven.  In prior lessons, we mostly looked at choosing and training models using relatively naive feature sets drawn from the underying datasets.  However, when you need to work on problems with real world complexity, often the features you are initially provided by a dataset are not powerful enough to achieve the model effectiveness you need.

Of course, some data simply does not contain the necessary intrinsic force.  But most of the time, it rather requires extra work to tease out the "features of the features" that are actually most useful for your purposes.  These initial steps are called "feature engineering" and "feature selection."  The former involve constructing synthetic features based on the raw features you are given, by various combinations of scaling them, combining them, handling outliers, or transforming the representation of features.  The latter, feature selection, involves reducing the number of features you utilize, often subsequent to multiplying that number in feature engineering steps, to select only those that are most predictive.  Sometimes feature selection is needed simply to make training a model computationally tractable.

## Lesson 8: Pipelines

Welcome to lesson eight.  In prior lessons we have seen a variety of techniques for preparing and transforming data, and for selection of models and hyperparameters of models.  Very often when you have combined and refined these steps in a particular way relevant to your domain, you would like to be able to encapsulate those steps.

The scikit-learn abstraction and classes called "pipelines" allow this combination of steps while maintaining the same APIs that have now become familiar.  There are a variety of components that you can combine using pipelines, but producing a combined object that follows the same API as those components is a very useful programming style.

## Lesson 9: Robust Train/test splits 

Welcome to lesson nine.  In earlier lessons we utilized the simple `train_test_split()` function to divide data that was used in training models.  This function is perfectly suffient for exploratory purposes, but at a final stage when you are interested in more rigorous validation of models in preparation for production, you probably want to consider more robust train/test split strategies.

In this lesson, we look at the numerous classes provided by scikit-learn for robust train/test splits.

## Summary

Thank you for watching this course on "Machine Learning with scikit-learn." 

We have spent a number of hours together reviewing concepts in machine learning and usage details about scikit-learn.  This course was only the beginning of your learning path, but I hope it has been a good start.  After having watched this video, I encourage you to return to the notebooks presented to review them, and also to followup by completing all the exercises provided to accompany these notebooks.  After these hours and those working on exercises, I advice you next to spend months and years exploring the ins and outs of concrete machine learning problems; a good intuition about these issues takes both practice and dedication to learning.

The beginning of this course presented the broad concepts you will need to understand machine learning, even if you use a language other than Python or a library other than scikit learn.  From there, we had a chance to work with supervised learning problems, performing both classifications and regressions.  You saw discussion of dozens of models available in scikit-learn for supervised learning, and came to understand the methodology of train/test splits and valiation metrics. 

By the middle lesson, you had a chance to look also at unsupervised models, and should understand both when you will want to use them against future datasets and problems, and also what API differences you need to think about compared with supervised models.

The last one third, or so, of this course presented you with a variety of tools and facilities in scikit-learn for doing the concrete work of machine learning.  Using models is only part of it.  You learned the importance of choosing good hyperparameters and how you can go about determining them.  You learned to structure your reusable code into reproducible pipelines.  And finally, we looked at some intricacies of constructing more robust train/test splits for production ready models.

I hope very much hope this introduction provides you with the tools you need to become accomplished as a data scientist.  I welcome feedback from any students in this course, who can email me at mertz@gnosis.cx.  I will do my best to reply to everyone, both to improve the content herein and to engage with the wonderful professional community around machine learning in Python, and with scikit-learn.

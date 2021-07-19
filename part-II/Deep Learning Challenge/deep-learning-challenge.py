# DeepArmor Coding Challenge PT II: Deep Learning Edition
# Before you begin, a few notes regarding this challenge:
# You are not required to fully train a model. We are looking at code quality and understanding
# You may use the framework of your choice, however we recommend you use a subclassing, functional or other
# similar method for DAG construction over using the sequential/linear style
# We will not be considering model prediction accuracy in judging this challenge
# We will give consideration to models that incur unnecessary performance issues, but chasing optimization
# is not necessary

# CV task
# Our product owner has just gotten off the phone with a bakery chain. Due to an increased popularity
# in high quality apple varietals orders for two in vogue apple types for tarts, tartins, etc. have skyrocketed.
# Unfortunately, the grocery supplier which provide the apples mix Honey Crisp and Cosmic Crisp in together.
# You've been asked to create a proof of concept that will use images from the bakery's camera to determine
# which varietal of apples are in a box.

# You will find a folder containing a few images in the repo (.resources//apples/)
# Please use your preferred framework's dataloader, or write your own, with a preference for streamed data
# rather than in-memory

# Please demonstrate a few affine transformation additions to your model, you can do this in your dataloader
# it's own class or as a custom layer in your model. We'd like to see a rotation, a mirror and one
# transformation of your own choosing that you'd like to discuss with us as to a practical real world application
# (you should choose one you would like to discuss rather than one specific to this toy dataset)


# As it happens, the product owner only recalls one CV architecture; inception, because they really thought
# Tom Hardy was great in that film and the practical effects were something else. You've been asked to take
# inspiration from that model in the POC.
# Please construct a CNN model in your framework that demonstrates:
# input
# one inception block (please refer to the included diagram in ./resources if you are not familiar with it)
# (you may use a block from any version of inception, just include a diagram if you choose a different one)
# for ease, we recommend using a kernal size of 8 for all the layers
# a linear/dense layer of size 1, with softmax activation
# RMSprop as the optimizer, BinaryCrossEntropy as the loss (this is just so the model compiles)
# a learing rate scheduler, feel free to use 1e-3 as the learning rate and add reasonable looking numbers for the rest


# Please demonstrate a model fitting routine, either with a training loop or the API version
# Running for 1 epoch is fine just to show it works


# Please demonstrate a prediction of one of the images in the folder


# Please demonstrate saving and loading your model


# finally, please create a requirements.txt e.g. pip list --format freeze > requirements.txt

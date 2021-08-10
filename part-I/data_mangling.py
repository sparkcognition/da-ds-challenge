string_input = (
    "f15.0;f24.0;f37.;f650; f4.034387870891734; f57.864648;842709; f240.442@457330"
)

# our tokenizer written in EarSharp has had a bit of a malfunction. we had expected a nicely formatted list of floats
# separated by commas, but got the above output. our song lyrics sentiment analysis model cannot process them as-is
# luckily we were able to confirm that the values themselves are correct in the dataset but there were some unwanted
# insertions please create a script that takes the above input and breaks it into a numpy array of type double
# hint: every distinct value in string_input starts with the character f

# please enter your solution here:

# well, it turns out that in order to be ingested by our model we have to solve a few more problems with our data
# the zeroeth column is the label, please split that out into it's own array
# the next two columns have their orders swapped, please put them in the correct spots
# our model expects an array of dimensionality (1,6) due to a legacy code issue,
# please make the vector conform to the input dimension

# please enter your solution here:

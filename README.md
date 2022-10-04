# SignRecognitionSystem
Sign recognition for the Innopolis University course of "Practical Machine Learning and Deep Learning".  


Short desctiption of the project:
1) **Short description**: In our topic we want to implement signs recognition “on-fly”.
2) **Relevance**: This topic is quite relevant now since more and more cars drive themselves
and need an ability to read road signs to follow traffic rules.
3) **Input**: As an input we will use only one camera, since other data is hard to get and the
“usual” car does not contain any other sensors (while a lot of people are using
dashboard cameras).
4) **Data source**: For the simplicity of obtaining data, we will use some car driving simulator.
5) **Output**: As a result we want to be able to find road signs on the video (of course,
real-life, which makes it a bit harder since we should do the processing fast enough) and
to identify them.
6) **Real-life example**: Actually, this is quite a developed field, but we are still very
interested in researching and implementing the whole system by ourselves. More
information can be found on the Wikipedia:
https://en.wikipedia.org/wiki/Traffic-sign_recognition
7) **Additional information**: We are going to make the project more interesting by one more
requirement: it should work almost perfectly in any weather conditions and daytime.

## Dataset
For this task we want to have as realistic dataset, as possible. So, our team desided to generate our own dataset from real-life situations. Since we have 2-3 people, who own cars with dashboard cameras in them, we are going to ask them to share their recordings for following usage in the project.  
**More information about the dataset can be found in the "Dataset" folder, which contains it's own README.md.**

## Modern approaches.
1) **Computer vision only. _(outdated)_**  
One of the oldest approaches for solving this task. As for now, almost not used due to it's low speed, big error and complexity of implementation.
2) **Two-staged networks**  
Mainly used due to their accuracy. It can easily be more, than 99.5%, which is more than enough even for the fully-autonomous systems. But they have one problem - relatively slow work.
3) **One-staged networks**  
This type of networks works much faster, than the previous one, but they suffer a bit in the accuracy.  

More information about the last two approaches can be found in the following paper: [(PDF-file)](https://bit.ly/3rv0CRm)

## Approach, that we are going to use.
Due to the fact, that our main goal is to make just an "assistant" for our drivers, we can use **One-staged networks**, since very-high accuracy is not needed, while we would like to achieve high speed of work.

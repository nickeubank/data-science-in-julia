.. CS for DS documentation master file, created by
   sphinx-quickstart on Sat Jan 26 15:59:43 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Computer Science for Data Science!
=============================================

Computer science has much to offer the budding Data Scientist, but all too often computer science programs and texts just aren't designed with data science in mind. Computer science programs are full of useful concepts and topics, but they are often mixed in with lots of material that isn't relevant for non-academics or people not going into software development.

This resource is designed to provide an introduction to key computer science concepts of relevance to data scientists in an applied, efficient manner, including:

- **How computers think about numbers and text:** learn why 42.0 doesn't always equal 42.0.
- **Defensive Programming:** How to write code that minimizes the likelihood you'll make mistakes and maximizes the likelihood that when you do make mistakes, you'll be able to catch them.
- **Parallelization:** What is parallel computing, why is it becoming more and more important, and what are it's limitations
- **Big Data and The Memory Hierarchy:** Why working with big data requires categorically different strategies than smaller datasets.
- **Speed:** Why are some programming languages fast and others slow, how do I write code that runs quickly, and how to I evaluate the speed of my code?

In addition to these core computer science concepts, this site also provides a set of topics pages on data science tools like the command line, git and github, getting help on stack overflow and more that are often left out of introductory data science classes and texts that just teach a core program like Stata, R, Python, or Julia. These pages both explain the *purpose* of these tools and why they may be of use to you, as well as tutorials and links to outside resources for further learning.

This site is meant to be an *intermediate* data science resource. The world is full of "Intro to Data Science" texts, but it can be especially hard for people to take the next step of learning about all the tools and resources in the data science ecosystem and to develop a deeper understanding of how computers work to make troubleshooting easier and less scary. This site is meant to address that.

Because of that goal, this site assumes that the reader is already comfortable doing basic data manipulations (e.g. loading CSVs, tabulating data, merging data) in a language like Stata, R, Python, or Julia. If you don't have that background, there are lots of great resources for getting started with these programs. And if you want to know more about *why* there are so many of these data science programs and how they compare, you can jump here (put in link eventually).

.. toctree::
   :maxdepth: 2

   How Computers Think About Numbers <data_types>
   Defensive Programming <defensive_programming>
   Parallelism <parallelism>
   Big Data and Memory Hierarchy <memory_hierarchy>
   Speed <performance>
   The Command Line <command_line>
   Git and Github <git_and_github>
   Getting Help Online <getting_help>
   Understanding Programming Language Ecosystem <languages>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

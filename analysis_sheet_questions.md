Read the Wikipedia page on Big-O notation at
<http://en.wikipedia.org/wiki/Big_O_notation> and answer the following
questions:

1.  What is the order of growth of $n^3 + n^2$? What about
    $1000000 n^3 + n^2$? What about $n^3 + 1000000 n^2$?

    all three of those are of the cubic order of growth because the leading term is cubic.

2.  What is the order of growth of $(n^2 + n) \cdot (n + 1)$? Before you
    start multiplying, remember that you only need the leading term.

    This one is also cubic because the leading term is going to be cubic.

3.  If $f$ is in $O(g)$, for some unspecified function $g$, what can we
    say about $af+b$, where $a$ and $b$ are constants?

    We can say that $af+b$ is also going to be in $O(g)$

4.  If $f_1$ and $f_2$ are in $O(g)$, what can we say about $f_1 + f_2$?

    $f_1 + f_2 $ will be in $O(g)$

5.  If $f_1$ is in $O(g)$ and $f_2$ is in $O(h)$, what can we say about
    $f_1 + f_2$?

    It will belong to the higher of the two orders of growth.

6.  If $f_1$ is in $O(g)$ and $f_2$ is in $O(h)$, what can we say about
    $f_1 \cdot f_2$?

    It will belong to $O(gh)$



Read the Wikipedia page on sorting algorithms at
<http://en.wikipedia.org/wiki/Sorting_algorithm> and answer the
following questions:

1.  What is a "comparison sort?" What is the best worst-case order of growth for a comparison sort? What is the best worst-case order of growth for any sort algorithm?

    A comparison sort puts the items of a list through a sort operation, often a boolean, that decides if it should remain on the list or not. The best case order of growth is $n$ and the worst case looks to be $n^2$

2.  What is the order of growth of bubble sort, and why does Barack Obama think it is "the wrong way to go?"

    The order of growth for bubble sort is $n^2$ and it is the wrong way to go in that scenario because when working with a large data set, this would quickly get out of hand. 

3.  What is the order of growth of radix sort? What preconditions do we need to use it?

    Radix sort is an algorithm that sorts numbers by processing individual digits. $n$ numbers consisting of $k$ digits each are sorted in $O(n · k)$ time.

4.  What is a stable sort and why might it matter in practice?

    A stable sort preserves the order of input and output if certain conditions were met. A good example of when this would be useful if if you needed to sort a data set multiple times, first by one condition, then by another. This would allow you to do the second sort without undoing the results of the first.

5.  What is the worst sorting algorithm (that has a name)?

    Bogosort is the worst algorithm with a name. The run time is unbounded.

6.  What sort algorithm does the C library use? What sort algorithm does Python use? Are these algorithms stable? You might have to Google around to find these answers.

    "In C programming language, there are multiple sorting algorithms available, which can be incorporated inside the code. The various types of sorting methods possible in the C language are Bubble sort, Selection sort, Quick sort, Merge sort, Heap sort and Insertion sort." 

    "Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort."

    Tim sort is stable. The C library also uses stable sort algorithms.

7.  Many of the non-comparison sorts are linear, so why does Python use an $O(n \log n)$ comparison sort?

    It is used because it is capable of handling complex data sets.
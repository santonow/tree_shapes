# tree_shapes
A little project for Comparative Genomics class. 

The task was to calculate shapes of rooted unlabeled binary trees of given leaf count.

I thought it was a fun assignment, because I could abuse Python sets with to allowing trees to be hashed.

The algorithm is explained in the docstrings. Takes exponential time sadly.

### Usage:

```bash
$ python tree_shapes.py 4
((,),(,));
(((,),),);
```

How many unlabeled rooted binary trees with given number of trees are there?

```bash
$ for i in {1..10}; do python tree_shapes.py $i | wc -l; done 
       1
       1
       1
       2
       3
       6
      11
      23
      46
      98
```
OEIS A001190 says the same.
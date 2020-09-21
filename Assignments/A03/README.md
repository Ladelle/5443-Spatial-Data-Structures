## Assignment 3 - Flask API
#### Due: 09-28-2020 (Monday @ 4:30 p.m.)

For this assignment, you will use flask to query a spatial data structure for N points closest to a mouse click, and display those points on a map. This is just to get you started for our bigger project. You can use an R-Tree or a KD-Tree it doesn't matter. I have a few links below of where you can find the resources to implement your spatial data structure. It doesn't matter which one you pick to start, because you will eventually will implement them both and will run comparisons on differing queries between the those structures and more. 

### Resources for R-Tree and KD-Tree

Both R-Tree's and KD-Tree's store spatial data by continuously dividing the space into smaller and smaller sections. The basic difference is that KD-Trees divide each sub-space into quadrants, and R-Tree keeps creating smaller and smaller bounding boxes. Both of these have subtle differences when performing queries on our points. Here is a pretty good overview of both trees along with nearest neighbor and range queries.

- Article about `range queries` and `nearest neighbor queries`  
  - https://blog.mapbox.com/a-dive-into-spatial-search-algorithms-ebd0c5e39d2a


And here are a couple of implementations for both types of trees. Please post other implementations of either tree on slack if you find them. We want to stay within the `scipy` / `pandas` world since that will be the vast majority of documentation that we find and they both use `dataframes` to store data.

- Kdtree:
  - With code for tree:
    - https://scipy-cookbook.readthedocs.io/items/KDTree_example.html
  - Using scipy:
    - http://library.isr.ist.utl.pt/docs/scipy/spatial.html

- Rtree
  - Using libspatialindex lib:
    - https://libspatialindex.org/en/latest/
    - https://toblerity.org/rtree/index.html#home
  - With geopandas:
    - https://geoffboeing.com/2016/10/r-tree-spatial-index-python/



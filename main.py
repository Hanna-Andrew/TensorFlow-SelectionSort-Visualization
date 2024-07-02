import numpy as np
import tensorflow as tf
from sort import selection_sort
from visualize import plot_array

def main():
    x = int(input("How many numbers would you like the array to have?: "))
    
    array = tf.random.uniform([x], minval=1, maxval=100, dtype=tf.dtypes.int32, seed=12)
    array = np.array(array)

    print("Original random array:", array)
    
    selection_sort(array)
    
    print('The array after sorting in Ascending Order by selection sort is:', array)
    
    print("Graphic of Ascending Order of array")
    plot_array(array)

if __name__ == "__main__":
    main()

# algorythms-analysis

Additional functions in ```analysis.py```:
- **generate arrays(size)** - generates arrays of specified size for each case of the experiment
- **write_info(data, algo_name, arr_size, test_case, time)** - writes information about algorithm running time of specific case to a dictionary
structure of dictionary is the following:
```
{
  algorithm1: {
    size1: {
      case1: time
      case2: time
      ...
    }
    size2: {
      ...
    }
    ...
  }
  ...
}
```
- **get_case_info(data, case)** forms list of lists, where each sublist is separate algorithm's running time in a specified case

<hr></hr>

- **run_algorithms()** runs algorithms and writes data
- **build_diagrams()** main function of the module.

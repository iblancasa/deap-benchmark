# deap-benchmark

This repository is to study [Deap library](https://github.com/deap/deap) in comparation with [Pythoneo](https://github.com/iblancasa/PythonEO)

To run this, install dependences:
```bash
pip install -r requeriments.txt
```

## Run benchmarks

### Bitflip
```bash
python bitflip.py [numpy/lists] [native]
```

Arguments:
 * [numpy/lists]: you have to select if run the benchmark using numpy arrays or Python lists.
 * [native]: if you add this param, you will run the benchmark using native bitflip. Else, you will run a bitflip that only changes one bit.


 ### Onemax
 ```bash
 python onemax.py [numpy]
 ```

Arguments:
* [numpy]: if you run with this option, you will run the benchmark using numpy arrays. Else, you will use Python lists.


### Xover
```bash
python xover.py [numpy]
```

Arguments:
* [numpy]: if you run with this option, you will run the benchmark using numpy arrays. Else, you will use Python lists.

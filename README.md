# Python fire demo

Demo for Python [google/python-fire](https://github.com/google/python-fire) library

## Why Python file?
* Fire can be applied on any Python object: functions, classes, modules, objects, dictionaries, lists, tuples, etc. They all work!
* No need to parse explicetly command line arguments, instead Python definition is used

## How to get help
see [demo_simple_01.py](demo_simple_01.py)
```bash
$ python demo_with_class_01.py --help
```


## How to run while passing arguments
see [demo_simple_01.py](demo_simple_01.py)
```bash
$ python demo_with_class_01.py hello_world "John Doe"
Hello John Doe! ツ
```

## Expose all functions
see [demo_simple_01.py](demo_simple_01.py)
```python
if __name__ == "__main__":
    fire.Fire()
```

## Expose only a single function
see [demo_simple_02.py](demo_simple_02.py)
```python
if __name__ == "__main__":
    fire.Fire(hello_world)
```

## How to get help with docstring
see [demo_simple_02.py](demo_simple_02.py)
```python
def hello_world(name):
    """Let's say hello to someone and add a smile"""
    pass
```

```bash
$ python demo_simple_04.py hello_world --help
NAME
    demo_simple_02.py - Let's say hello to someone and add a smile

SYNOPSIS
    demo_simple_02.py NAME <flags>

DESCRIPTION
    Let's say hello to someone and add a smile

POSITIONAL ARGUMENTS
    NAME
        Type: str
        someone's name

FLAGS
    --smile=SMILE
        Type: str
        Default: 'ツ'
        optional smile to add to the message
    --exclamation=EXCLAMATION
        Type: bool
        Default: False
        add an exclamation mark

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

## Optional parameters
see [demo_simple_02.py](demo_simple_02.py)
```python
def hello_world(name, smile="ツ"):
    pass
```

```bash
$ python demo_simple_02.py "Alice" --smile "ツ"
Hello, Alice! ツ
```

## Boolean flags
see [demo_simple_02.py](demo_simple_02.py)
```python
def hello_world(name, smile="ツ", exclamation: bool = False):
    pass
```

```bash
$ python demo_simple_02.py "Alice" --smile "ツ" --exclamation
Hello, Alice! ツ
```

## Functions with `_` are hidden
see [demo_simple_03.py](demo_simple_03.py)
```bash
$ python demo_with_class_03.py --help
```

## Explicetly define functions to be exposed
see [demo_simple_04.py](demo_simple_04.py)
```python
if __name__ == "__main__":
    fire.Fire({
        "hello_world": hello_world,
        "salut_le_monde": salut_le_monde
    })
```

```bash
$ python demo_simple_04.py ça_va
ERROR: Cannot find key: ça_va
Usage: demo_simple_04.py <command>
  available commands:    hello_world | salut_le_monde
```

## Running in interactive mode
see [demo_simple_04.py](demo_simple_04.py)
Use `--` to enter interactive mode 
```bash
python demo_simple_04.py -- --interactive
Fire is starting a Python REPL with the following objects:
Modules: fire
Objects: component, demo_simple_04.py, hello_world, result, salut_le_monde, trace, ça_va

(InteractiveConsole)
>>> hello_world("test")
'Hello test!'
```

## Call on return object
see [demo_simple_04.py](demo_simple_04.py)
```bash
$ python demo_simple_04.py hello_world "Alice"
Hello Alice!
$ python demo_simple_04.py hello_world "Alice" upper
HELLO ALICE!
$ python demo_simple_04.py hello_world "Alice" lower
hello alice!
```

## Grouping commands using Python class
see [demo_with_class_01.py](demo_with_class_01.py)
```bash
$ python demo_with_class_01.py hello_world "John Doe"
Hello John Doe! ツ
```

## More optional arguments for class constructor
see [demo_with_class_01.py](demo_with_class_01.py)
```bash
$ python demo_with_class_01.py salut_le_monde "Monsieur Dupont" --smile ":)"
Salut le monde, c'est moi Monsieur Dupont! :)
```

## Grouping commands with Python classes
see [demo_with_class_02.py](demo_with_class_02.py)
```bash
$ python demo_with_class_02.py greetings hello_world "John Doe"
Hello John Doe! ツ
$ python demo_with_class_02.py farwell adieu_le_monde
Adieu tout le monde
```

## Chaining functions, i.e., simple DSL
see [demo_with_class_03.py](demo_with_class_03.py)
```bash
python demo_with_class_03.py hello_world "John Doe" farwell_everyone end_here
Hello John Doe! ツ
Farewell everyone
```

## Tracing
see [demo_with_class_03.py](demo_with_class_03.py)
```bash
$ python demo_with_class_03.py hello_world "John Doe" farwell_everyone end_here -- --trace

Fire trace:
1. Initial component
2. Instantiated class "PhrasesGenerator" (demo_with_class_03.py:4)
3. Accessed property "hello_world" (demo_with_class_03.py:8)
4. Called routine "hello_world" (demo_with_class_03.py:8)
5. Accessed property "farwell_everyone" (demo_with_class_03.py:20)
6. Called routine "farwell_everyone" (demo_with_class_03.py:20)
7. Accessed property "end_here" (demo_with_class_03.py:28)
```

# References
* [The Python Fire Guide](https://github.com/google/python-fire/blob/master/docs/guide.md)

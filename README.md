## How to get help

```bash
$ python demo_with_class_01.py --help
```


## How to run while passing arguments
```bash
$ python demo_with_class_01.py hello_world "John Doe"
Hello John Doe! ツ
```

## Expose all functions

```python
if __name__ == "__main__":
    fire.Fire()
```

## Expose only a single function

```python
if __name__ == "__main__":
    fire.Fire(hello_world)
```

## How to get help with docstring
```python
def hello_world(name):
    """Let's say hello to someone and add a smile"""
    pass
```

```bash
$ python demo_with_class_02.py --help
```

## Optional parameters
```python
def hello_world(name, smile="ツ"):
    pass
```

```bash
$ python demo_simple_02.py "Alice" --smile "ツ"
Hello, Alice! ツ
```

## Functions with `_` are hidden
```bash
$ python demo_with_class_03.py --help
```

## Explicetly define functions to be exposed
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

## Grouping commands using Python class
```bash
$ python demo_with_class_01.py hello_world "John Doe"
Hello John Doe! ツ
```

## More optional arguments for class constructor
```bash
$ python demo_with_class_01.py salut_le_monde "Monsieur Dupont" --smile ":)"
Salut le monde, c'est moi Monsieur Dupont! :)
```

## Grouping commands with Python classes
```bash
$ python demo_with_class_02.py greetings hello_world "John Doe"
Hello John Doe! ツ
$ python demo_with_class_02.py farwell adieu_le_monde
Adieu tout le monde
```

## Chaining functions, i.e., simple DSL
```bash
python demo_with_class_03.py hello_world "John Doe" farwell_everyone end_here
Hello John Doe! ツ
Farewell everyone
```

## Tracing
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
## PROGRAMMING

# Dictionaries

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/725e6bee-01fd-4769-a808-36029e914bac" width="800" />
</div>

## Even more organising

Dictionaries are similar to lists, however the data is stored in key :
 value pairs. While a list automatically assigns an index to each item
within, in a dictionary we need to specify the data item but also the
key it will be stored against.

Let's jump into an example:

```py
mydictionary = {
    "firstname": "james",
    "lastname": "lyne",
    "age": 974
}

print(mydictionary)
print(mydictionary["firstname"])
print(mydictionary.get("lastname"))
```

```console
$ python3 test.py
{'firstname': 'james', 'lastname': 'lyne', 'age': 974}
james
lyne
```

In the example code we can see the structure of a dictionary. It's similar to the [Lists and tuples](https://play.cyberstart.com/field-manual/8fca838a-d7eb-11eb-93b2-0242ac140009)
 we've already looked at, though it's spread over a few lines to make it
 easier to read. Each item is still separated by a comma, however each
item contains two components separated by a colon, for example `"firstname": "james"`. These are the **key** (firstname) and **value** (james).

As with other collections, we're still able to store different data
types within. Here we have a couple of string values, as well as an
integer (the value for "age").

In the code we print a few things. The first is the dictionary itsel - note the output is on a single line. For the second print, we can
access an item inside the dictionary by using square brackets and the **key** associated with the value we're after; much like we can use an **index** with other collections or strings.

Alternatively, we can also retrieve items from the dictionary using the `get` method, providing the key as an argument.

Unlike tuples, dictionaries are not read-only. As such, we can add, update and remove data where needed:

```py
mydictionary = {}
print(mydictionary)
mydictionary["foo"] = "bar"
print(mydictionary)
mydictionary.update({"hello": "world", "foo": "new"})
print(mydictionary)
mydictionary.pop("hello")
print(mydictionary)
```

```bash
$ python3 test.py
{}
{'foo': 'bar'}
{'foo': 'new', 'hello': 'world'}
{'foo': 'new'}
```

Here we start with an empty dictionary, which we can see is empty
when printed. Next, we add a new item much like we would set a regular
variable: the `foo` key inside the dictionary is equal to `bar`.

There's also a neat function available for dictionaries called `update`. Here we provide a separate dictionary as the argument, and note that we have a new item (with the key `hello`) but also an item with an existing key (`foo`). The result of the `update` is that the new item is created, while the existing item is overwritten with the new value. That's pretty cool!

Finally, if we want to remove something from the dictionary we can use the `pop`
 method. Here we can provide a key we want to remove as the argument,
and we can confirm in the output that the key : value pair for the key `hello` has been removed.

What's also very powerful with all of these collections is that they
can contain other collections, allowing us to have very complex sets of
data, structured in whatever way we need. For example:

```py
taxi = {
    "make": "Honda",
    "model": "Accord",
    "registration": "AB21 CDE",
    "attributes": {
        "capacity": 5,
        "fuel": "diesel",
        "range": "400 miles"
    },
    "current\_passengers": [
        {"name": "Jane"},
        {"name": "John"},
    ],
}
```

Here we have a top-level dictionary (the variable `taxi`) which contains some strings, but also another dictionary (the value for key `attributes`) as well as a list of more dictionaries (the value for key `current_passengers`)!

> When combining all the different data types available you'll find
> many creative and powerful ways to store, manipulate and manage data
> inside your programs. Be sure to experiment and identify which types are
> best suited to your desired use-cases!

<div align="center">

[← Previous: 5.06 - Lists and tuples](ListsAndTuples5.6.md) | [Next: 5.08 - Conditionals (if statements) →](Conditionals(ifStatements)5.8.md)
:-|-:

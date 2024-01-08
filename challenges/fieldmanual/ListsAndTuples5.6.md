## PROGRAMMING

# Lists and tuples

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/1b46ca67-a255-42b8-803f-f4a83a753f82" width="800" />
</div>

## Organising data

### Lists

Lists are a useful 'collection' data type that are designed to enable
 us to store multiple 'things' in a single variable. There are different
 types of collections in Python which serve different purposes, for
example some which really care about the order of items within or others
 which are read-only. As you grow to understand these different types
you'll get a feel for which is suitable for your use-case.

For now, let's start looking at an example of a simple list:

```py
interesting = [19, 'string', 3, 1337]
print(interesting)
print(interesting[3])
```

To begin with we create a variable `interesting` with a list - we use the square brackets, with comma separated values within, to tell Python this is what we're looking to do.

If we just print out the variable `interesting` we would see `[19, 'string', 3, 1337]`.
 That's not so... interesting - it looks exactly the same as we typed.
In fact, for all we know it could just be a string! However, with the
next line we can see something a bit more meaningful.

We print `interesting[3]`, which (as briefly mentioned in the [Variables](https://play.cyberstart.com/field-manual/8fc782c0-d7eb-11eb-9054-0242ac140009) page) asks for the value at **index 3**. As noted before, the index starts at 0, and so the value printed here would be `1337`.

Note that the items inside the list remain in the order we provided
them in. They're not being automatically sorted in any particular order.
 It also contains different types of data; we have both integers and a
string.

Much like the string concatenation we did previously, you can also concatenate lists in a similar way:

```py
print(interesting + ["a new list"])
```

The result of which would be: `[19, 'string', 3, 1337, 'a new list']`. Python has neatly appended our second list on to the first.

You can also add or remove items from the list with its built in functions. For example:

```py
interesting = [19, 'string', 3, 1337]
interesting.append('another string')
print(interesting)
interesting.remove('string')
print(interesting)
interesting.remove('string')
```

If we run this, we would see:

```console
$ python3 test.py
[19, 'string', 3, 1337, 'another string']
[19, 3, 1337, 'another string']
Traceback (most recent call last):
  File "test.py", line 6, in <module>
    interesting.remove('string')
ValueError: list.remove(x): x not in list
```

First, we can see that the `append` function has added the argument `'another string'` to the end of the list. Next, we can see the `remove` function has removed the argument `'string'` from the list. Neat!

Finally, we attempted to remove 'string' from the list a second time.
 As it no longer exists, Python isn't able to remove it and so it *throws* an error, telling us about the problem.

Lists can also be sorted! For example:

```py
interesting = [19, 3, 1337]
print(interesting)
interesting.sort()
print(interesting)
```

```console
$ python3 test.py
[19, 3, 1337]
[3, 19, 1337]
```

Note that here we removed the 'string' item from the list. This is
because Python doesn't like trying to sort a list with different data
type - what comes first? a number or a string? - and it would have
errored. The first `print` shows the list in the order we created. The second `print`, however, is after we've sorted our list and of course shows the numbers in their new sorted ascending order.

As you can see, lists are a simple way to group a bunch of
information together, allowing you to interact with the data and update
the list as needed.

### Tuples

A Tuple is similar to a list, however it is read-only. That is; once
you have defined the items in the tuple when it's created, you can't
modify the items within, add or remove items etc. Here's an example:

```py
readonly = (19, 3, 1337)
print(readonly)
print(readonly[0])
print(sorted(readonly))
readonly.append(123)
```

```console
$ python3 test.py
(19, 3, 1337)
19
[3, 19, 1337]
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    readonly.append(123)
AttributeError: 'tuple' object has no attribute 'append'
```

As you can see, can still interact with a tuple in the same ways you
could a list: accessing a particular index, sorting, etc. There's some
interesting things to note here however!

First, you'll notice we created the tuple slightly differently -
using parenthesis instead of square brackets. Second, rather than using
the `sort` function to change the tuple to a sorted version, we instead have to use the `sorted` function. This is because the tuple is read-only; we can't change it. Instead, the `sorted` function takes the contents and creates a list with the items in order.

Finally, if we try to append an item to the tuple we're given an error - the `append` function doesn't exist.

There is much more you can do with lists and tuples, far more than we
 can cover in this Field Manual. This page is already quite long!
However, hopefully you can start to see how these data types can be used
 and how they might fit into your own programs.

[← Previous: 5.05 - Mathematical functions](https://play.cyberstart.com/field-manual/8fc98354-d7eb-11eb-8ede-0242ac140009)
[Next: 5.07 - Dictionaries →](https://play.cyberstart.com/field-manual/8fcb8488-d7eb-11eb-bf0c-0242ac140009)

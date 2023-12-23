# 💾 Defence Data - L05 C02

The team on Earth are getting a little concerned, they want to know which countries we think would be vulnerable if the aliens decide to attack, which is sounding like a real possibility now. See if you can generate a valid xml file at /tmp/vulnerable-countries.xml that contains a list of country nodes that have name attributes. The third node should be Panama.

**Tip:** Generate the valid xml file with Panama as the third country to get the flag.

> 💡 Hint: Remember, each element has to have a name attribute and the third element has to be Panama.
>
> It should look like this: >
>
>   <country name="Panama">Panama</country>

## Answer

```python
#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node.
# Each country node should have a name attribute.
# The third node name should be Panama.
#
with open('/tmp/vulnerable-countries.xml', 'w') as xml:
  xml.write('<root>')
  xml.write('<country name="Bla">Bla</country>')
  xml.write('<country name="Bla">Bla</country>')
  xml.write('<country name="Panama">Panama</country>')
  xml.write('</root>')
```

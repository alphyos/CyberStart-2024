## WALKTHROUGHS

# Secret Caesar

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, agents have recovered some documents from one of the
gang's bike shops, and on review have noticed some references that look a
 little odd. We think they might be encrypted with a **Caesar Cipher**, and we believe that the cipher offset for each reference is determined by the **order quantity**.

We need to try and decrypt the references, using the order quantity
offset, to find a decrypted reference starting with the word "**BAR**". We can submit this reference in full as the flag to complete the challenge.

## Solution

A Caesar Cipher is a particular method of encrypting text where the
letters are 'shifted' by a particular offset, ie a number. For example,
if we started with the letter A and an offset of 2, it becomes C. For
more information, check out the [Caesar or ROT ciphers](https://play.cyberstart.com/field-manual/8fa4a304-d7eb-11eb-9c47-0242ac140009) page of the Field Manual.

We could decrypt these references manually: working out each
individual letter based on the offset (the quantity). We could also
search for an online Caesar Cipher decoding tool to handle this for us.
Either way, we can take each of the references, apply to each set of
letters and spot that one of them starts with the word "BAR": `BARSTEM`. We can submit this as the flag for the challenge to complete it.

## Real-world Uses

There's at least a couple of techniques being used here. The first is
 a Caesar Cipher, which isn't really a secure means of concealing
messages these days as computers can try all 26 shift offset variations
and identify any readable English words instantly.

However, the other technique is those encrypted strings (and even the offsets) for each, is *visible in plain sight*.
 Here they're acting as other data - a quantity and reference, which at
first glance doesn't appear suspicious but these data items have another
 meaning to the cyber criminals. A brazen way of communicating can be
very effective, it can appear innocent and not even be a suspected way
to send data, but is far from what it appears to be.

[← Previous: 8.03.06 - Executable](https://play.cyberstart.com/field-manual/6ab82c3a-0e89-11ec-82a8-0242ac130003)
[Next: 8.03.08 - Hidden Report →](https://play.cyberstart.com/field-manual/a3c9a8fa-0e89-11ec-82a8-0242ac130003)

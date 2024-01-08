## CRYPTOGRAPHY

# Hexadecimal

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/e21566e4-39bb-4d67-b4aa-605b0f0d8de1" width="800" />
</div>

## 16 base are belong to us

Hexadecimal (otherwise known as hex) is hugely important in computer
science and cyber security, especially on offensive tasks, hacking and
defensive roles like forensics. Typically, in everyday life we use a *base 10* numbering system (aka **Decimal** or **Denary**), that is; numbers 0 - 9. **Hexadecimal** however is base 16 (think of "hex" being 6, like *hexagon* and "decimal" being 10, like *decade* ... 6 + 10 = 16). A base 16 system stores values in a more space efficient and easy to process way for computers.

Take a look at this table to get a quick understanding:

| Decimal | Binary | Hex |
| --- | --- | --- |
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| 10 | 1010 | A |
| 11 | 1011 | B |
| 12 | 1100 | C |
| 13 | 1101 | D |
| 14 | 1110 | E |
| 15 | 1111 | F |

## Space Saving

Notice how when we get to `10` in decimal, the hex value becomes `A`. This is powerful particularly when it comes to dealing with larger data values. For example, the value `D` in hex is `1101`
 in binary. This is 4 bits of data in size (count the individual binary
bits, there are 4!). If we want, we can represent an 8 bit number, which
 can be much larger.

But by considering even just 2 digits, in decimal we've got the
ability to only have a range of 00 - 99 (10 x 10), so that's a scope of
100 variations. Within hexadecimal, we have 00 - FF, that provides a
range of 256 possibilities (16 x 16). The space-saving becomes even
greater as the number of digits grows - increase by just another digit
to 3; in decimal we have a range of 1,000 (10 x 10 x 10), but
hexadecimal has 4,096 (16 x 16 x 16). By the time we get to 6 digits,
that's a range of 1,000,000 in decimal, but hexadecimal has an
impressive range of 16,777,216, almost 17 times as much! With files
perhaps being many megabytes, you can see how it can save a lot of
space, as you can fit more data within less space.

## Converting and editing

Having data in hex format doesn't change the underlying data, it is
just a more efficient way of communicating that data. For this reason
it's often used as a means of encoding and sometimes computers will
convert data to hexadecimal before transmitting it. A lot of web
applications will do this, for example.

If you want to convert data to or from other formats quickly and
easily, there's some great online tools available. Simply just search
for what you'd like to achieve and there will be a range of great tools
ready to covert data for you.

There's some great hex editing tools to make use of if you need to do more than just a quick conversion. Some of these might be [hexedit](https://linux.die.net/man/1/hexedit) if you want to edit some hex in your terminal, [Ghex](https://wiki.gnome.org/Apps/Ghex) if you'd prefer a GUI app and there's great online editors such as [HexEd](https://hexed.it/) if you don't want to install anything and just want something in your browser.

<div align="center">

[← Previous: 3.05.01 - ASCII](Ascii3.5.1.md) | [Next: 3.05.03 - QR codes and barcodes →](QrCodesAndBarcodes3.5.3.md)
:-|-:

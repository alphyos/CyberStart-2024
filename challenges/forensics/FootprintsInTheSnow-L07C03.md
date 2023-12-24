# 🎿 Footprints in The Snow - L07 C03

It looks like the bad guys left a trail behind. For example, they left a suspicious PDF on the system, but it seems to be empty. Investigate and see if you can figure out what it is.

**Tip:** Analyse the PDF to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: PDF parsers can be useful in analyzing PDF's. Also, strange object?

</details>

## Files

- [emptyPDF.pdf](/assets/footprintsinthesnow1.pdf)

<details><summary>

## Step by Step</summary>

- Download the file and either view the file contents with `cat filename`or a pdf parser with a command such as `pdf-parser filename`
- Digging around through there, you should spot a section labeled as "fonts" with a series of hex numbers hidden nearby
- Decoding this string of numbers  into ASCII gives you the flag

`flag: h1d1ng_am0ng_t3h_f0nt5`

</details>

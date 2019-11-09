# stylename.py

## About

`stylename.py` is a `.ttf` and `.otf` font style renaming script that edits OpenType name table ID 2 and 17 records.  It requires the Python 3.6+ interpreter.

## Dependency
- [fonttools](https://github.com/fonttools/fonttools) Python library (requires v4.0.0+)

Install with:

```
pip3 install fonttools
```

## Usage

The script usage is as follows:

```
$ python3 stylename.py [OPTIONS] [FONT PATH]
```

This script updates existing OpenType name table records nameID 2 and 17 with command line definitions.  The following command line options are supported:

- `--id2` : defines all nameID 2 records in font
- `--id17` : defines all nameID 17 records in font
- `--all` : defines all nameID 2 and nameID 17 records in font (mutually exclusive with `--id2` and `--id17`)

**Note**: this re-writes the name tables in the font passed as an argument on the command line (i.e. writes file in place) so make a copy before you use this tool if you intend to maintain the fonts with the former name table definitions for any reason (though you can simply re-write with the previous name if you forget...).

**Note**: This script to does not write new OpenType name ID 2 or 17 records in the font if they do not previously exist.

### Examples

#### Example Pro Regular

```
$ python3 stylename.py --id2 Regular ExamplePro-Regular.ttf
```

#### Example Pro Semibold

```
$ python3 stylename.py --id2 Regular --id17 Semibold ExamplePro-Semibold.ttf
```

#### Example Pro Semibold Italic

```
$ python3 stylename.py --id2 Italic --id17 "Semibold Italic" ExamplePro-SemiboldItalic.ttf
```

**Note**: Use quotation marks around argument strings that include spaces.

## License

[MIT License](LICENSE)
# General Types
- `%T` : Type
- `%v` : Value
- `%%` : Literal % sign

# Boolean
- `%t` : true or false

# Strings
- `%s` : default
- `%q` : double quoted string
- `%x` : base 16, lower-case, two characters per byte
- `%X` : base 16, upper-case, two characters per byte

# Integers
- `%b` : base 2
- `%c` : the character repr by the corr Unicode code point
- `%o` : base 8
- `%O` : base 8 with 0o prefix
- `%d` : base 10
- `%x` : base 16 , with lower-case letters for a-f
- `%X` : base 16, with upper-case letters for A-F
- `%U` : Unicode format: U+1234; same as "U+%04X"

# Floating 
- `%b` : decimalless scientific notation with exponent a power of two,
	in the manner of strconv. - FormatFloat with the 'b' format,
	e.g. -123456p-78
- `%e` : scientific notation, e.g. -1.234456e+78
- `%E` : scientific notation, e.g. -1.234456E+78
- `%f` : decimal point but no exponent, e.g. 123.456
- `%F` : synonym for `%f`
- `%g` : `%e` for large exponents, %f otherwise. Precision is discussed below.
- `%G` : `%E` for large exponents, `%F` otherwise
- `%x` : hexadecimal notation (with decimal power of two exponent), e.g. -0x1.23abcp+20
- `%X` : upper-case hexadecimal notation, e.g. -0X1.23ABCP+20

## Slice
`%p` : address of 0th element in base 16 notation, with leading 0x

## Pointer
`%p` : base 16 notation, with leading 0x
The `%b`, `%d`, `%o`, `%x` and `%X` verbs also work with pointers,
formatting the value exactly as if it were an integer.

### **For compound objects, the elements are printed using these rules, recursively, laid out like this:**

- `struct` : {field0 field1 ...}
- `array`, `slice` : [elem0 elem1 ...]
- `maps` :  map[key1:value1 key2:value2 ...]
- `pointer` to above :   &{}, &[], &map[]

### **Precision**
- `%f` : default width, default precision
- `%9f` : width 9, default precision
- `%.2f` : default width, precision 2
- `%9.2f` :  width 9, precision 2
- `%9.f` : width 9, precision 0
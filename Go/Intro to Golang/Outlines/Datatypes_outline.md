# Data Types
## Bolean:
- `true`
- `false`
## String:
- `"example string"`
## Integers:
### **Signed integers:**
- `int8`: (-128, 127)
- `int16`: (-32768, 32767)
- `int32` or `rune` :
(-2147483648, 2147483647)
- `int64`: (-9223372036854775808, 9223372036854775807)
### **Unsigned integers:**
- `uint8`: (0, 255)
- `uint16`: (0, 65535)
- `uint32` or `rune` :
(0, 4294967295)
- `uint64`: (0, 18446744073709551615)
## Floating point:
- `float32`
- `float64`

## Complex Numbers:
- `complex64`:
    - `float32` + i `float32`
- `complex128`:
    - `float64` + i `float64`
### Machine Dependent types:
- `uint`: (32 or 64) [system dependent]
- `int`: (32 or 64) [system dependent]
- `unintptr`: 
    - Unisigned integer to store the uninterpreted bits of a pointer value.
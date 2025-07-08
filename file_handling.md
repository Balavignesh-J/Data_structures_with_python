# 📂 File Handling in Python

## ✅ 1️⃣ What is file handling?

File handling means **opening**, **reading**, **writing**, and **closing** files from your Python program.

Python makes it easy with built-in functions and methods.

---

## ✅ 2️⃣ File Modes in Python

When you open a file, you specify the *mode*:

| Mode | Meaning                                          |
|------|--------------------------------------------------|
| `'r'`  | Read (default), error if file does not exist     |
| `'w'`  | Write, creates new file or truncates existing    |
| `'a'`  | Append, creates new file or appends to existing  |
| `'x'`  | Exclusive creation, fails if file exists         |
| `'b'`  | Binary mode (e.g., `'rb'`, `'wb'`)               |
| `'t'`  | Text mode (default, e.g., `'rt'`, `'wt'`)        |
| `'+'`  | Read and write (e.g., `'r+'`, `'w+'`, `'a+'`)    |

---

## ✅ 3️⃣ Opening a file

```python
f = open('example.txt', 'r')
```

- `'example.txt'` is the file name.
- `'r'` is the mode.

---

## ✅ 4️⃣ Reading a file

### 4.1 `read()`
Reads the entire contents:

```python
f = open('example.txt', 'r')
content = f.read()
print(content)
f.close()
```

---

### 4.2 `readline()`
Reads one line at a time:

```python
f = open('example.txt', 'r')
line = f.readline()
print(line)
f.close()
```

---

### 4.3 `readlines()`
Reads all lines into a list:

```python
f = open('example.txt', 'r')
lines = f.readlines()
print(lines)
f.close()
```

---

## ✅ 5️⃣ Writing to a file

### 5.1 Overwrite (`w` mode)

```python
f = open('example.txt', 'w')
f.write("Hello, world!")
f.close()
```

This will **overwrite** existing content.

---

### 5.2 Append (`a` mode)

```python
f = open('example.txt', 'a')
f.write("\\nThis is a new line.")
f.close()
```

This **adds** to the end of the file.

---

## ✅ 6️⃣ Best Practice: Using `with`

Recommended way to handle files because it auto-closes the file:

```python
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)
```

No need to call `f.close()`.

---

## ✅ 7️⃣ Example: Writing and reading back

```python
# Write
with open('example.txt', 'w') as f:
    f.write("Line 1\\nLine 2\\nLine 3")

# Read
with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

---

## ✅ 8️⃣ Working with binary files

For images, audio, etc.:

```python
with open('image.jpg', 'rb') as f:
    data = f.read()
```

---

## ✅ 9️⃣ Checking if a file exists

Using the `os` module:

```python
import os

if os.path.exists('example.txt'):
    print("File exists!")
else:
    print("File not found!")
```

---

## ✅ 10️⃣ Deleting a file

```python
import os

os.remove('example.txt')
```

---

## ✅ 11️⃣ Example: Copying a file

```python
with open('source.txt', 'r') as src:
    data = src.read()

with open('destination.txt', 'w') as dst:
    dst.write(data)
```

---

## ✅ 12️⃣ Exception handling

Always handle errors for safer code:

```python
try:
    with open('example.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
```

---

## ✅ Summary

⭐ `open(filename, mode)` — opens a file  
⭐ `read()`, `readline()`, `readlines()` — for reading  
⭐ `write()`, `writelines()` — for writing  
⭐ `with` statement — best practice for auto-close  
⭐ `os` module — for checking, deleting files
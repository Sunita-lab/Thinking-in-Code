# Recursion to Iteration — Thinking Framework

A structured way to convert recursive logic into iterative form.

Derived from Binary Search, extended into general recursion patterns so it remains useful even for DFS, trees, and backtracking later.

---

## The Core Idea

Every recursive function is built from a few fundamental components.  
Each of these has a direct equivalent in iteration.

| Recursive Concept               | Iterative Equivalent                          |
|--------------------------------|----------------------------------------------|
| Changing parameters            | Variables updated inside a loop              |
| Fixed parameters               | Stay as function arguments                  |
| Base case                      | Loop condition (termination condition)      |
| Recursive call                 | Variable updates OR explicit stack handling |
| Return on success              | Return inside loop immediately              |
| Return on failure (base case)  | Return after loop ends                      |

---

## Step-by-Step Process (Linear Recursion)

This process applies to problems where recursion follows a single path  
(e.g., Binary Search).

---

### Step 1 — Separate fixed vs changing parameters

Look at the recursive function signature.

- Fixed → values that do NOT change across calls  
  (e.g., `arr`, `target`)
- Changing → values that update each call  
  (e.g., `left`, `right`)

Initialize changing variables using the values from the first recursive call.

---

### Step 2 — Base case → loop condition

The recursive base case becomes the **opposite condition** in the loop.

- Recursion stops when condition becomes true  
- Loop runs while that condition is false  

Examples:
- `if left > right` → `while left <= right`
- `if n == 0` → `while n > 0`

---

### Step 3 — Replace recursive calls with updates

Instead of calling the function again:

- Update the changing variables
- Let the loop handle the next iteration

This simulates the next recursive call.

---

### Step 4 — Return inside the loop

If recursion returns early (like when an element is found),  
iteration must also return immediately inside the loop.

Delaying the return leads to incorrect results.

---

### Step 5 — Return after the loop

This handles the base case outcome  
(e.g., element not found, condition failed).

---

## Binary Search — Example

```python
# Recursive
def binary_search(arr, x, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, x, left, mid - 1)
    else:
        return binary_search(arr, x, mid + 1, right)


# Iterative
def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return -1
``` 

 # The Hidden Layer — Call Stack

Recursion internally uses a **call stack** to manage function calls.

Each recursive call:
- stores its current state
- pauses execution
- resumes after deeper calls return

---

## Key Insight

> Recursion = function calls + state + implicit stack

Iteration replaces this with **explicit control**.

---

## Two Conversion Cases

### Case 1 — No need to remember past states

**Example:** Binary Search

- Only one active path at a time  
- No pending work after recursive call  

→ Can convert using:
- variables  
- `while` loop  

---

### Case 2 — Need to remember past states

**Examples:** DFS, tree traversal, backtracking

- Multiple recursive calls (branching)  
- Work remains after returning  

→ Must simulate stack manually:

```python
stack = []
stack.append(initial_state)

while stack:
    state = stack.pop()
    # process state
    # push next states  
```
# Types of Recursion → Conversion Strategy

Understanding the type of recursion determines how to convert it.

---

## 1. Linear Recursion (Single Path)

**Example:** Binary Search

- Only one recursive call at a time  
- No state needs to be preserved  

→ Convert using:
- variables  
- `while` loop  

---

## 2. Tree Recursion (Multiple Paths)

**Examples:** DFS, subsets, permutations

- Multiple branches  
- State must be preserved across paths  

→ Use explicit stack (LIFO)

---

## 3. Tail Recursion

**Example:** optimized factorial

- Recursive call is the last operation  
- No pending work after the call  

→ Directly convertible to iteration

---

## Why `while` and not `for`?

Recursion is **condition-driven**, not count-driven.

- `while` → runs until a condition fails  
- `for` → runs for a fixed number of iterations  

More importantly:

> `while` mimics repeated function calls until the base case is reached  

In recursion:
- we don't know how many steps it will take  
- we only know when to stop  

This aligns directly with `while`, not `for`.

---

## When NOT to Convert

- When recursion is simpler and easier to understand  
- When stack simulation becomes complex  
- When constraints do not require optimization  

---

## Key Mental Model

Do NOT think:

> "Replace recursion with loop"

Think:

> "Manually control execution instead of relying on the call stack"

---

## Origin

- Observed from Binary Search (Week 6)  
- Generalized before learning DFS / Trees  
- Will be extended further after stack-based problems       
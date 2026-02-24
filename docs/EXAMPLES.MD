# 📚 Examples - Agentic Calculator

**Comprehensive examples demonstrating the agent flow from prompt to response.**

This document provides detailed walkthroughs of how the system processes natural language inputs, showing exactly what happens at each step of the agentic pipeline.

---

## 📋 Table of Contents

- [Understanding the Flow](#-understanding-the-flow)
- [Basic Examples](#-basic-examples)
- [Intermediate Examples](#-intermediate-examples)
- [Advanced Examples](#-advanced-examples)
- [Complex Multi-Step Examples](#-complex-multi-step-examples)
- [Edge Cases](#-edge-cases)
- [Error Handling Examples](#-error-handling-examples)
- [Pattern Recognition Guide](#-pattern-recognition-guide)

---

## 🔄 Understanding the Flow

Every user prompt goes through **5 stages**:

```
1. INPUT       → User types natural language
2. PLANNING    → LLM generates execution plan (JSON)
3. VALIDATION  → Sandbox checks security
4. EXECUTION   → Specialists process operations
5. OUTPUT      → Results consolidate and return
```

Let's see this in action with real examples!

---

## 🎯 Basic Examples

### Example 1: Simple Addition

#### 👤 User Prompt
```
"Add 15 and 25"
```

#### 🔄 Agent Flow

**STAGE 1: INPUT RECEPTION**
```python
user_input = "Add 15 and 25"
orchestrator.execute(user_input)
```

**STAGE 2: LLM PLANNING**

The LLM receives:
```
System Prompt: "Convert natural language to math operations JSON..."
User Input: "Add 15 and 25"
```

LLM generates:
```json
{
  "steps": [
    {
      "operation": "add",
      "args": [15, 25],
      "description": "Somar 15 + 25"
    }
  ]
}
```

**Why this plan?**
- LLM identified the verb "Add" → maps to operation `add`
- Extracted numbers: `15` and `25` → becomes args
- Single operation → only 1 step needed

**STAGE 3: VALIDATION**

```python
Sandbox.validate_operation("add")
✅ "add" is in allowed_operations whitelist
✅ Arguments are valid numbers
✅ No security violations
```

**STAGE 4: EXECUTION**

```python
# Orchestrator calls the specialist
specialist = BasicOperations.add
result = specialist(15, 25)

# Specialist executes
def add(*args):
    return sum(args)  # 15 + 25 = 40

result = 40.0
```

**STAGE 5: OUTPUT**

```python
{
  "success": True,
  "input": "Add 15 and 25",
  "final_result": 40.0,
  "steps_executed": 1,
  "intermediate_results": [40.0]
}
```

#### 💬 User Sees
```
🤖 Agente: 40.0
```

---

### Example 2: Multiplication

#### 👤 User Prompt
```
"Multiply 7 by 8"
```

#### 🔄 Agent Flow (Abbreviated)

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "multiply", "args": [7, 8], "description": "7 × 8"}
  ]
}
```

**Key Differences from Example 1:**
- Verb "Multiply" → operation `multiply`
- Preposition "by" is understood by LLM as multiplication indicator
- Same single-step pattern

**Execution:**
```python
BasicOperations.multiply(7, 8)
# 7 * 8 = 56
```

**Result:** `56.0`

---

### Example 3: Division with Natural Language Variations

#### 👤 User Prompt (Variation A)
```
"Divide 100 by 4"
```

#### 👤 User Prompt (Variation B)
```
"What is 100 divided by 4?"
```

#### 👤 User Prompt (Variation C)
```
"100 over 4"
```

#### 🔄 Agent Flow

**All three variations produce the SAME plan:**

```json
{
  "steps": [
    {"operation": "divide", "args": [100, 4], "description": "100 ÷ 4"}
  ]
}
```

**Why?**
- LLM understands semantic equivalence
- "divide by", "divided by", "over" all mean division
- Question format vs statement format doesn't matter

**Result:** `25.0`

---

## 🎓 Intermediate Examples

### Example 4: Two-Step Calculation

#### 👤 User Prompt
```
"Add 5 and 3, then multiply by 2"
```

#### 🔄 Agent Flow

**STAGE 2: LLM PLANNING**

```json
{
  "steps": [
    {
      "operation": "add",
      "args": [5, 3],
      "description": "Somar 5 + 3"
    },
    {
      "operation": "multiply",
      "args": ["$result_0", 2],
      "description": "Multiplicar resultado anterior por 2"
    }
  ]
}
```

**🎯 Key Concept: Result References**

Notice `"$result_0"` in step 2!

This tells the system:
- "Use the result from step 0"
- Creates dependency chain
- Enables multi-step operations

**STAGE 4: EXECUTION**

**Step 0:**
```python
operation = "add"
args = [5, 3]
resolved_args = [5, 3]  # No references to resolve

result_0 = BasicOperations.add(5, 3)
# result_0 = 8.0

results = [8.0]
```

**Step 1:**
```python
operation = "multiply"
args = ["$result_0", 2]

# Resolve references
resolved_args = resolve_args(["$result_0", 2], results=[8.0])
# "$result_0" → results[0] → 8.0
resolved_args = [8.0, 2]

result_1 = BasicOperations.multiply(8.0, 2)
# result_1 = 16.0

results = [8.0, 16.0]
```

**STAGE 5: OUTPUT**

```python
{
  "success": True,
  "final_result": 16.0,
  "steps_executed": 2,
  "intermediate_results": [8.0, 16.0]
}
```

#### 💬 User Sees
```
🤖 Agente: 16.0
```

**Behind the scenes visible in logs:**
```
INFO: Step 0: Somar 5 + 3 → 8.0
INFO: Step 1: Multiplicar resultado anterior por 2 → 16.0
```

---

### Example 5: Statistical Calculation

#### 👤 User Prompt
```
"Calculate the average of 10, 20, 30"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {
      "operation": "mean",
      "args": [10, 20, 30],
      "description": "Calcular média de 10, 20, 30"
    }
  ]
}
```

**Execution:**
```python
StatisticsOperations.mean(10, 20, 30)

# Inside the method:
def mean(*args):
    return statistics.mean(args)
    # (10 + 20 + 30) / 3 = 20.0
```

**Result:** `20.0`

---

### Example 6: Advanced Math - Square Root

#### 👤 User Prompt
```
"What is the square root of 144?"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {
      "operation": "sqrt",
      "args": [144],
      "description": "Raiz quadrada de 144"
    }
  ]
}
```

**Execution:**
```python
AdvancedOperations.sqrt(144)

# Inside the method:
def sqrt(x):
    if x < 0:
        raise ValueError("Raiz de número negativo")
    return math.sqrt(x)  # √144 = 12.0
```

**Result:** `12.0`

---

## 🚀 Advanced Examples

### Example 7: Three-Step Chain

#### 👤 User Prompt
```
"Calculate the mean of 100, 200, 300, then take the square root, then divide by 2"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {
      "operation": "mean",
      "args": [100, 200, 300],
      "description": "Calcular média"
    },
    {
      "operation": "sqrt",
      "args": ["$result_0"],
      "description": "Raiz quadrada do resultado"
    },
    {
      "operation": "divide",
      "args": ["$result_1", 2],
      "description": "Dividir por 2"
    }
  ]
}
```

**Execution Flow:**

```python
# Step 0: Mean
mean(100, 200, 300) = 200.0
results = [200.0]

# Step 1: Square Root
# Resolve: "$result_0" → results[0] = 200.0
sqrt(200.0) = 14.142135...
results = [200.0, 14.142135]

# Step 2: Divide
# Resolve: "$result_1" → results[1] = 14.142135
divide(14.142135, 2) = 7.071067...
results = [200.0, 14.142135, 7.071067]
```

**Final Result:** `7.071067811865475`

---

### Example 8: Complex Expression

#### 👤 User Prompt
```
"Add 10 and 5, multiply the result by 3, then subtract 20"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {
      "operation": "add",
      "args": [10, 5],
      "description": "10 + 5"
    },
    {
      "operation": "multiply",
      "args": ["$result_0", 3],
      "description": "Resultado × 3"
    },
    {
      "operation": "subtract",
      "args": ["$result_1", 20],
      "description": "Resultado - 20"
    }
  ]
}
```

**Execution with Dependency Graph:**

```
Step 0: add(10, 5) = 15.0
         ↓
Step 1: multiply(15.0, 3) = 45.0
         ↓
Step 2: subtract(45.0, 20) = 25.0
```

**Verification:**
```
(10 + 5) × 3 - 20
= 15 × 3 - 20
= 45 - 20
= 25 ✅
```

---

## 🧩 Complex Multi-Step Examples

### Example 9: Statistics Pipeline

#### 👤 User Prompt
```
"Calculate the average of 5, 10, 15, 20, 25, then calculate the square root of that average"
```

#### 🔄 Complete Agent Flow

**INPUT STAGE:**
```python
user_input = "Calculate the average of 5, 10, 15, 20, 25, then calculate the square root of that average"
```

**PLANNING STAGE:**

LLM receives the full system prompt plus user input and generates:

```json
{
  "steps": [
    {
      "operation": "mean",
      "args": [5, 10, 15, 20, 25],
      "description": "Calcular média de 5, 10, 15, 20, 25"
    },
    {
      "operation": "sqrt",
      "args": ["$result_0"],
      "description": "Raiz quadrada da média"
    }
  ]
}
```

**VALIDATION STAGE:**

```python
# Step 0 validation
sandbox.validate_operation("mean")
✅ Operation allowed

# Step 1 validation
sandbox.validate_operation("sqrt")
✅ Operation allowed

# Arguments validation
[5, 10, 15, 20, 25] → all numbers ✅
["$result_0"] → valid reference ✅
```

**EXECUTION STAGE:**

```python
# === STEP 0 ===
print("Executing Step 0: mean")

operation = "mean"
args = [5, 10, 15, 20, 25]
resolved_args = [5, 10, 15, 20, 25]  # No references

specialist = StatisticsOperations.mean
result_0 = specialist(5, 10, 15, 20, 25)

# Inside mean():
# sum([5, 10, 15, 20, 25]) / 5 = 75 / 5 = 15.0

result_0 = 15.0
results = [15.0]

print(f"Step 0 result: {result_0}")

# === STEP 1 ===
print("Executing Step 1: sqrt")

operation = "sqrt"
args = ["$result_0"]

# Resolve reference
resolved_args = resolve_args(["$result_0"], results)
# "$result_0" → results[0] → 15.0
resolved_args = [15.0]

specialist = AdvancedOperations.sqrt
result_1 = specialist(15.0)

# Inside sqrt():
# math.sqrt(15.0) = 3.872983346207417

result_1 = 3.872983346207417
results = [15.0, 3.872983346207417]

print(f"Step 1 result: {result_1}")
```

**OUTPUT STAGE:**

```python
{
  "success": True,
  "input": "Calculate the average of 5, 10, 15, 20, 25, then calculate the square root of that average",
  "plan": {
    "steps": [...]  # Full plan
  },
  "steps_executed": 2,
  "intermediate_results": [15.0, 3.872983346207417],
  "final_result": 3.872983346207417
}
```

---

### Example 10: Compound Operations

#### 👤 User Prompt
```
"Multiply 8 by 3, add 12 to the result, then divide by 4"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "multiply", "args": [8, 3], "description": "8 × 3"},
    {"operation": "add", "args": ["$result_0", 12], "description": "Resultado + 12"},
    {"operation": "divide", "args": ["$result_1", 4], "description": "Resultado ÷ 4"}
  ]
}
```

**Execution Tree:**
```
multiply(8, 3) = 24.0
    ↓
add(24.0, 12) = 36.0
    ↓
divide(36.0, 4) = 9.0
```

**Mathematical Verification:**
```
(8 × 3 + 12) ÷ 4
= (24 + 12) ÷ 4
= 36 ÷ 4
= 9 ✅
```

---

## ⚠️ Edge Cases

### Example 11: Handling Zero Division

#### 👤 User Prompt
```
"Divide 10 by 0"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "divide", "args": [10, 0], "description": "10 ÷ 0"}
  ]
}
```

**Execution:**
```python
try:
    BasicOperations.divide(10, 0)
    
    # Inside divide():
    def divide(a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b
    
    # ❌ Raises ValueError
    
except ValueError as e:
    error = str(e)  # "Divisão por zero não permitida"
```

**Output:**
```python
{
  "success": False,
  "input": "Divide 10 by 0",
  "error": "Divisão por zero não permitida"
}
```

#### 💬 User Sees
```
❌ Erro: Divisão por zero não permitida
```

---

### Example 12: Negative Square Root

#### 👤 User Prompt
```
"Calculate the square root of -25"
```

#### 🔄 Agent Flow

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "sqrt", "args": [-25], "description": "√-25"}
  ]
}
```

**Execution:**
```python
try:
    AdvancedOperations.sqrt(-25)
    
    # Inside sqrt():
    def sqrt(x):
        if x < 0:
            raise ValueError("Raiz quadrada de número negativo")
        return math.sqrt(x)
    
    # ❌ Raises ValueError
    
except ValueError as e:
    error = str(e)
```

**Output:**
```python
{
  "success": False,
  "input": "Calculate the square root of -25",
  "error": "Raiz quadrada de número negativo"
}
```

---

### Example 13: Ambiguous Input

#### 👤 User Prompt
```
"Do something with 5 and 3"
```

#### 🔄 Agent Flow

**LLM Response:**

The LLM might generate:
```json
{
  "steps": [
    {"operation": "add", "args": [5, 3], "description": "Somar (operação padrão)"}
  ]
}
```

**OR** it might fail to generate valid JSON.

**Why this happens:**
- "Do something" is too vague
- LLM makes best guess (often defaults to addition)
- Not ideal - should prompt user for clarification

**Better prompt:**
```
"Add 5 and 3"  // Specific
"5 plus 3"     // Clear intent
```

---

## 🔍 Error Handling Examples

### Example 14: Invalid Operation

#### 👤 User Prompt
```
"Calculate the factorial of 5"
```

#### 🔄 Agent Flow

**LLM might generate:**
```json
{
  "steps": [
    {"operation": "factorial", "args": [5], "description": "5!"}
  ]
}
```

**Validation:**
```python
sandbox.validate_operation("factorial")

# Check whitelist:
allowed_operations = ["add", "subtract", "multiply", "divide", "sqrt", "power", "mean", "median"]

# ❌ "factorial" NOT in list
raise SecurityError("Operação 'factorial' não permitida")
```

**Output:**
```python
{
  "success": False,
  "input": "Calculate the factorial of 5",
  "error": "Operação 'factorial' não permitida"
}
```

#### 💬 User Sees
```
❌ Erro: Operação 'factorial' não permitida
```

**Solution:**
Add factorial specialist and whitelist it in config.yaml.

---

### Example 15: Malformed LLM Response

#### 👤 User Prompt
```
"Calculate something really weird and complex"
```

#### 🔄 Agent Flow

**LLM might return:**
```
I'm not sure how to interpret that. Could you be more specific?
```

**Parsing:**
```python
try:
    json_start = response.find('{')
    json_end = response.rfind('}') + 1
    
    # json_start = -1 (not found)
    
    if json_start == -1:
        raise ValueError("LLM não retornou JSON válido")
        
except ValueError as e:
    error = str(e)
```

**Output:**
```python
{
  "success": False,
  "input": "Calculate something really weird and complex",
  "error": "LLM não conseguiu gerar plano válido"
}
```

---

## 🎓 Pattern Recognition Guide

### How the LLM Recognizes Operations

#### Addition Patterns
```
✅ "Add 5 and 3"
✅ "5 plus 3"
✅ "Sum of 5 and 3"
✅ "5 + 3"
✅ "What is 5 added to 3?"
```

#### Subtraction Patterns
```
✅ "Subtract 3 from 5"
✅ "5 minus 3"
✅ "Difference between 5 and 3"
✅ "5 - 3"
✅ "Take away 3 from 5"
```

#### Multiplication Patterns
```
✅ "Multiply 5 by 3"
✅ "5 times 3"
✅ "Product of 5 and 3"
✅ "5 × 3"
✅ "5 multiplied by 3"
```

#### Division Patterns
```
✅ "Divide 15 by 3"
✅ "15 divided by 3"
✅ "15 over 3"
✅ "15 ÷ 3"
✅ "Quotient of 15 and 3"
```

#### Square Root Patterns
```
✅ "Square root of 144"
✅ "√144"
✅ "sqrt(144)"
✅ "What is the square root of 144?"
```

#### Power/Exponent Patterns
```
✅ "2 to the power of 8"
✅ "2 raised to 8"
✅ "2^8"
✅ "2 ** 8"
✅ "2 to the 8th"
```

#### Mean/Average Patterns
```
✅ "Average of 10, 20, 30"
✅ "Mean of 10, 20, 30"
✅ "Calculate the average of 10, 20, 30"
✅ "What is the mean of 10, 20, 30?"
```

---

## 💡 Best Practices for Prompts

### ✅ DO:

**Be Specific**
```
✅ "Add 15 and 25"
❌ "Do math with 15 and 25"
```

**Use Clear Conjunctions**
```
✅ "Add 5 and 3, then multiply by 2"
✅ "Add 5 and 3, after that multiply by 2"
❌ "Add 5 and 3 multiply by 2"  // Ambiguous
```

**State Operations Clearly**
```
✅ "Calculate the average of 10, 20, 30"
❌ "What about 10, 20, 30?"  // Unclear intent
```

### ❌ AVOID:

**Vague Language**
```
❌ "Do something with these numbers"
❌ "Process this data"
❌ "Figure out what to do"
```

**Multiple Operations Without Order**
```
❌ "Multiply 5 by 3 and add 10 and divide by 2"
   // Which first? Ambiguous!
   
✅ "Multiply 5 by 3, then add 10, then divide by 2"
   // Clear sequence
```

**Mixing Different Contexts**
```
❌ "Calculate average of 10, 20, 30 and also tell me a joke"
   // System only handles math
```

---

## 🔬 Advanced: Understanding LLM Decision Making

### Example 16: How LLM Interprets Context

#### 👤 User Prompt
```
"I have five apples and buy three more. How many do I have?"
```

#### 🧠 LLM Internal Processing (Simplified)

**Step 1: Extract Intent**
```
Keywords: "five", "buy three more", "how many"
Action: Increase quantity
Operation: Addition
```

**Step 2: Extract Numbers**
```
"five" → 5
"three more" → 3
```

**Step 3: Generate Plan**
```json
{
  "steps": [
    {"operation": "add", "args": [5, 3], "description": "5 maçãs + 3 maçãs"}
  ]
}
```

**Result:** System executes `add(5, 3) = 8`

---

### Example 17: Word Problem

#### 👤 User Prompt
```
"If a train travels 60 km in the first hour and 80 km in the second hour, what's the average speed?"
```

#### 🧠 LLM Processing

**Analysis:**
- Two distances: 60 km, 80 km
- Question asks for "average"
- Operation: mean/average

**Plan:**
```json
{
  "steps": [
    {"operation": "mean", "args": [60, 80], "description": "Velocidade média"}
  ]
}
```

**Result:** `70.0` km/h

---

## 🎯 Testing Your Understanding

Try to predict the agent flow for these prompts:

### Challenge 1
```
"Calculate 2 to the power of 10"
```

<details>
<summary>Click to see answer</summary>

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "power", "args": [2, 10], "description": "2^10"}
  ]
}
```

**Execution:** `power(2, 10) = 1024.0`

</details>

### Challenge 2
```
"Find the mean of 4, 9, 16, then take its square root"
```

<details>
<summary>Click to see answer</summary>

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "mean", "args": [4, 9, 16], "description": "Média"},
    {"operation": "sqrt", "args": ["$result_0"], "description": "√média"}
  ]
}
```

**Execution:**
- Step 0: `mean(4, 9, 16) = 9.666...`
- Step 1: `sqrt(9.666) = 3.109...`

</details>

### Challenge 3
```
"Multiply 3 by 4, add the result to 8, then divide everything by 2"
```

<details>
<summary>Click to see answer</summary>

**LLM Plan:**
```json
{
  "steps": [
    {"operation": "multiply", "args": [3, 4], "description": "3 × 4"},
    {"operation": "add", "args": ["$result_0", 8], "description": "+ 8"},
    {"operation": "divide", "args": ["$result_1", 2], "description": "÷ 2"}
  ]
}
```

**Execution:**
- Step 0: `multiply(3, 4) = 12.0`
- Step 1: `add(12.0, 8) = 20.0`
- Step 2: `divide(20.0, 2) = 10.0`

**Verification:** `(3 × 4 + 8) ÷ 2 = (12 + 8) ÷ 2 = 20 ÷ 2 = 10 ✅`

</details>

---

## 🚀 Next Steps

Now that you understand the agent flow:

1. **Try the examples** in the running system
2. **Modify the prompts** slightly and observe changes
3. **Create your own specialist** for new operations
4. **Experiment with complex chains** (4+ steps)
5. **Read [ARCHITECTURE.md](ARCHITECTURE.md)** for deeper understanding

---

## 📝 Summary

**Key Takeaways:**

✅ Every prompt goes through: Input → Planning → Validation → Execution → Output

✅ The LLM acts as a "task planner", not executor

✅ `$result_N` enables chaining operations

✅ Specialists are isolated, single-responsibility executors

✅ Sandbox ensures security at validation stage

✅ Clear, specific prompts yield best results

✅ The same patterns scale from math to trading to automation

---

**Questions?** Open an issue or check the [main README](README.md)!

**Want to contribute examples?** See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Created with 📚 for learning | v1.0 | 2026**
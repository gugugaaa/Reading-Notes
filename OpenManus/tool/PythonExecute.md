# PythonExecute 工具详解

`PythonExecute` 是 OpenManus 框架中一个用于安全执行 Python 代码的工具，它提供了一种隔离且受控的方式来运行动态生成的 Python 代码片段。

## 核心功能

1. **安全执行环境**：在隔离的进程中执行代码，防止对主程序的影响
2. **超时控制**：防止无限循环或长时间运行的代码阻塞系统
3. **输出捕获**：捕获`print`语句的输出结果
4. **异常处理**：捕获并返回代码执行过程中的错误

## 技术实现

`PythonExecute` 使用以下技术来实现安全执行:

### 1. 多进程隔离

```python
proc = multiprocessing.Process(
    target=self._run_code, args=(code, result, safe_globals)
)
proc.start()
proc.join(timeout)
```

通过 Python 的 `multiprocessing` 库在单独的进程中执行代码，确保即使代码出现问题也不会影响主程序。

### 2. 输出重定向

```python
output_buffer = StringIO()
sys.stdout = output_buffer
exec(code, safe_globals, safe_globals)
```

使用 `StringIO` 对象捕获 `print` 语句的输出，而不是直接输出到控制台。

### 3. 超时机制

```python
proc.join(timeout)
if proc.is_alive():
    proc.terminate()
    # 返回超时信息
```

如果代码执行超过设定时间（默认 5 秒），进程会被强制终止，返回超时信息。

### 4. 全局环境控制

```python
if isinstance(__builtins__, dict):
    safe_globals = {"__builtins__": __builtins__}
else:
    safe_globals = {"__builtins__": __builtins__.__dict__.copy()}
```

通过控制代码执行的全局环境，提供基本的安全保障。

## 执行流程

1. 接收要执行的 Python 代码字符串和可选的超时设置
2. 创建共享字典用于跨进程传递结果
3. 在隔离进程中执行代码
4. 捕获标准输出或异常信息
5. 处理超时情况，如有必要则终止执行
6. 返回执行结果或错误信息

## 使用注意事项

1. **仅捕获 print 输出**：函数返回值不会被捕获，需要使用 `print` 语句显示结果
2. **默认超时 5 秒**：长时间运行的任务会被终止
3. **不适合交互式代码**：不能执行需要用户输入的代码
4. **共享状态有限**：由于在单独进程中执行，无法直接访问主程序的变量和状态

这个工具特别适合在 AI 代理环境中安全地执行动态生成的代码，同时提供足够的安全保障防止潜在的恶意使用或意外错误。
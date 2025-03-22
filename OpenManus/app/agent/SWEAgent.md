# SWEAgent: OpenManus 的软件工程智能体

## SWE 概述

"SWE"是 Software Engineer（软件工程师）的缩写。在 OpenManus 框架中，`SWEAgent` 是一个专门为软件开发和编程任务设计的智能体，它能够像一名真正的软件工程师那样工作，通过命令行界面和文件编辑器执行各种编程任务。

## SWEAgent 核心特点

### 1. 主要定位与用途

`SWEAgent` 是一个自主编程智能体，专注于：
- 代码编写与修改
- 程序调试与测试
- 命令行操作
- 文件管理

### 2. 工具集成

```python
available_tools: ToolCollection = ToolCollection(
    Bash(), StrReplaceEditor(), Terminate()
)
```

SWEAgent 集成了三个主要工具：
- **Bash**：执行命令行操作（如 ls, cd, mkdir 等）
- **StrReplaceEditor**：编辑代码文件（查看、修改、创建文件）
- **Terminate**：结束执行流程

这些工具使 SWEAgent 能够完成从文件浏览到代码编辑的完整开发流程。

### 3. 工作目录追踪

```python
bash: Bash = Field(default_factory=Bash)
working_dir: str = "."

async def think(self) -> bool:
    # Update working directory
    self.working_dir = await self.bash.execute("pwd")
    self.next_step_prompt = self.next_step_prompt.format(
        current_dir=self.working_dir
    )
    
    return await super().think()
```

SWEAgent 会自动追踪当前工作目录，这是它区别于其他智能体的重要特点：
- 每次执行思考循环时自动更新 `working_dir`
- 将当前工作目录注入到提示模板中
- 提供类似终端的环境感知能力

### 4. 系统提示设计

`system_prompt` 使用 `SYSTEM_PROMPT` 模板，这个模板专门为编程活动设计：
- 定义了命令行交互格式 `bash-$`
- 要求智能体每次只执行一个工具调用
- 强调代码缩进的重要性
- 提供文件导航和编辑指导

## SWEAgent 在 OpenManus 中的位置

SWEAgent 在 OpenManus 的继承体系中：
```
BaseAgent
  └── ToolCallAgent
       └── SWEAgent
```

它继承自 `ToolCallAgent`，是一个专门化的实现，为软件开发场景定制。

## 工作流程

1. **环境感知**：通过 `think()` 方法获取当前工作目录
2. **命令执行**：调用 `Bash()` 工具执行命令行操作
3. **文件编辑**：使用 `StrReplaceEditor()` 工具查看和修改代码
4. **迭代开发**：循环执行上述步骤直至完成任务或达到最大步骤数

## 应用场景

SWEAgent 适用于：
- 编写新功能或修复 bug
- 代码重构和优化
- 构建和测试应用
- 文件系统操作（如创建目录、移动文件）
- 项目依赖管理

SWEAgent 在 OpenManus 中扮演了"编程专家"的角色，能够处理从简单脚本到复杂应用的各种软件开发任务，为用户提供自动化编程能力。
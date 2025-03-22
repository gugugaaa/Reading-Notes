# ReActAgent：中间抽象层

# ReActAgent 简要笔记

## 核心概念
- ReActAgent 是 OpenManus 中的抽象代理类，实现了 ReAct (Reasoning + Acting) 模式
- 继承自 BaseAgent，为各种专业化代理提供基础架构

## 关键特性
- 分离思考 (think) 和行动 (act) 为独立步骤
- 内置状态管理和步骤限制 (max_steps)
- 支持内存系统和 LLM 集成

## 工作流程
1. `step()` 方法调用 `think()` 进行推理
2. 根据推理结果决定是否调用 `act()` 执行操作
3. 子类通过具体实现 `think()` 和 `act()` 来实现特定功能

## 在 OpenManus 中的应用
```
BaseAgent
  └── ReActAgent
```
作为中间抽象层，被用于构建各种专业代理，如工具调用代理、浏览器代理、规划代理等，每种代理共享相同的思考-行动循环基础结构。
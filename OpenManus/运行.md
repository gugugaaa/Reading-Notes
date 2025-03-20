# OpenManus 运行文件对比分析

这三个文件代表了 OpenManus 项目中不同的运行方式，各有不同的功能和复杂度：

## 1. main.py - 基础直接模式

最简单的运行方式：
- 直接创建 `Manus` 代理实例
- 获取用户输入并通过代理处理
- 没有复杂的流程管理
- 适用于简单的测试或基础应用场景

```python
agent = Manus()
await agent.run(prompt)
```

## 2. run_flow.py - 流程管理模式

引入流程系统的中等复杂度运行方式：
- 创建一个包含 `Manus` 代理的字典
- 使用 `FlowFactory` 创建 `PLANNING` 类型的流程
- 有超时控制（1小时）
- 跟踪和输出执行时间
- 适用于复杂任务的处理和规划

```python
agents = {"manus": Manus()}
flow = FlowFactory.create_flow(flow_type=FlowType.PLANNING, agents=agents)
result = await flow.execute(prompt)
```

## 3. run_mcp.py - MCP 控制器模式

最复杂的运行方式：
- 使用 `MCPAgent` 代替 `Manus` 代理
- 支持多种连接模式（stdio 或 SSE）
- 提供交互式模式、单次运行模式和默认模式
- 完整的命令行参数支持和资源管理
- 适用于更高级的应用场景，特别是需要与外部服务器交互的情况

```python
runner = MCPRunner()
await runner.initialize(connection_type, server_url)
# 根据不同模式运行
```

## 主要区别

- run_flow.py 使用 Manus，而 run_mcp.py 使用 MCPAgent
- **处理方式**：从直接处理到流程系统再到服务器连接
- **灵活性**：从简单固定到高度可配置
- **应用场景**：从基础测试到复杂任务处理再到高级应用

根据您的需求复杂度和使用场景选择合适的运行方式。
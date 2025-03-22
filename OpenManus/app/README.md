# OpenManus项目结构及模块简介

通过分析代码，我可以为您梳理OpenManus项目中app文件夹的结构和各个模块功能：

## 📁 app目录结构

```
app/
├── agent/             # 智能体实现
├── prompt/            # 提示词模板
├── schema/            # 数据结构定义
├── tool/              # 工具集合
│   ├── search/        # 搜索功能实现
│   └── ...
├── sandbox/           # 沙箱执行环境
├── bedrock.py         # AWS Bedrock集成
├── config.py          # 配置管理
├── exceptions.py      # 异常定义
├── llm.py             # 大语言模型接口
└── logger.py          # 日志系统
```

## 📝 主要模块简介

### 1. agent 模块
包含各种不同功能的智能体实现：

- **BaseAgent**: 所有智能体的基类，提供基础功能
- **ToolCallAgent**: 支持工具调用的智能体基类
- **ReActAgent**: 实现ReAct范式的智能体
- **BrowserAgent**: 浏览器操作智能体
- **CoTAgent**: 实现思维链(Chain-of-Thought)的智能体
- **SWEAgent**: 软件工程师智能体，专注于代码执行和自然语言交互
- **PlanningAgent**: 规划型智能体
- **MCPAgent**: 模型上下文协议(MCP)智能体，可以连接MCP服务器
- **Manus**: 多功能通用智能体，整合了浏览器和多种工具能力

### 2. prompt 模块
存储各种智能体使用的提示词模板：

- **browser.py**: 浏览器智能体提示词
- **manus.py**: Manus智能体提示词
- **mcp.py**: MCP智能体提示词
- **swe.py**: 软件工程师智能体提示词
- **toolcall.py**: 工具调用智能体提示词

### 3. tool 模块
实现各种工具功能：

- **BaseTool**: 所有工具的基类
- **BrowserUseTool**: 浏览器操作工具，支持网页交互
- **PythonExecute**: Python代码执行工具
- **StrReplaceEditor**: 字符串替换编辑工具
- **Terminate**: 终止操作工具
- **WebSearch**: 网络搜索工具
- **PlanningTool**: 规划工具

#### 3.1 search 子模块
实现各种搜索功能：
- **bing_search.py**: 必应搜索实现

### 4. llm.py
大语言模型接口实现：

- 支持OpenAI API及兼容接口
- 支持多模态模型和工具调用
- 实现API错误处理和重试逻辑
- 支持AWS Bedrock等多种后端

### 5. config.py
应用配置管理：

- LLM设置（API密钥、模型选择、参数等）
- 浏览器设置
- 沙箱设置
- 搜索设置

### 6. bedrock.py
AWS Bedrock集成：

- 实现OpenAI API兼容接口
- 转换请求和响应格式
- 支持工具调用

### 7. sandbox 模块
提供安全的执行环境：

- 隔离代码执行
- 资源限制
- 网络控制

## 🔄 核心功能流程

1. **智能体初始化**: 通过LLM、工具和提示词创建特定类型的智能体
2. **用户请求处理**: 智能体接收用户请求并规划行动
3. **工具调用**: 智能体使用工具执行具体操作（如浏览器操作、代码执行等）
4. **状态维护**: 智能体维护对话历史和状态
5. **响应生成**: 基于工具执行结果生成最终响应

OpenManus的设计遵循模块化原则，通过组合不同的智能体和工具可以构建各种复杂任务的自动化解决方案。

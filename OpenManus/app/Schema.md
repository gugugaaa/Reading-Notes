# OpenManus Schema 类解析

schema.py 文件定义了 OpenManus 项目中的核心数据结构，用于构建基于大语言模型的智能代理系统。下面是各个类的详细解析：

## 消息角色和工具选择枚举

### `Role` 类
- 字符串枚举，定义了消息的角色类型
- 包含四种角色：
  - `SYSTEM`：系统消息，提供指令和背景
  - `USER`：用户消息，表示用户输入
  - `ASSISTANT`：助手消息，表示 AI 回复
  - `TOOL`：工具消息，表示工具执行结果

### `ToolChoice` 类
- 字符串枚举，定义工具选择策略
- 包含三个选项：
  - `NONE`：不使用工具
  - `AUTO`：自动决定是否使用工具
  - `REQUIRED`：强制使用工具

## 代理状态

### `AgentState` 类
- 字符串枚举，表示代理的执行状态
- 状态包括：
  - `IDLE`：空闲状态
  - `RUNNING`：运行中
  - `FINISHED`：已完成
  - `ERROR`：发生错误

## 工具调用相关

### `Function` 类
- 表示函数调用的基本模型
- 属性：
  - `name`：函数名称
  - `arguments`：函数参数（JSON 字符串）

### `ToolCall` 类
- 表示工具/函数调用的详细信息
- 属性：
  - `id`：调用的唯一标识符
  - `type`：调用类型，默认为 "function"
  - `function`：Function 对象，包含名称和参数

## 核心消息类

### `Message` 类
- 表示对话系统中的一条消息
- 主要属性：
  - `role`：消息角色（必需）
  - `content`：消息内容（可选）
  - `tool_calls`：工具调用列表（可选）
  - `name`：名称（可选，用于工具消息）
  - `tool_call_id`：工具调用 ID（可选）
  - `base64_image`：Base64 编码的图像（可选）
- 支持操作符重载：
  - 支持 `Message + list`、`Message + Message` 和 `list + Message` 操作
- 提供多种工厂方法创建不同类型消息：
  - `user_message`：创建用户消息
  - `system_message`：创建系统消息
  - `assistant_message`：创建助手消息
  - `tool_message`：创建工具结果消息
  - `from_tool_calls`：从原始工具调用创建助手消息

## 记忆管理

### `Memory` 类
- 管理对话历史记录
- 属性：
  - `messages`：消息列表
  - `max_messages`：最大消息数量限制（默认100）
- 方法：
  - `add_message`：添加单条消息，超出上限时移除最旧消息
  - `add_messages`：批量添加多条消息
  - `clear`：清空所有消息
  - `get_recent_messages`：获取最近 n 条消息
  - `to_dict_list`：将消息列表转换为字典列表形式

这些类为 OpenManus 项目提供了强大的对话管理、工具调用和状态跟踪功能，形成了智能代理系统的核心数据结构。
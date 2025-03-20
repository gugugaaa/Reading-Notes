# BaseAgent：基类

## 基础设计

BaseAgent 作为 OpenManus 代理系统的抽象基类，结合了 Pydantic 数据验证和 ABC 抽象类功能，提供了统一的代理行为框架。

## 关键属性

- **身份信息**: `name`(必填)和`description`(可选)
- **提示系统**: `system_prompt`和`next_step_prompt`
- **核心组件**: `llm`, `memory`, `state`
- **执行控制**: `max_steps=10`, `current_step`, `duplicate_threshold=2`

## 主要功能

### 初始化与配置
- `initialize_agent`: 确保 LLM 和 Memory 实例正确配置
- 允许额外字段(`extra="allow"`)和任意类型(`arbitrary_types_allowed=True`)

### 状态管理
- `state_context`: 异步上下文管理器保证状态转换安全
- 支持状态: IDLE → RUNNING → (FINISHED/ERROR) → IDLE

### 内存操作
- `update_memory`: 支持四种角色消息(user/system/assistant/tool)
- `messages`属性: 提供对内存内容的访问和修改

### 执行流程
- `run`: 主执行循环，处理请求并按步骤执行
- 参数: `request`(可选的初始用户请求)
- 返回: 步骤结果的摘要字符串

### 循环检测
- `is_stuck`: 通过检测重复内容发现循环
- `handle_stuck_state`: 添加特殊提示词改变策略
- 提示词: "Observed duplicate responses. Consider new strategies and avoid repeating ineffective paths already attempted."

### 抽象接口
- `step`: 子类必须实现的方法，定义单步行为

## 设计亮点

1. **安全的状态转换**: 使用上下文管理器确保状态一致性
2. **灵活的内存系统**: 结构化消息存储对话历史
3. **自动循环检测**: 识别重复响应并主动干预
4. **清晰的扩展点**: 通过抽象方法定义扩展接口
5. **健壮的错误处理**: 异常自动转为ERROR状态

## 使用模式

1. 子类继承 BaseAgent 并实现 step 方法
2. 初始化代理时提供名称和可选的系统提示
3. 调用 run 方法启动执行，可选传入初始请求
4. 代理自动管理状态、记忆和执行流程
5. 循环检测机制防止代理卡住

使用 state_context 进行任何需要临时状态变更的操作，确保状态能正确恢复。

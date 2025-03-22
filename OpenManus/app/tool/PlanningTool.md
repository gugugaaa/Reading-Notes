# PlanningTool 类详解

`PlanningTool` 是 OpenManus 框架中一个强大的计划管理工具，用于帮助代理（agents）创建和管理解决复杂任务的结构化计划。

## 核心功能

`PlanningTool` 提供以下主要功能：

1. **计划创建与管理**：创建、更新、查看和删除任务计划
2. **步骤跟踪**：跟踪计划中每个步骤的执行状态
3. **进度可视化**：展示任务完成百分比和各状态步骤数量
4. **活动计划管理**：维护当前活动计划的状态

## 命令系统

该工具支持以下七种命令：

| 命令 | 描述 |
|------|------|
| `create` | 创建新计划 |
| `update` | 更新现有计划 |
| `list` | 列出所有可用计划 |
| `get` | 获取特定计划详情 |
| `set_active` | 将特定计划设置为活动计划 |
| `mark_step` | 更新步骤状态和备注 |
| `delete` | 删除计划 |

## 数据结构

每个计划在内部表示为一个字典，包含以下键：
- `plan_id`：唯一标识符
- `title`：计划标题
- `steps`：步骤列表
- `step_statuses`：每个步骤的状态
- `step_notes`：每个步骤的备注

## 步骤状态

支持四种步骤状态：
- `not_started`：未开始 `[ ]`
- `in_progress`：进行中 `[→]`
- `completed`：已完成 `[✓]`
- `blocked`：被阻塞 `[!]`

## 工作流示例

1. 创建一个新计划：
   ```python
   planning_tool.execute(
       command="create",
       plan_id="task_123",
       title="实现新功能",
       steps=["分析需求", "设计解决方案", "编写代码", "测试功能", "部署上线"]
   )
   ```

2. 标记步骤状态：
   ```python
   planning_tool.execute(
       command="mark_step",
       plan_id="task_123",
       step_index=1,
       step_status="in_progress",
       step_notes="正在进行架构设计"
   )
   ```

3. 查看计划进度：
   ```python
   planning_tool.execute(command="get", plan_id="task_123")
   ```

## PlanningTool 方法实现详解

`PlanningTool` 是一个强大的任务计划管理器，下面我将详细讲解其各个方法的实现：

### 1. 主执行方法 `execute`

这是工具的入口方法，根据命令类型分发到对应的私有处理方法：

```python
async def execute(self, *, command, plan_id=None, title=None, steps=None, ...):
    if command == "create":
        return self._create_plan(plan_id, title, steps)
    elif command == "update":
        return self._update_plan(plan_id, title, steps)
    # ... 其他命令处理
```

### 2. 计划创建 `_create_plan`

```python
def _create_plan(self, plan_id, title, steps) -> ToolResult:
```

- **参数验证**：确保 plan_id、title 必须提供，steps 必须是非空字符串列表
- **重复检查**：确保 plan_id 不与现有计划冲突
- **计划初始化**：创建新计划，为每个步骤设置初始状态("not_started")和空备注
- **设置活动计划**：自动将新创建的计划设为活动计划

### 3. 计划更新 `_update_plan`

```python
def _update_plan(self, plan_id, title, steps) -> ToolResult:
```

- **智能状态保留**：当更新步骤时，对于保持不变的步骤会保留其状态和备注
- **状态重置**：对于新添加的步骤，状态被设置为"not_started"
- **选择性更新**：可以只更新标题或只更新步骤

### 4. 计划列表 `_list_plans`

```python
def _list_plans(self) -> ToolResult:
```

- **可用性检查**：检查是否有可用计划
- **简明摘要**：为每个计划显示标题、ID、活动状态和完成进度
- **活动标记**：标记当前活动的计划

### 5. 获取计划详情 `_get_plan`

```python
def _get_plan(self, plan_id) -> ToolResult:
```

- **ID智能推断**：如果未指定plan_id，使用当前活动计划
- **存在性验证**：确保指定的计划存在
- **格式化输出**：调用`_format_plan`生成格式化的计划信息

### 6. 设置活动计划 `_set_active_plan`

```python
def _set_active_plan(self, plan_id) -> ToolResult:
```

- **参数校验**：确保提供了plan_id且对应的计划存在
- **活动状态更新**：将指定计划设为当前活动计划

### 7. 标记步骤 `_mark_step`

```python
def _mark_step(self, plan_id, step_index, step_status, step_notes) -> ToolResult:
```

- **活动计划回退**：若未指定plan_id，使用当前活动计划
- **索引验证**：确保step_index在有效范围内
- **状态验证**：确保step_status是有效的状态值
- **选择性更新**：可以只更新状态或只更新备注

### 8. 删除计划 `_delete_plan`

```python
def _delete_plan(self, plan_id) -> ToolResult:
```

- **参数验证**：确保提供了plan_id且对应的计划存在
- **活动计划清理**：如果删除的是当前活动计划，会清除活动计划标记

### 9. 格式化计划 `_format_plan`

```python
def _format_plan(self, plan: Dict) -> str:
```

- **标题信息**：显示计划标题和ID
- **进度统计**：计算和显示总步骤数、已完成步骤数和完成百分比
- **状态分布**：显示各种状态(已完成、进行中、阻塞、未开始)的步骤数量
- **步骤可视化**：以符号标记不同状态([✓]已完成,[→]进行中,[!]阻塞,[ ]未开始)
- **备注展示**：若步骤有备注，在步骤下方显示

通过这些精心设计的方法，`PlanningTool`提供了一个完整的计划管理系统，适用于复杂任务的分解和跟踪。

这个工具特别适合处理复杂任务，可以将大型问题分解为可管理的步骤，并跟踪每个步骤的进度，确保任务能够有条理地完成。
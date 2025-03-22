# OpenManus Config.py 解析

config.py 文件是 OpenManus 项目的配置管理核心，采用单例模式确保全局只有一个配置实例。该模块负责加载、解析和提供对项目各组件配置的访问。

## 核心组件

### 路径管理
```python
def get_project_root() -> Path:
    """获取项目根目录"""
    return Path(__file__).resolve().parent.parent

PROJECT_ROOT = get_project_root()
WORKSPACE_ROOT = PROJECT_ROOT / "workspace"
```
- 确定项目根目录和工作空间目录的常量

### 配置模型（使用 Pydantic）

1. **LLMSettings**：大语言模型配置
   - 模型名称、API信息、请求参数等
   - 支持不同的API类型（Azure、OpenAI、Ollama）

2. **ProxySettings**：代理服务器配置
   - 服务器地址、认证信息

3. **SearchSettings**：搜索引擎配置
   - 主搜索引擎和备选引擎
   - 重试策略和延迟设置

4. **BrowserSettings**：浏览器配置
   - 无头模式、安全设置
   - Chrome实例路径、WebSocket连接等
   - 代理设置（嵌套ProxySettings）

5. **SandboxSettings**：沙盒执行环境
   - Docker容器配置
   - 资源限制（内存、CPU）
   - 网络访问控制

6. **AppConfig**：应用总配置
   - 集成以上所有配置类型

### 配置管理类

Config类是核心配置管理器：
- 实现单例模式（`__new__`方法）
- 线程安全的初始化（使用`threading.Lock()`）
- 配置文件查找和加载
- 配置解析与模型构造
- 通过属性访问器提供各部分配置

## 配置加载流程

1. 查找配置文件：优先使用`config/config.toml`，不存在则使用示例配置
2. 解析TOML格式配置
3. 提取基础LLM配置和模型特定覆盖配置
4. 处理浏览器、代理、搜索和沙盒配置
5. 构造最终的AppConfig对象

## 使用方式

通过导出的全局实例访问配置：
```python
config = Config()  # 全局单例实例

# 使用示例
llm_config = config.llm
sandbox_settings = config.sandbox
browser_settings = config.browser_config
```

这种设计确保了配置的一致性和线程安全，同时通过Pydantic模型提供了类型安全和自动验证功能，为整个OpenManus项目提供灵活可靠的配置管理。
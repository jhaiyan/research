# 通过 MLX-LM 在 macOS（Apple Silicon）上运行 HuggingFace 上的模型

## 目的

本文演示在 macOS（Apple Silicon）上，通过 [MLX-LM][4] 把 [Hugging Face][5] 上的开源大模型跑起来作为本地 API Server，再经由 [LiteLLM][6] 转换为 [Anthropic Messages API][7] 协议，供 [Claude Code][8] 作为本地 LLM 后端调用。涉及的相关软件与平台如下。

## 相关组件

- **MLX**：Apple 机器学习研究团队开源的数组框架，专为 Apple Silicon 设计，采用统一内存架构（CPU 与 GPU 共享同一块内存），提供与 NumPy / PyTorch 类似的 Python 与 C++ API，支持 `grad()` / `vmap()` / `compile()` 等函数式变换，2023 年 12 月开源。[🔗](https://github.com/ml-explore/mlx "ml-explore/mlx · GitHub") [🔗](https://ml-explore.github.io/mlx/ "MLX Documentation")
- **MLX-LM**：Apple 机器学习研究团队在 [`ml-explore/mlx-lm`](https://github.com/ml-explore/mlx-lm) 仓库中维护的 Python 包，基于 MLX 在 Apple Silicon 上运行大语言模型，提供 `mlx_lm.chat`、`mlx_lm.generate`、`mlx_lm.server` 等命令行工具以及 Python API。[🔗](https://github.com/ml-explore/mlx-lm "ml-explore/mlx-lm · GitHub")
- **Hugging Face**：面向机器学习社区的协作平台，托管模型（Models）、数据集（Datasets）与交互式应用（Spaces）；提供 `huggingface_hub` Python 库与 `hf` 命令行工具，用于下载、上传与管理模型与数据集。[🔗](https://huggingface.co/ "Hugging Face – The AI community building the future.") [🔗](https://huggingface.co/docs/huggingface_hub "Hugging Face Hub Documentation")
- **mlx-community**：[Hugging Face](https://huggingface.co/mlx-community) 上的组织，托管已转换为 MLX 格式（含 4-bit/8-bit 等量化版本）的模型权重，可在 Apple Silicon 上被 MLX-LM / mlx-swift-examples / mlx-vlm / mlx-audio 等直接加载。[🔗](https://huggingface.co/mlx-community "mlx-community · Hugging Face")
- **Claude Code**：Anthropic 官方提供的智能编程 CLI，可直接读取代码库、编辑文件、执行命令并接入开发工具；通过环境变量 `ANTHROPIC_BASE_URL` 与 `ANTHROPIC_AUTH_TOKEN` 接入符合 Anthropic Messages API 规范的 LLM Gateway。[🔗](https://code.claude.com/docs/en/overview "Claude Code Overview")
- **LiteLLM**：BerriAI 开源的 AI Gateway（代理服务器），提供 OpenAI 兼容的统一接口，覆盖 100+ LLM 提供方，可作为协议转换层将 OpenAI-compatible 后端映射为 Anthropic Messages API，供 Claude Code 调用。[🔗](https://github.com/BerriAI/litellm "BerriAI/litellm · GitHub")
- **uv**：[Astral](https://astral.sh) 发布的 Rust 编写的 Python 包与项目管理器，速度比 `pip` / `pip-tools` 快 10–100 倍，可作为 `pipx` 的替代用于安装隔离的 CLI 工具（如本文中的 `mlx-lm`、`huggingface_hub`、`litellm[proxy]`）。[🔗](https://docs.astral.sh/uv/ "uv · Astral Docs")

## 步骤

1. 安装 `uv`。

   ```bash
   brew install uv
   ```

2. 安装 MLX-LM 和 Hugging Face CLI。

   ```bash
   uv tool install mlx-lm
   uv tool install huggingface_hub
   ```

   > `mlx` 会随 MLX-LM 一起安装。

3. 用一个极小模型快速验证本地运行。

   ```bash
   mlx_lm.chat --model mlx-community/SmolLM2-135M-Instruct
   ```

   > 首次运行会自动下载模型；之后直接读取本地缓存。

4. 查看本地已经下载的所有 Hugging Face 模型。

   ```bash
   hf cache ls --filter "type=model"
   ```

   > Hugging Face 官方目前使用 `hf cache ls` 管理本地缓存。([Hugging Face][1])

5. 删除某个本地模型。

   ```bash
   hf cache rm model/mlx-community/SmolLM2-135M-Instruct
   ```

   > 会先询问确认；加 `-y` 可直接删除。([Hugging Face][1])

6. 查看 Hugging Face 上有哪些 MLX 模型可用。

   ```bash
   hf models list --author mlx-community
   ```

   > 也可以直接浏览 [mlx-community 模型列表](https://huggingface.co/mlx-community/models?utm_source=chatgpt.com)。不是所有 Hugging Face 模型都能直接用 MLX-LM，优先选 `mlx-community` 中已经转换好的模型。

7. 如果要让其他程序调用模型，启动本地 API Server。

   ```bash
   mlx_lm.server --model mlx-community/SmolLM2-135M-Instruct
   ```

   > 默认地址为 `http://127.0.0.1:8080`，提供 OpenAI-compatible `/v1/chat/completions` API。可通过 `--port`（简写 `-p`）修改端口、通过 `--host` 修改监听地址，例如 `mlx_lm.server --model mlx-community/SmolLM2-135M-Instruct --port 9000 --host 0.0.0.0`。([GitHub][2])

8. Claude Code **不能直接连接 MLX-LM**，因为 Claude Code 使用 Anthropic Messages API，而 MLX-LM 提供 OpenAI-compatible API；可以用 LiteLLM 做协议转换。

   ```bash
   uv tool install 'litellm[proxy]'
   ```

   创建 `litellm.yaml`：

   ```yaml
   model_list:
     - model_name: local
       litellm_params:
         model: openai/mlx-community/SmolLM2-135M-Instruct
         api_base: http://127.0.0.1:8080/v1
         api_key: none
   ```

   启动：

   ```bash
   litellm --config litellm.yaml
   ```

   > LiteLLM 可以把 OpenAI-compatible 后端转换成 Claude Code 所需要的 Anthropic-compatible 接口。Anthropic 官方也明确支持 Claude Code 通过 LiteLLM Gateway 使用 `ANTHROPIC_BASE_URL`。([Claude Platform Docs][3])

9. 让 Claude Code 使用这个本地模型。

   ```bash
   ANTHROPIC_BASE_URL=http://127.0.0.1:4000 \
   ANTHROPIC_AUTH_TOKEN=local \
   claude --model local
   ```

   > 此时链路是：`Claude Code → LiteLLM → MLX-LM → 本地模型`。([Claude Platform Docs][3])
   > **135M 模型只适合验证运行链路，不足以真正驱动 Claude Code 写代码。** 验证成功后，再换成 20B～30B 级 Coding 模型。

[1]: https://huggingface.co/docs/huggingface_hub/en/guides/cli?utm_source=chatgpt.com "Command Line Interface (CLI) · Hugging Face"
[2]: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md?utm_source=chatgpt.com "mlx-lm/mlx_lm/SERVER.md at main · ml-explore/mlx-lm · GitHub"
[3]: https://docs.anthropic.com/en/docs/claude-code/llm-gateway?utm_source=chatgpt.com "LLM gateway configuration - Anthropic"
[4]: https://github.com/ml-explore/mlx-lm "ml-explore/mlx-lm · GitHub"
[5]: https://huggingface.co/ "Hugging Face – The AI community building the future"
[6]: https://github.com/BerriAI/litellm "BerriAI/litellm · GitHub"
[7]: https://platform.claude.com/docs/en/api/messages "Messages API · Anthropic"
[8]: https://code.claude.com/docs/en/overview "Claude Code Overview"

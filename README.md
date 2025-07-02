# PDF分割工具

一个基于Python的PDF文件分割脚本，可将大PDF文件按指定页数分割成多个小文件。

## 功能特点

- 按指定页数分割PDF文件
- 使用PyPDF2库进行可靠的PDF处理
- 通过JSON配置文件进行参数设置
- 保持原始PDF文件质量
- 生成具有清晰命名规则的分割文件

## 系统要求

- Python 3.x
- uv包管理工具

## 安装步骤

1. 克隆本仓库或下载脚本文件
2. 安装所需依赖：
   ```bash
   uv pip install PyPDF2
   ```
3. 同步项目依赖：
   ```bash
   uv sync
   ```

## 配置说明

创建`config.json`文件，内容如下：

```json
{
    "input_path": "输入PDF文件路径",
    "output_path": "输出目录路径",
    "max_pages_per_file": 10
}
```

- `input_path`: 要分割的PDF文件路径
- `output_path`: 分割后文件的保存目录
- `max_pages_per_file`: (可选) 每个分割文件的最大页数(默认: 10)

## 使用方法

1. 编辑`config.json`文件，设置正确的路径
2. 使用uv运行脚本：
   ```bash
   uv run python main.py
   ```

3. 脚本将在输出目录生成分割后的PDF文件，命名格式为：
   - `原文件名_part_1.pdf`
   - `原文件名_part_2.pdf`
   - 以此类推

## 示例

对于一个25页的PDF文件使用默认设置：
- 将生成3个文件：
  - part_1.pdf (1-10页)
  - part_2.pdf (11-20页)
  - part_3.pdf (21-25页)

## 注意事项

- 请确保输入PDF路径正确且可访问
- 输出目录必须已存在
- 脚本会覆盖输出目录中同名的现有文件
- 建议使用uv虚拟环境运行脚本

import os
import json
from glob import glob
from PyPDF2 import PdfMerger

def read_config(config_path):
    """
    读取配置文件，获取输入和输出文件夹路径。
    :param config_path: 配置文件路径
    :return: 输入文件夹路径和输出文件夹路径
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        input_dir = config.get('input_dir')
        output_dir = config.get('output_dir')
        if not input_dir or not output_dir:
            raise ValueError("配置文件中缺少输入或输出文件夹路径")
        return input_dir, output_dir
    except FileNotFoundError:
        raise FileNotFoundError(f"配置文件 {config_path} 未找到")
    except json.JSONDecodeError:
        raise ValueError(f"配置文件 {config_path} 格式错误")

def group_pdf_files(input_dir):
    """
    遍历输入文件夹，识别并分组以 `_part_*.pdf` 命名的 PDF 文件。
    :param input_dir: 输入文件夹路径
    :return: 分组后的 PDF 文件字典，键为文件名前缀，值为文件列表
    """
    pdf_files = glob(os.path.join(input_dir, '*_part*.pdf'))
    grouped_files = {}
    for file_path in pdf_files:
        file_name = os.path.basename(file_path)
        # 提取文件名前缀（去掉 `_part_*.pdf` 部分）
        prefix = file_name.split('_part_')[0]
        if prefix not in grouped_files:
            grouped_files[prefix] = []
        grouped_files[prefix].append(file_path)
    return grouped_files

def merge_pdfs(grouped_files, output_dir):
    """
    按文件名分组，将每个组中的 PDF 文件按顺序合并。
    :param grouped_files: 分组后的 PDF 文件字典
    :param output_dir: 输出文件夹路径
    """
    for prefix, files in grouped_files.items():
        # 按文件名排序（确保 `_part1.pdf` 在前，`_part2.pdf` 在后）
        files.sort()
        merger = PdfMerger()
        for file_path in files:
            try:
                merger.append(file_path)
            except Exception as e:
                print(f"合并文件 {file_path} 时出错: {e}")
        output_path = os.path.join(output_dir, f"{prefix}.pdf")
        try:
            with open(output_path, 'wb') as f:
                merger.write(f)
            print(f"成功合并文件到 {output_path}")
        except Exception as e:
            print(f"保存合并后的文件 {output_path} 时出错: {e}")
        finally:
            merger.close()

def main():
    """
    主函数，执行 PDF 文件合并流程。
    """
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        input_dir, output_dir = read_config(config_path)
        grouped_files = group_pdf_files(input_dir)
        if not grouped_files:
            print("未找到任何以 `_part*.pdf` 命名的文件")
            return
        merge_pdfs(grouped_files, output_dir)
    except Exception as e:
        print(f"程序运行出错: {e}")

if __name__ == "__main__":
    main()
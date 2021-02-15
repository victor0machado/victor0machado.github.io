"""
Script para buildar os materiais das disciplinas

- Percorre recursivamente o diretório em execução;
- Gera .html a partir de .adoc e .pdf a partir de .doc e .ppt;
- Move arquivos gerados para diretório `assets\<disciplina>`.
"""
import os
import subprocess
import shutil

from pathlib import Path

CURR_PATH: Path = Path(os.getcwd())
ASST_PATH: Path = Path(os.path.realpath(os.path.dirname(__file__))) / "assets"

EXCLUDE_FILES_EXP = "_gab"

DEFAULT_MATERIAL_FOLDER = "materiais"


def call_cmd(cmd):
    """Roda uma instrução."""
    error = subprocess.call(cmd, shell=True)
    if error:
        print(f"Build failed! Error code: {error}")
    else:
        print("Success!")

    return error


def build_adoc(basename, ext, src_path, out_path):
    """Builda documentação em .adoc em HTML."""
    print(f"Building {src_path}\\{basename}{ext}...")
    filepath = os.path.join(src_path, f"{basename}{ext}")
    cmd = ["asciidoctor", filepath, "-D", str(out_path)]
    call_cmd(cmd)


def build_office(basename, ext, src_path, out_path):
    """Builda documentação do office em pdf."""
    print(f"Building {src_path}\\{basename}{ext}...")
    filepath = os.path.join(src_path, f"{basename}{ext}")
    destpath = os.path.join(out_path, f"{basename}.pdf")
    cmd = ["officetopdf", filepath, destpath]
    call_cmd(cmd)


BUILDERS = {
    ".docx": build_office,
    ".pptx": build_office,
    ".adoc": build_adoc
}


def build_course_files(from_path, to_path):
    """Build os arquivos de uma disciplina."""
    if not os.path.isdir(to_path):
        os.mkdir(to_path)

    copy_img(from_path, to_path)
    for filename in os.listdir(from_path):
        basename, ext = os.path.splitext(filename)
        if ext in BUILDERS.keys() and EXCLUDE_FILES_EXP not in basename:
            BUILDERS[ext](basename, ext, from_path, to_path)


def copy_img(assets_path, out_path):
    """Copia as imagens para o destino."""
    print("Copying images...")
    out_img_path = os.path.join(out_path, "img")
    img_path = os.path.join(assets_path, "img")

    if os.path.isdir(img_path):
        if os.path.isdir(out_img_path):
            shutil.rmtree(out_img_path)

        shutil.copytree(img_path, out_img_path)


def prepare_path(pathname: Path) -> None:
    """
    Limpa a pasta de destino dos materiais,
    ou cria a pasta se não existir.
    """
    if os.path.exists(pathname):
        shutil.rmtree(pathname)

    os.makedirs(pathname)


def clear_log_files(dir_path):
    """Limpa recursivamente arquivos de log em um diretório."""
    for entry_name in os.listdir(dir_path):
        entry_path = os.path.join(dir_path, entry_name)
        if os.path.isdir(entry_path):
            clear_log_files(entry_path)
        if entry_name == "debug.log":
            os.remove(entry_path)


def get_name(pathname: Path) -> str:
    """Obtém o nome da última pasta do diretório em execução."""
    return str(pathname.relative_to(pathname.parent))


def main():
    """Entrada do script."""
    course = get_name(CURR_PATH)
    prepare_path(ASST_PATH / course)
    build_course_files(CURR_PATH / DEFAULT_MATERIAL_FOLDER, ASST_PATH / course)
    clear_log_files(CURR_PATH)


if __name__ == "__main__":
    main()
